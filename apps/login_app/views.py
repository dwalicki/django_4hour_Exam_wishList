# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'login_app/index.html')

def register(request):
    #User.objects.all.().delete()
    results = User.objects.validate(request.POST)
    if results['status'] == True:
        user = User.objects.creator(request.POST)
        request.session['userid'] = user.id        
    else:
        for error in results['errors']:
            messages.error(request, error)

    request.session['name'] = request.POST['name']
    return redirect('wish_list/')

def login(request):
    results = User.objects.loginVal(request.POST)
    if results['status'] == False:
        messages.error(request, 'Username and/or password is incorrect')
        return redirect('/')
    request.session['username'] = results['user'].username
    request.session['userid'] = results['user'].id
    request.session['name'] = results['user'].name
    return redirect('wish_list/')