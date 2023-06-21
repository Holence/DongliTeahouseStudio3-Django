from django.db import models
from attachments.models import Attachment

# Create your models here.
class Text(models.Model):
    date = models.DateField()
    content = models.TextField(blank=True, null=True)
    index = models.PositiveIntegerField(
        default=0,
        blank=False,
        null=False,
    )
    
    attachments = models.ManyToManyField(Attachment, blank=True)

    class Meta:
        ordering = ['index']
