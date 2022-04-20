#from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User

class Todo(models.Model):
   title = models.CharField(max_length=100)
   description = models.TextField()
   completed = models.BooleanField(default=False)

   def _str_(self):
     return self.title

class Event_Host(models.Model):
  host_id = models.OneToOneField(User, on_delete=models.CASCADE)
  host_fname = models.CharField(max_length=30,null=True)
  host_lname = models.CharField(max_length=30,null=True)

  def _str_(self):
    return self.Username


class Event_Users(models.Model):
  user_id = models.IntegerField(primary_key=True)
  user_fname = models.CharField(max_length=30,null=True)
  user_fname = models.CharField(max_length=30,null=True)
  username = models.CharField(max_length=30,null=True)

  def _str_(self):
    return self.Username


class Event_Socials(models.Model):
  social_id = models.IntegerField(primary_key=True)
  user_id = models.ForeignKey(Event_Users, on_delete=models.CASCADE,null=True)
  host_id = models.ForeignKey(Event_Host, on_delete=models.CASCADE,null=True)
  twitter = models.CharField(max_length=30,null=True)
  instagram = models.CharField(max_length=30,null=True)
  snapchat = models.CharField(max_length=30,null=True)
  cashapp = models.CharField(max_length=30,null=True)
  user_bio = models.CharField(max_length=255,null=True)
  event_host = models.BooleanField(default=False)
  event_performer = models.BooleanField(default=False)
  event_guest = models.BooleanField(default=False)

class Event(models.Model):
  event_id = models.IntegerField(primary_key=True)
  event_code = models.IntegerField()
  event_name = models.CharField(max_length=55,null=True)
  event_location = models.CharField(max_length=30,null=True)
  event_org = models.CharField(max_length=30,null=True)
  event_host = models.ForeignKey(Event_Users, on_delete=models.CASCADE)
  event_start_date = models.DateTimeField()
  event_end_date = models.DateTimeField()
  event_image = models.ImageField()
 

class Event_Attendee(models.Model):
  event_id = models.ForeignKey(Event, on_delete=models.CASCADE,max_length=12)
  user_id = models.ForeignKey(Event_Users, on_delete=models.CASCADE, max_length=12)
