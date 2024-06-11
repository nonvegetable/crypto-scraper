from django.db import models

# Create your models here.
from django.db import models

class Job(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    status = models.CharField(max_length=20, default='PENDING')
    created_at = models.DateTimeField(auto_now_add=True)

class Task(models.Model):
    coin = models.CharField(max_length=20)
    data = models.JSONField(blank=True, null=True) 
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='tasks')
