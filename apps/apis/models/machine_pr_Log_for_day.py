
from django.db import models
from .machine import Machines

class MachineProductionLogForDays(models.Model):
    machine = models.ForeignKey(
        Machines,
        on_delete=models.CASCADE,
        related_name="machine_production_log_for_days",
        db_column="MachineId"
    )
    work_date = models.DateField(db_column="WorkDate")
    program_name = models.CharField(max_length=255, null=True, blank=True, db_column="ProgramName")
    first_run_time = models.DateTimeField(null=True, blank=True, db_column="FirstRunTime")
    last_run_time = models.DateTimeField(null=True, blank=True, db_column="LastRunTime")
    total_run_time_in_minutes = models.IntegerField(default=0, db_column="TotalRunTimeInMinutes")
    error_run_time = models.IntegerField(default=0, db_column="ErrorRunTime")
    total_part = models.IntegerField(default=0, db_column="TotalPart")

    class Meta:
        db_table = "MachineProductionLogForDays"

    def __str__(self):
        return f"{self.machine.name} - {self.work_date}"