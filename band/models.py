# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import datetime

# Create your models here.

class Band(models.Model):
  name = models.CharField(max_length = 200, null = False, unique = True)
  date_added = models.DateField(default = datetime.datetime.now())
  image = models.CharField(max_length = 400, null = True, blank = True)
  bio = models.TextField(max_length = 5000, null = True, blank = True)
