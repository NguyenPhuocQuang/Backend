
from django.db import models

from .machine import Machines
from .protocol_library import ProtocolLibrarys


class ConnectionProfiles(models.Model):
    created_date = models.DateTimeField(auto_now_add=True, db_column="CreatedDate")
    created_by = models.CharField(max_length=100, null=True, blank=True, db_column="CreatedBy")
    updated_date = models.DateTimeField(auto_now=True, db_column="UpdatedDate")
    updated_by = models.CharField(max_length=100, null=True, blank=True, db_column="UpdatedBy")
    is_deleted = models.BooleanField(default=False, db_column="IsDeleted")
    deleted_date = models.DateTimeField(null=True, blank=True, db_column="DeletedDate")
    deleted_by = models.CharField(max_length=100, null=True, blank=True, db_column="DeletedBy")

    machine = models.ForeignKey(
        Machines,
        on_delete=models.CASCADE,
        related_name="connection_profiles",
        db_column="MachineId"
    )
    protocol = models.ForeignKey(
        ProtocolLibrarys,
        on_delete=models.PROTECT,
        related_name="connection_profiles",
        db_column="ProtocolId"
    )
    source_name = models.CharField(max_length=255, db_column="SourceName")
    polling_interval_ms = models.IntegerField(default=1000, db_column="PollingIntervalMs")
    worker_service_name = models.CharField(max_length=255, null=True, blank=True, db_column="WorkerServiceName")
    instance_config_json = models.JSONField(null=True, blank=True, db_column="InstanceConfigJson")

    class Meta:
        db_table = "ConnectionProfiles"

    def __str__(self):
        return f"{self.machine.name} - {self.protocol.protocol_name}"