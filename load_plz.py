import settings
from django.core.management  import setup_environ

setup_environ(settings)

from information.models import Location

import csv
import codecs

dataFormat = 'mbcs';

class LoadData():
	print "Loading location data"
	count = 0
	with codecs.open('db/plz_l_20120124.txt', 'rb', dataFormat) as f:
		reader = csv.reader(f, dialect=csv.excel_tab)
		for row in reader:
			print row[2], '=', row[4]
			l = Location(name=row[4], plz=row[2])
			l.save()
			count = count + 1
	print count
	
LoadData()