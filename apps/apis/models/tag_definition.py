
from django.db import models
from .connection_profile import ConnectionProfiles


class TagDefinitions(models.Model):
    created_date = models.DateTimeField(auto_now_add=True, db_column="CreatedDate")
    created_by = models.CharField(max_length=100, null=True, blank=True, db_column="CreatedBy")
    updated_date = models.DateTimeField(auto_now=True, db_column="UpdatedDate")
    updated_by = models.CharField(max_length=100, null=True, blank=True, db_column="UpdatedBy")
    is_deleted = models.BooleanField(default=False, db_column="IsDeleted")
    deleted_date = models.DateTimeField(null=True, blank=True, db_column="DeletedDate")
    deleted_by = models.CharField(max_length=100, null=True, blank=True, db_column="DeletedBy")

    profile = models.ForeignKey(
        ConnectionProfiles,
        on_delete=models.CASCADE,
        related_name="tag_definitions",
        db_column="ProfileId"
    )
    tag_key = models.CharField(max_length=100, db_column="TagKey")
    tag_name = models.CharField(max_length=255, db_column="TagName")
    address_config_json = models.JSONField(null=True, blank=True, db_column="AddressConfigJson")
    data_type = models.CharField(max_length=50, db_column="DataType")
    scaling_factor = models.FloatField(default=1.0, db_column="ScalingFactor")
    unit = models.CharField(max_length=50, null=True, blank=True, db_column="Unit")

    class Meta:
        db_table = "TagDefinitions"

    def __str__(self):
        return self.tag_name