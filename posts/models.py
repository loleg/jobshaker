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
	profession = models.CharField(max_length=30)
	postcode = models.IntegerField() # why not working? min_value=1000, max_value=9999)
	english = models.BooleanField()
	german = models.BooleanField()
	french = models.BooleanField()
	italian = models.BooleanField()
	other_lang = models.CharField('Other', max_length=70, blank=True, null=True)
	birth_year = models.IntegerField('Year of birth', blank=True, null=True) #, min_value=1900, max_value=2050)
	GENDER_CHOICES = (
	        (u'M', u'Male'),
	        (u'F', u'Female'),
	    )
	sex = models.CharField(max_length=2, choices=GENDER_CHOICES, blank=True, null=True)
	aboutme = models.TextField('About myself', max_length=500, blank=True, null=True)
	def __unicode__(self):
		return self.user.username

class Post(models.Model):
	pub_date = models.DateTimeField('date published', auto_now_add=True)
	user = models.ForeignKey(UserProfile, editable=False)
	intent = models.ForeignKey(Intent)
	location = models.CharField(max_length=60, blank=True, null=True)
	valid_from = models.DateField(blank=True, null=True) 
	valid_until = models.DateField(blank=True, null=True) 
	comment = models.TextField()
	def __unicode__(self):
		return self.intent.name
	def was_published_today(self):
		return self.pub_date.date() == datetime.date.today()
	
class Reply(models.Model):
	pub_date = models.DateTimeField('date replied', auto_now_add=True)
	user = models.ForeignKey(UserProfile, editable=False)
	post = models.ForeignKey(Post, editable=False)
	reply_to = models.ForeignKey('self', related_name='replies', 
		editable=False, null=True, blank=True)
	# flag = models.BooleanField()
	# like = models.BooleanField()
	comment = models.TextField()
	def __unicode__(self):
		return self.comment
