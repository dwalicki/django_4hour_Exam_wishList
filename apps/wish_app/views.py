# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from models import Wish
from django.shortcuts import render, redirect
from django.urls import reverse
from ..login_app.models import User

# Create your views here.

def index(request):
    context = {
        'name': request.session['name'],
        'wished_items': Wish.objects.filter(wished_by=User.objects.get(pk=request.session['userid'])),
        'havent_wished': Wish.objects.exclude(wished_by=User.objects.get(pk=request.session['userid']))
    }
    return render(request, 'wish_app/index.html', context)

def add_item(request):
    return render(request, 'wish_app/edit.html')

def add(request):
    item = Wish.objects.create(item=request.POST['item'],uploader=User.objects.get(pk=request.session['userid']))
    return redirect('home')

def delete(request, wish_pk):
    item = Wish.objects.get(pk=wish_pk)
    item.delete()
    return redirect(reverse('home'))

def remove(request, wish_pk):
    item = Wish.objects.get(pk=wish_pk)
    item.wished_by.remove(User.objects.get(pk=request.session['userid']))
    item.save()
    return redirect(reverse('home'))

def add_to(request, wish_pk):
    item = Wish.objects.get(pk=wish_pk)
    item.wished_by.add(User.objects.get(pk=request.session['userid']))
    item.save()
    return redirect(reverse('home'))

def who_added(request, wish_pk):
    context = {
        'item': Wish.objects.get(id=wish_pk),
    }
    return render(request, 'wish_app/who_added.html', context)

def logout(request):
    request.session.flush()
    return redirect('/')
