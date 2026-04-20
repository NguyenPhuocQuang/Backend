from django.db import models
from .category_machine import CategoryMachines
from .department import Departments

class Machines(models.Model):
    created_date = models.DateTimeField(auto_now_add=True, db_column="CreatedDate")
    created_by = models.CharField(max_length=100, null=True, blank=True, db_column="CreatedBy")
    updated_date = models.DateTimeField(auto_now=True, db_column="UpdatedDate")
    updated_by = models.CharField(max_length=100, null=True, blank=True, db_column="UpdatedBy")
    is_deleted = models.BooleanField(default=False, db_column="IsDeleted")
    deleted_date = models.DateTimeField(null=True, blank=True, db_column="DeletedDate")
    deleted_by = models.CharField(max_length=100, null=True, blank=True, db_column="DeletedBy")

    category_machine = models.ForeignKey(
        CategoryMachines,
        on_delete=models.PROTECT,
        related_name="machines",
        db_column="CategoryMachineId"
    )
    name = models.CharField(max_length=255, db_column="Name")
    normalized_name = models.CharField(max_length=255, null=True, blank=True, db_column="NormalizedName")
    department = models.ForeignKey(
        Departments,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="machines",
        db_column="DepartmentId"
    )
    image_url = models.CharField(max_length=500, null=True, blank=True, db_column="ImageUrl")
    location = models.CharField(max_length=255, null=True, blank=True, db_column="Location")
    machine_code = models.CharField(max_length=100, unique=True, db_column="MachineCode")
    status = models.CharField(max_length=100, null=True, blank=True, db_column="Status")

    class Meta:
        db_table = "Machines"

    def __str__(self):
        return f"{self.machine_code} - {self.name}"