from django.db import models

# Create your models here.
class Attachment(models.Model):
    data = models.DateField(auto_now_add=True)
    file = models.FileField()
    url = models.URLField()
