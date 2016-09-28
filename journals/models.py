from __future__ import unicode_literals

from django.db import models
from subjects.models import Subject

# Create your models here.


class Journal(models.Model):
    title = models.CharField(max_length=100)
    subject = models.ForeignKey(Subject)
    description = models.CharField(max_length=1000)
    feeOSB = models.FloatField()

    class JSONAPIMeta:
        resource_name = 'journals'
