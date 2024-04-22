from django.db import models
import uuid

class AppointmentBook(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False,null=True, blank=True, unique=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    disease = models.CharField(max_length=200, null=True, blank=True)
    phone = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name