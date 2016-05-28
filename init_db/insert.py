import requests
import json
from api.models import *


f=open("init_db/cities.json")
x=f.read()
x=json.loads(x)
cities = x
out = []
for st in cities:
	try:
		stobj = StatesUT.objects.get(place_id=st['state_id'])
		# print stobj
		try:
			obj = Cities(name=st['name'],lat=st['_geoloc']['lat'],lng=st['_geoloc']['lng'],place_id=st['place_id'],state_id=stobj.place_id)
			obj.save()
			out.append(st)
		except Exception,e:
			print str(e)
			# break
			pass
	except:
		# print "not found state"
		pass
	
	# print res['results']
	# break

f.close()
f=open("init_db/cities.json","w")
f.write(json.dumps(out))
f.close()
