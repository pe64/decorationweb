# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class UserInfo(models.Model):
    name = models.CharField('姓名',max_length=30)
    #email = models.EmailField(max_length=30)
    qq=models.CharField(blank=True,max_length=11)
    telphone = models.CharField(max_length=11)
    address = models.CharField(blank=True,max_length=1024)
    park = models.CharField(blank=True,max_length=1024)
    housenumber = models.CharField(blank=True,max_length=1024)
    housesize = models.IntegerField(blank=True)
    date = models.DateField(blank=True,auto_now_add=True)

    def __unicode__(self):
        return '姓名：【'+self.name+'】'+'电话：【'+self.telphone+'】'
        #memo = models.TextField(max_length=300)
    #img = models.ImageField(null=True, blank=True, upload_to="upload")