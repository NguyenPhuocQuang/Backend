from django.urls import re_path
from .consumers import AllMachinesTagsConsumer

websocket_urlpatterns = [
    re_path(r"ws/all-machines-tags/$", AllMachinesTagsConsumer.as_asgi()),
]
