
from django.db import models
from .tag_definition import TagDefinitions

class LiveTags(models.Model):
    last_updated = models.DateTimeField(auto_now=True, db_column="LastUpdated")
    tag = models.OneToOneField(
        TagDefinitions,
        on_delete=models.CASCADE,
        related_name="live_tag",
        db_column="TagId"
    )
    value = models.TextField(null=True, blank=True, db_column="Value")

    class Meta:
        db_table = "LiveTags"

    def __str__(self):
        return f"{self.tag.tag_name} - {self.value}"