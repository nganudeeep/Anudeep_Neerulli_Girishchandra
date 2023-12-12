'''from datetime import timezone'''
from time import timezone
from django.db import models

# Create your models here.
# contacts/models.py
from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True)
    notes = models.TextField(blank=True)
    created_time = models.DateTimeField()

    def __str__(self):
        return self.name
