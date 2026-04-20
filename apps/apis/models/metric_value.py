from  django.db import models
from .tag_definition import TagDefinitions


class MetricValues(models.Model):
    log_time = models.DateTimeField(db_column="LogTime")
    tag = models.ForeignKey(
        TagDefinitions,
        on_delete=models.CASCADE,
        related_name="metric_values",
        db_column="TagId"
    )
    value = models.TextField(null=True, blank=True, db_column="Value")

    class Meta:
        db_table = "MetricValues"

    def __str__(self):
        return f"{self.tag.tag_name} - {self.log_time}"