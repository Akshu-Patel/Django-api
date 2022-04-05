from email.policy import default
from django.db import models
from django.forms import BooleanField


class Enroll(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    username = models.CharField(max_length=200, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=200)
    confirm_password = models.CharField(max_length=200)
    user_type = models.CharField(max_length=200)

    def __str__(self): 
          return self.username

class Project(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=200,unique=True)
    start_date = models.DateField()
    end_date = models.DateField()
    billable = models.BooleanField()
    technology = models.CharField(max_length=200)
    project_manager = models.ForeignKey(Enroll,to_field='username',on_delete=models.DO_NOTHING, default=1)
    
    def __str__(self): 
        return self.name

class Task(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    title = models.CharField(max_length=200,unique=True)
    start_date = models.DateField()
    end_date = models.DateField()
    developer = models.ForeignKey(Enroll,to_field='username',on_delete=models.DO_NOTHING,default=1)
    project = models.ForeignKey(Project,to_field='name',on_delete=models.DO_NOTHING, default=1)
    completed = models.BooleanField()
    STATUS = (
       ('pending','pending'),
       ('completed','completed'),
       ('in-progress','in-progress'),
       ('testing','testing'),
   )
    status = models.CharField(max_length=32,choices=STATUS,default='pending')
    
    def __str__(self): 
        return self.title

class Bug(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    head = models.CharField(max_length=200)
    resolved = models.BooleanField()
    tester = models.ForeignKey(Enroll,to_field='username',on_delete=models.DO_NOTHING, default=1)
    task = models.ForeignKey(Task,to_field='title',on_delete=models.DO_NOTHING, default=1)
    
    def __str__(self): 
        return self.head