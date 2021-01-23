from django.db import models
from django.contrib.auth.models import User
from rest_framework import serializers
class Todos(models.Model):
    todo_id=models.IntegerField(primary_key=True)
    todo_text=models.TextField()
    todo_add_date=models.DateField()
    todo_priporty=models.TextField(default="normal")
    todo_add_time=models.TextField(default="0.0.0")
    todo_updated_time=models.TextField(default="0.0.0")
    todo_status=models.CharField(max_length=50,default="uncompleted")
    author=models.CharField(max_length=500,default=None)
class TodosSerializer(serializers.Serializer):
    todo_id=serializers.IntegerField()
    todo_text=serializers.CharField(max_length=500)
    todo_add_date=serializers.DateField()
    todo_priporty=serializers.CharField(default="normal")
    todo_add_time=serializers.CharField(default="0.0.0")
    todo_updated_time=serializers.CharField(default="0.0.0")
    author=serializers.CharField(max_length=500,default=None)
class TodoUserMedia(models.Model):
    username=models.CharField(max_length=50)
    profile=models.ImageField(upload_to="images")
class NotificationsSettings(models.Model):
    username=models.CharField(max_length=500)
    task_notifications=models.BooleanField(default=False)
    task_completedNotifiication=models.BooleanField(default=False)
    via_email=models.BooleanField(default=False)
    system_notifications=models.BooleanField(default=True)
class Feedback(models.Model):
    username=models.CharField(max_length=500)
    title=models.CharField(max_length=50)
    feedbackmessage=models.TextField()    
class insight(models.Model):
    username=models.CharField(max_length=50,default=None)
    logins=models.IntegerField(default=0)
    changeusername=models.IntegerField(default=0)
    changepassword=models.IntegerField(default=0)
    addtasks=models.IntegerField(default=0)
    deletetasks=models.IntegerField(default=0)
    edittasks=models.IntegerField(default=0)
    completetask=models.IntegerField(default=0)
    searchtask=models.IntegerField(default=0)
    mostsearchkeywords=models.CharField(max_length=1000,default="None")
    date=models.DateField(default=None)
class insightserializer(serializers.Serializer):
    username=serializers.CharField(max_length=50,default=None)
    logins=serializers.IntegerField(default=0)
    changeusername=serializers.IntegerField(default=0)
    changepassword=serializers.IntegerField(default=0)
    addtasks=serializers.IntegerField(default=0)
    deletetasks=serializers.IntegerField(default=0)
    edittasks=serializers.IntegerField(default=0)
    completetask=serializers.IntegerField(default=0)
    searchtask=serializers.IntegerField(default=0)
    mostsearchkeywords=serializers.CharField(max_length=1000,default="None")
    date=serializers.CharField(default=None)
        