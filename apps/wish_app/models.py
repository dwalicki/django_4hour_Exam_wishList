# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from ..login_app.models import User

# Create your models here.

class Wish(models.Model):
    item = models.TextField()
    uploader = models.ForeignKey(User, related_name='added_by')
    wished_by = models.ManyToManyField(User, related_name='wishes')
    date_added = models.DateTimeField(auto_now_add=True)
