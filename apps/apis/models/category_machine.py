from django.db import models


class CategoryMachines(models.Model):
    created_date = models.DateTimeField(auto_now_add=True, db_column="CreatedDate")
    created_by = models.CharField(max_length=100, null=True, blank=True, db_column="CreatedBy")
    updated_date = models.DateTimeField(auto_now=True, db_column="UpdatedDate")
    updated_by = models.CharField(max_length=100, null=True, blank=True, db_column="UpdatedBy")
    is_deleted = models.BooleanField(default=False, db_column="IsDeleted")
    deleted_date = models.DateTimeField(null=True, blank=True, db_column="DeletedDate")
    deleted_by = models.CharField(max_length=100, null=True, blank=True, db_column="DeletedBy")

    name = models.CharField(max_length=255, db_column="Name")

    class Meta:
        db_table = "CategoryMachines"

    def __str__(self):
        return self.name
