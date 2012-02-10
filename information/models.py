from django.db import models

class Location(models.Model):
	name = models.CharField(max_length=50)
	plz = models.IntegerField()
	def __unicode__(self):
		return self.name