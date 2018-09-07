# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

import bcrypt

import re
# Create your models here.


class UserManager(models.Manager):
    def loginVal(self, postData):
        results = {'status': True, 'errors':[], 'user': None}
        users = self.filter(username = postData['username'])

        if len(users) < 1:
            results['status'] == False
        else:
            if bcrypt.checkpw(postData['pw'].encode(), users[0].password.encode()):
                results['user'] = users[0]
            else:    
                results['errors'].append('Password is correct.')
                results['status'] = False     

        return results

    def creator(self, postData):
        user = self.create(name = postData['name'], username = postData['username'], password = bcrypt.hashpw(postData['pw'].encode(), bcrypt.gensalt()))
        return user

    def validate(self, postData):
        results = {'status': True, 'errors':[]}
        if len(postData['name']) < 3:
            results['errors'].append('Your name is too short.')
            results['status'] = False
        if len(postData['username']) < 3:
            results['errors'].append('Your username is too short.')
            results['status'] = False          
        if postData['pw'] != postData['confirm_pw']:
            results['errors'].append('Your password does not match.')
            results['status'] = False            
        if len(postData['pw']) < 5:
            results['errors'].append('Password needs to be five characters long.')
            results['status'] = False             
        return results

class User(models.Model):
    name = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    objects = UserManager()