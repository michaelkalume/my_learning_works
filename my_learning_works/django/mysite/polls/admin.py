# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Choice, Question

admin.site.register(Choice)
admin.site.register(Question)

# Register your models here.
