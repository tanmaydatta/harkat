import requests
import json

f=open("india_states.geojson")
x=f.read()
x=json.loads(x)
states = x['features']
out = []
for st in states:
	url = "https://maps.googleapis.com/maps/api/geocode/json?address="+st['properties']['NAME_1']+"&key=AIzaSyAmHbz-EvneAAG67FdFZ9JCIVmX1jZzwbk"
	res = requests.get(url).json()
	if len(res['results']) > 0:
		data = {}
		data['name'] = st['properties']['NAME_1'] 
		data['_geoloc'] = res['results'][0]['geometry']['location']
		data['place_id'] = res['results'][0]['place_id']
		out.append(data)
	# print res['results']
	# break

f.close()
f = open("states.json","w")
f.write(json.dumps(out))
f.close()