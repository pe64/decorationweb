# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class UserInfo(models.Model):
    name = models.CharField(max_length=30)
    #email = models.EmailField(max_length=30)
    qq=models.CharField(max_length=11)
    telphone = models.CharField(max_length=11)
    address = models.CharField(max_length=1024)
    park = models.CharField(max_length=1024)
    hosenumber = models.CharField(max_length=1024)
    hosesize = models.IntegerField()
    date = models.DateField(auto_now_add=True)

    def __unicode__(self):
        return self.name + self.hosenumber + self.park + self.telphone
        #memo = models.TextField(max_length=300)
    #img = models.ImageField(null=True, blank=True, upload_to="upload")