from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Subject(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images')

    class JSONAPIMeta:
        resource_name = 'subjects'
