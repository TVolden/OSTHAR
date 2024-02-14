from django.db import models
from studies.models import Subject

# Create your models here.
class Record(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    localtime = models.DateTimeField()
    servertime = models.DateTimeField()
    behavior = models.CharField(max_length=200)
    affect = models.CharField(max_length=200)
    intervention = models.CharField(max_length=200)
    marked = models.BooleanField(default=False)
    note = models.CharField(max_length=200, null=True)
    exclude = models.BooleanField(default=False)