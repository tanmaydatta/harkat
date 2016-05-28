import requests
import json

f=open("cities.txt")
x=f.readlines()
# x=json.loads(x)
# states = x['features']
out = []
for ct in x:
	url = "https://maps.googleapis.com/maps/api/geocode/json?address="+ct+"&key=AIzaSyAmHbz-EvneAAG67FdFZ9JCIVmX1jZzwbk"
	res = requests.get(url).json()
	if len(res['results']) > 0:
		data = {}
		try:
			data['name'] = ct 
			data['_geoloc'] = res['results'][0]['geometry']['location']
			data['place_id'] = res['results'][0]['place_id']
			state = ''
			address_components = res['results'][0]['address_components']
			for addr in address_components:
				if 'administrative_area_level_1' in addr['types']:
					state = addr['long_name']
					break
			surl = "https://maps.googleapis.com/maps/api/geocode/json?address="+state+"&key=AIzaSyAmHbz-EvneAAG67FdFZ9JCIVmX1jZzwbk"
			sres = requests.get(surl).json()
			data['state_id'] = sres['results'][0]['place_id']
			data['state'] = state
			out.append(data)
			print ct + " -> " + state 
		except:
			pass
	# print res['results']
	# break

f.close()
f = open("cities.json","w")
f.write(json.dumps(out))
f.close()