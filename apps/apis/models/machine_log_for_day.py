from django.db import models
from .machine import Machines

class MachineLogForDays(models.Model):
    machine = models.ForeignKey(
        Machines,
        on_delete=models.CASCADE,
        related_name="machine_log_for_days",
        db_column="MachineId"
    )
    work_date = models.DateField(db_column="WorkDate")
    tag_name = models.CharField(max_length=255, db_column="TagName")
    total_value = models.FloatField(default=0, db_column="TotalValue")
    value_scan_for_day = models.FloatField(default=0, db_column="ValueScanForDay")

    class Meta:
        db_table = "MachineLogForDays"

    def __str__(self):
        return f"{self.machine.name} - {self.tag_name} - {self.work_date}"