#from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User

class Todo(models.Model):
   title = models.CharField(max_length=100)
   description = models.TextField()
   completed = models.BooleanField(default=False)

   def _str_(self):
     return self.title


class Event_Users(models.Model):
  User_id = models.IntegerField(primary_key=True)
  User_Fname = models.CharField(max_length=15)
  User_Lname = models.CharField(max_length=15)
  Username = models.CharField(max_length=15)
  Social_id = models.CharField(max_length=15)
  Bio = models.CharField(max_length=255)

  def _str_(self):
    return self.Username


class Event_Socials(models.Model):
  Social_id = models.IntegerField(primary_key=True)
  User_id = models.ForeignKey(Event_Users, on_delete=models.CASCADE)
  twitter = models.CharField(max_length=15)
  instagram = models.CharField(max_length=15)
  snapchat = models.CharField(max_length=15)
  cashapp = models.CharField(max_length=15)
  Event_host = models.BooleanField(default=False)
  Event_performer = models.BooleanField(default=False)
  Event_guest = models.CharField(max_length=15)

class Event(models.Model):
  Event_id = models.IntegerField(primary_key=True)
  Event_code = models.IntegerField()
  Event_name = models.CharField(max_length=25)
  Event_location = models.CharField(max_length=15)
  Event_Org = models.CharField(max_length=15)
  Event_host = models.ForeignKey(Event_Users, on_delete=models.CASCADE)
  Event_start_date = models.DateTimeField()
  Event_end_date = models.DateTimeField()
  Event_image = models.ImageField()
 

class Event_Attendee(models.Model):
  Event_id = models.ForeignKey(Event, on_delete=models.CASCADE,max_length=12)
  User_id = models.ForeignKey(Event_Users, on_delete=models.CASCADE, max_length=12)
