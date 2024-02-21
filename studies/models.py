import uuid
from django.db import models

# Create your models here.
class Study(models.Model):
    username = models.CharField(max_length=200)
    software = models.CharField(max_length=200)
    institution = models.CharField(max_length=200)
    trial = models.CharField(max_length=200)
    behavior = models.CharField(max_length=200)
    affect = models.CharField(max_length=200)
    localtime = models.DateTimeField(null=True)
    servertime = models.DateTimeField(null=True)
    intervention = models.CharField(max_length=200)
    session = models.UUIDField(default=uuid.uuid4)
    localendtime = models.DateTimeField(null=True)
    serverendtime = models.DateTimeField(null=True)

    def __str__(self) -> str:
        return f"{self.software}.{self.institution}.{self.trial}"

class Subject(models.Model):
    study = models.ForeignKey(Study, on_delete=models.CASCADE)
    number = models.IntegerField()
    label = models.CharField(max_length=200)

    def __str__(self) -> str:
        return f"{self.pk}: ({self.number}) {self.label}"