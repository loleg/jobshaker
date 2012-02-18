from django.db import models
from django.contrib import auth
import datetime

class Intent(models.Model):
	name = models.CharField(max_length=70)
	icon = models.CharField(max_length=99, blank=True, null=True)
	back = models.CharField(max_length=99, blank=True, null=True)
	def __unicode__(self):
		return self.name
	
class UserProfile(models.Model):
	user = models.OneToOneField(auth.models.User)
	nickname = models.CharField(max_length=30)
	profession = models.CharField(max_length=30)
	postcode = models.IntegerField() # why not working? min_value=1000, max_value=9999)
	aboutme = models.TextField(max_length=500)
	english = models.BooleanField()
	german = models.BooleanField()
	french = models.BooleanField()
	italian = models.BooleanField()
	other_lang = models.CharField('other languages', max_length=70, blank=True, null=True)
	birth_year = models.IntegerField(blank=True, null=True) #, min_value=1900, max_value=2050)
	GENDER_CHOICES = (
	        (u'M', u'Male'),
	        (u'F', u'Female'),
	    )
	sex = models.CharField(max_length=2, choices=GENDER_CHOICES, blank=True, null=True)
	def __unicode__(self):
		return self.nickname

class Post(models.Model):
	pub_date = models.DateTimeField('date published', auto_now_add=True)
	user = models.ForeignKey(UserProfile, editable=False)
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
	user = models.ForeignKey(UserProfile, editable=False)
	post = models.ForeignKey(Post, editable=False)
	flag = models.BooleanField()
	like = models.BooleanField()
	comment = models.TextField()
	def __unicode__(self):
		return self.comment
