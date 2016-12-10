# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django import forms

# Create your views here.

class AppointmentInfo(forms.Form):
    name = forms.CharField()
    # email = models.EmailField(max_length=30)
    qq = forms.CharField()
    telphone = forms.CharField()
    address = forms.CharField()
    park = forms.CharField()
    hosenumber = forms.CharField()
    hosesize = forms.CharField()
    date =



def appointment(request):
    if request.method == 'POST':
        af = AppointmentInfo(request.POST)
        if af.is_valid():


    return render(request, 'index.html')
