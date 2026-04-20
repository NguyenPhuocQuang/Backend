
from django.db import models



class ProtocolLibrarys(models.Model):
    created_date = models.DateTimeField(auto_now_add=True, db_column="CreatedDate")
    created_by = models.CharField(max_length=100, null=True, blank=True, db_column="CreatedBy")
    updated_date = models.DateTimeField(auto_now=True, db_column="UpdatedDate")
    updated_by = models.CharField(max_length=100, null=True, blank=True, db_column="UpdatedBy")
    is_deleted = models.BooleanField(default=False, db_column="IsDeleted")
    deleted_date = models.DateTimeField(null=True, blank=True, db_column="DeletedDate")
    deleted_by = models.CharField(max_length=100, null=True, blank=True, db_column="DeletedBy")

    protocol_code = models.CharField(max_length=100, unique=True, db_column="ProtocolCode")
    protocol_name = models.CharField(max_length=255, db_column="ProtocolName")
    form_schema_json = models.JSONField(null=True, blank=True, db_column="FormSchemaJson")
    default_config_json = models.JSONField(null=True, blank=True, db_column="DefaultConfigJson")
    default_worker_image = models.CharField(max_length=255, null=True, blank=True, db_column="DefaultWorkerImage")

    class Meta:
        db_table = "ProtocolLibrarys"

    def __str__(self):
        return self.protocol_name