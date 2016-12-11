# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django import forms
from flweb import models

# Create your views here.

class AppointmentInfo(forms.Form):
    name = forms.CharField()
    # email = models.EmailField(max_length=30)
    qq = forms.CharField()
    telphone = forms.CharField()
    address = forms.CharField()
    park = forms.CharField()
    housenumber = forms.CharField()
    housesize = forms.CharField()




def appointment(request):
    if request.method == 'POST':
        af = AppointmentInfo(request.POST)
        if af.is_valid():
            name=af.cleaned_data['name']
            qq = af.cleaned_data['qq']
            telphone = af.cleaned_data['telphone']
            address = af.cleaned_data['address']
            park = af.cleaned_data['park']
            housenumber = af.cleaned_data['housenumber']
            housesize = af.cleaned_data['housesize']
            print(name)
            models.UserInfo.objects.create(name=name,qq=qq,telphone=telphone,address=address,park=park,housenumber=housenumber,housesize=housesize)
    return render(request, 'index.html')
