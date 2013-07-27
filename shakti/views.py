# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from shakti.models import PersonalInfo
import random

def home(request):
	""" Render Home Page """
	return render_to_response('index.html',context_instance=RequestContext(request))
	# HttpResponse("Home page comes here")

def personal(request):
	if request.method == 'POST':
			post_req = request.POST
			person = PersonalInfo()
			person.name = post_req.get('name',None)
			person.dob = post_req.get('dob',None)
			person.gender = post_req.get('gender',None)
			person.address = post_req.get('address',None)
			person.email = post_req.get('email',None)
			person.maritial_status = post_req('maritial_status','NA')
			person.code = 'A'+str(random.randint(0000,9999))
			person.save()
			return HttpResponse("Personal Details",)
	return redirect('/home')

def more_information(request,id):
	if request.method == 'POST':
		post_req = request.POST
		try:
			person = person.objects.get(pk=id)
		except Exception:
			return HttpResponse("Error in more_information , No such user exists")
		
		return redirect('/home')

	else:
		return redirect('/home')

def skills(request,id):
	if request.method == 'POST':
		post_req = request.POST
		try:
			person = person.objects.get(pk=id)
		except Exception:
			return HttpResponse("Error in more_information , No such user exists")

		return redirect('/more_information/'+id)

	else:
		return HttpResponse("Please send a post request")


