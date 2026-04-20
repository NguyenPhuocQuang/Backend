from django.db import models
from .machine import Machines


class MachineProductionLogs(models.Model):
    machine = models.ForeignKey(
        Machines,
        on_delete=models.CASCADE,
        related_name="production_logs",
        db_column="MachineId"
    )
    work_date = models.DateField(db_column="WorkDate")
    first_run_time = models.DateTimeField(null=True, blank=True, db_column="FirstRunTime")
    last_run_time = models.DateTimeField(null=True, blank=True, db_column="LastRunTime")
    total_run_time_in_minutes = models.IntegerField(default=0, db_column="TotalRunTimeInMinutes")
    is_get_time = models.BooleanField(default=False, db_column="IsGetTime")
    program_name = models.CharField(max_length=255, null=True, blank=True, db_column="ProgramName")
    last_cutting_time_in_minutes = models.IntegerField(default=0, db_column="LastCuttingTimeInMinutes")
    total_part = models.IntegerField(default=0, db_column="TotalPart")

    class Meta:
        db_table = "MachineProductionLogs"

    def __str__(self):
        return f"{self.machine.name} - {self.work_date}"