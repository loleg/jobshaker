from django.db import models
from django.contrib import auth
import datetime

class Profession(models.Model):
	name = models.CharField(max_length=30)
	def __unicode__(self):
		return self.name
	
class Place(models.Model):
	name = models.CharField(max_length=30)
	def __unicode__(self):
		return self.name
	
class UserProfile(models.Model):
	user = models.OneToOneField(auth.models.User)
	nickname = models.CharField(max_length=30)
	location = models.ForeignKey(Place)
	profession = models.ForeignKey(Profession)
	def __unicode__(self):
		return self.nickname

class Post(models.Model):
	pub_date = models.DateTimeField('date published', auto_now_add=True)
	user = models.ForeignKey(UserProfile)
	place = models.ForeignKey(Place)
	intent = models.CharField(max_length=70)
	comment = models.TextField()
	def __unicode__(self):
		return self.intent
	def was_published_today(self):
		return self.pub_date.date() == datetime.date.today()
	
class Reply(models.Model):
	pub_date = models.DateTimeField('date replied', auto_now_add=True)
	user = models.ForeignKey(UserProfile)
	post = models.ForeignKey(Post)
	flag = models.BooleanField()
	like = models.BooleanField()
	comment = models.TextField()
	def __unicode__(self):
		return self.pub_date