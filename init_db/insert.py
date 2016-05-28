import requests
import json
from api.models import *


f=open("init_db/states.json")
x=f.read()
x=json.loads(x)
states = x
# out = []
for st in states:
	try:
		obj = StatesUT(name=st['name'],lat=st['_geoloc']['lat'],lng=st['_geoloc']['lng'],place_id=st['place_id'])
		obj.save()
	except:
		pass
	# print res['results']
	# break

f.close()
