from django.db import models
from django.contrib import auth
import datetime

class Intent(models.Model):
	name = models.CharField(max_length=70)
	icon = models.CharField(max_length=99)
	back = models.CharField(max_length=99)
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
	other_lang = models.CharField('other languages', max_length=70)
	age = models.IntegerField()
	sex = models.CharField(max_length=1)
	def __unicode__(self):
		return self.nickname

class Post(models.Model):
	pub_date = models.DateTimeField('date published', auto_now_add=True)
	user = models.ForeignKey(UserProfile)
	postcode = models.IntegerField()
	distance = models.IntegerField()
	intent = models.ForeignKey(Intent)
	valid_from = models.DateField('from') 
	valid_until = models.DateField('until') 
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