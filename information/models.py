from django.db import models

def get_location_by_plz(p):
	list = Location.objects.filter(plz=p)
	if len(list) > 0:
		return list[0]
	else:
		# location not found
		return ''

class Location(models.Model):
	name = models.CharField(max_length=50)
	plz = models.IntegerField()
	def __unicode__(self):
		return self.name