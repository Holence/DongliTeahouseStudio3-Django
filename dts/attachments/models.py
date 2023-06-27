from django.db import models

# Create your models here.
class Attachment(models.Model):
    date = models.DateField(auto_now_add=True)
    name = models.CharField(max_length=512)
