import asyncio
import json
from urllib.parse import parse_qs

from asgiref.sync import sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from rest_framework_simplejwt.tokens import AccessToken

from apps.apis.models.machine import Machines
from apps.apis.models.tag_definition import TagDefinitions


class AllMachinesTagsConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.running = False
        self.user = await self.get_authenticated_user()

        if not self.user:
            await self.close(code=4401)
            return

        await self.accept()

    async def disconnect(self, close_code):
        self.running = False

    @sync_to_async
    def get_authenticated_user(self):
        query_string = self.scope.get("query_string", b"").decode()
        params = parse_qs(query_string)
        token = params.get("token", [None])[0]

        if not token:
            return None

        try:
            payload = AccessToken(token)
        except (InvalidToken, TokenError):
            return None

        user_id = payload.get("user_id")
        if not user_id:
            return None

        User = get_user_model()

        try:
            user = User.objects.get(pk=user_id, is_active=True)
        except User.DoesNotExist:
            return None

        return user

    async def receive(self, text_data):
        data = json.loads(text_data)
        action = data.get("action")

        if action == "ping":
            await self.send(text_data=json.dumps({
                "event": "pong",
                "data": {
                    "message": "socket_ok",
                    "user_id": self.user.id,
                    "username": self.user.username,
                },
            }))

        elif action == "start_all_machines":
            if self.running:
                return

            self.running = True

            while self.running:
                payload = await self.get_all_machines_tags_payload()

                await self.send(text_data=json.dumps({
                    "event": "machines_tags_full",
                    "data": payload,
                }))

                await asyncio.sleep(1)

        elif action == "stop_all_machines":
            self.running = False

    @sync_to_async
    def get_all_machines_tags_payload(self):
        machines = (
            Machines.objects
            .filter(is_deleted=False)
            .order_by("id")
        )

        tags = (
            TagDefinitions.objects
            .select_related("profile__machine")
            .select_related("live_tag")
            .filter(
                is_deleted=False,
                profile__machine__is_deleted=False,
            )
            .order_by("profile__machine_id", "id")
        )

        machine_map = {
            machine.id: {
                "machine_id": machine.id,
                "machine_code": machine.machine_code,
                "machine_name": machine.name,
                "status": machine.status,
                "location": machine.location,
                "tags": [],
            }
            for machine in machines
        }

        for tag in tags:
            machine = tag.profile.machine
            live_tag = getattr(tag, "live_tag", None)

            if machine.id not in machine_map:
                continue

            machine_map[machine.id]["tags"].append({
                "tag_id": tag.id,
                "tag_key": tag.tag_key,
                "tag_name": tag.tag_name,
                "data_type": tag.data_type,
                "unit": tag.unit,
                "value": live_tag.value if live_tag else None,
                "last_updated": live_tag.last_updated.isoformat() if live_tag else None,
            })

        return list(machine_map.values())
