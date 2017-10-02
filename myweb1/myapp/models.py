from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Info(models.Model):

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)

    def __unicode__(self):
        return self.first_name
