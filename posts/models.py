from django.db import models
from django.contrib import auth
import datetime

class Intent(models.Model):
	name = models.CharField(max_length=70)
	icon = models.CharField(max_length=99, blank=True, null=True)
	back = models.CharField(max_length=99, blank=True, null=True)
	def __unicode__(self):
		return self.name

class Profession(models.Model):
	name = models.CharField(max_length=50)
	def __unicode__(self):
		return self.name
	
class UserProfile(models.Model):
	user = models.OneToOneField(auth.models.User)
	nickname = models.CharField(max_length=30)
	profession = models.ForeignKey(Profession)
	postcode = models.IntegerField()
	english = models.BooleanField()
	german = models.BooleanField()
	french = models.BooleanField()
	italian = models.BooleanField()
	other_lang = models.CharField('other languages', max_length=70, blank=True, null=True)
	age = models.IntegerField(blank=True, null=True)
	GENDER_CHOICES = (
	        (u'M', u'Male'),
	        (u'F', u'Female'),
	    )
	sex = models.CharField(max_length=2, choices=GENDER_CHOICES, blank=True, null=True)
	def __unicode__(self):
		return self.nickname

class Post(models.Model):
	pub_date = models.DateTimeField('date published', auto_now_add=True)
	user = models.ForeignKey(UserProfile)
	postcode = models.IntegerField(blank=True, null=True)
	distance = models.IntegerField(blank=True, null=True)
	intent = models.ForeignKey(Intent)
	valid_from = models.DateField('from', blank=True, null=True) 
	valid_until = models.DateField('until', blank=True, null=True) 
	comment = models.TextField()
	def __unicode__(self):
		return self.intent.name
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