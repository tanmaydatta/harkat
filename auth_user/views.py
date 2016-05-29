from django.shortcuts import render
from django.core.cache import cache
import json
from django.http import *
from facebook import GraphAPI, GraphAPIError
from django.core.cache import cache
from django.contrib.auth.password_validation import validate_password
from models import *
import hashlib
import string
import harkat.settings
# Create your views here.

def response(status, msg, *args):
	# args are tuples
	res = {}
	res['status'] = status
	res['msg'] = msg
	for arg in args:
		res[arg[0]] = arg[1]
	return HttpResponse(json.dumps(res))


def check_and_add_user(data,fb_id,g_id):
	try:
		name = data['name']
	    password = data['password']
	    username = data['username']
	    email = data['email']
	    city = data['city']
	    state = data['state']
	    try:
	    	check_pass = validate_password(password)
	    except ValidationError as e:
	    	return response("error", "password_validation", ("ValidationError",str(e)),("error_type", "password"))
	    try:
	    	if not city:
	    		city = None
	    		pass
	    	check_city = Cities.objects.get(place_id=city)
	    except:
	    	return response("error", "invalid city")
	    try:
	    	check_state = StatesUT.objects.get(place_id=state)
	    except:
	    	return response("error", "invalid state/union-territory")
	   	try:
	   		obj = Huser(name=name,username=username,city=city,state=state,g_id=g_id,fb_id=fb_id,password=hashlib.sha224(password).hexdigest())
	   		obj.save()
	   	except IntegrityError as e:
	   		return response("error", "username already exists", ("IntegrityError",str(e)), ("error_type", "dup_user"))
	   	except:
	   		return response("error", "internal server error", ("error_type","server"))
	   	try:
	   		obj.email = email
	   		obj.save()
	   	except IntegrityError as e:
	   		return response("error", "email already in use", ("IntegrityError",str(e)), ("error_type", "dup_email"))
	   	except:
	   		return response("error", "internal server error", ("error_type","server"))
	   	auth_token = str(obj.id) + str(obj.username) + ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(10))
 		auth_token = hashlib.sha224(auth_token).hexdigest()
 		access_token = auth_token + ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(10))
 		access_token = hashlib.sha224(access_token).hexdigest()
 		try:
 			cache.set("auth_" + auth_token, obj.id, timeout=None)
 			cache.set(obj.id, "auth_" + auth_token, timeout=None)
 			cache.set("access_" + access_token, obj.id)
 		except:
 			return response("error", "error generating token")
	   	res = response("sucess", "user signed up successfully")
	   	res['access_token'] = access_token
	   	res['auth_token'] = auth_token
	   	res.set_cookie("auth_token",value=auth_token,httponly=True,secure=harkat.settings.SECURE)
	   	res.set_cookie("access_token",value=access_token,httponly=True,secure=harkat.settings.SECURE)
	   	return res

	except:
		return response("error", "Incomplete data sent", ("error_type","Incomplete_data"))


def signup(request):
	if request.method == "POST":
		data = json.loads(request.body)
		try:
			if data['type'] == 'facebook':
				try:
					access_token = request.META['HTTP_FB_ACCESS_TOKEN']
					fb_id = data['fb_id']
					g_id = -1
					try:
				        graph = GraphAPI(access_token)
				        profile = graph.get_object('me', fields='email')
				        fb_graph_id = profile['id']
				    except GraphAPIError as e:
				        return response('error', e)
				    if fb_id != fb_graph_id:
				    	return response("error", "facebook auth failed", ("error_type", "fb_error"))
				    return check_and_add_user(data,fb_id,g_id)	   		
				except:
					return response("error", "Incomplete data sent", ("error_type","Incomplete_data"))

			elif data['type'] == 'google':
				pass
			else:
				return response("error", "Invalid signup type")
		except:
			return response("error", "Invalid signup type")
	else:
		return response("error", "Not a post request")

