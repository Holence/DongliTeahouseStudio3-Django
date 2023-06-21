from django.db import models
from attachments.models import Attachment
from texts.models import Text

# Create your models here.
class Concept(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField(null=True, blank=True)
    childs = models.ManyToManyField("self", blank=True, symmetrical=False, related_name="parents")
    relatives = models.ManyToManyField("self", blank=True, symmetrical=True)
    
    texts = models.ManyToManyField(Text, blank=True)
    attachments = models.ManyToManyField(Attachment, blank=True)
