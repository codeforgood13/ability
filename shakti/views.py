# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from shakti.models import PersonalInfo, Qualification, Skills, Constraints, JobDescriptor
from shakti.models import Vision, Orthopedic, Hearing, Other
import random
import algo

def home(request):
	""" Render Home Page """
	return render_to_response('Ability.htm',context_instance=RequestContext(request))
	# HttpResponse("Home page comes here")

def personal(request):
	""" Category 1: Get personal details here"""
	if request.method == 'POST':
			post_req = request.POST
			print post_req
			person = PersonalInfo()
			person.name = post_req.get('name',None)
			person.dob = post_req.get('dob',None)
			print person.dob
			gen = post_req.get('gender',None)
			if gen == 'male':
				person.gender = "M"
			elif gen == 'female':
				person.gender = "F"
			person.location = post_req.get('location',None)
			person.email = post_req.get('email',None)
			mar_stat = post_req.get('maritial_status','NA')
			if mar_stat == "yes":
				person.maritial_status = "T"
			elif mar_stat == "no":
				person.maritial_status == "F"
			person.code = 'A'+str(random.randint(0000,9999))
			person.mobile_number=post_req.get('mobile_number',None)
			person.save()
			return redirect('/skills/'+str(person.id)+'/')
	return render_to_response('employee_form.htm',context_instance=RequestContext(request))


def skills(request,id):
	""" Get skill detials of an individual"""
	if request.method == 'POST':
		post_req = request.POST
		try:
			person = PersonalInfo.objects.get(pk=id)

		except Exception:
			return HttpResponse("Error in more_information , No such user exists")

		qualification_object = Qualification()
		qualification_object.uid = person

		skill_object = Skills()
		skill_object.uid = person

		
		skill_object.projects = post_req.get('projects',"")
		skill_object.computer_skills = post_req.get('computer_skills',"")
		skill_object.speciality = post_req.get('speciality',"")
		skill_object.save()
		print skill_object
		print post_req
		qualification_object.perc = post_req.get('perc',0)
		qualification_object.eduIndex= post_req.get('latest_degree',0)
		qualification_object.other_desc = post_req.get('other_descr'," ")
		qualification_object.save()
		return redirect('/more_information/'+id)

	else:
		# return a page to enter the data of skills
		return render_to_response('qualificationskills.html',context_instance=RequestContext(request))


def more_information(request,id):
	""" Information About The disability of  challenged person are got here via POST request"""
	if request.method == 'POST':
		post_req = request.POST
		try:
			person =  PersonalInfo.objects.get(pk=id)
		except Exception:
			return HttpResponse("Error in more_information , No such user exists")

		print request.POST
		if post_req.get('severity',None):
			vision_object = Vision()
			vision_object.uid = person
			if post_req.get('severity') == 1:
				vision_object.severity = 'NA'
			elif post_req.get('severity') == 2:
				vision_object.severity = 'B'
			elif post_req.get('severity') == 3:
				vision_object.severity = 'L'
			vision_object.save()

		if post_req.get('level',None):
			hearing_object = Hearing()
			hearing_object.uid = person
			if post_req.get('level') == 1 :
				hearing_object.level = 'C'
			else:
				hearing_object.level = 'P'
			hearing_object.save()
	
		if post_req.get('rleg_amputee') or  post_req.get('lhand_amputee') or post_req.get('rhand_amputee') or post_req.get('lleg_amputee'):
			orthopedic_object = Orthopedic()
			orthopedic_object.uid = person
			rleg_amputee = post_req.get('rleg_amputee',None)
			if rleg_amputee:
				orthopedic_object.rleg_amputee = 'Y'
			elif rleg_amputee:
				orthopedic_object.rleg_amputee = 'N'
			lleg_amputee = post_req.get("lleg_amputee",None)
			if lleg_amputee:
				orthopedic_object.lleg_amputee = 'Y'
			else:
				orthopedic_object.lleg_amputee = 'N'
			rhand_amputee =	post_req.get('rhand_amputee',None)
			if rhand_amputee:
				orthopedic_object.rhand_amputee = 'Y'
			else:
				orthopedic_object.rhand_amputee = 'N'

			lhand_amputee = post_req.get('lhand_amputee',None)
			if lhand_amputee:
				orthopedic_object.lhand_amputee = 'Y'
			else:	
				orthopedic_object.lhand_amputee = 'N'

			orthopedic_object.save()

		if post_req.get('other',None):
			other_object = Other()
			other_object.uid =  person
			other_object.other_description = post_req.get('other_description',None)
			other_object.save()
		return redirect('/constraints/'+id+'/')

	else:
		# return a page to enter the data of skills

		return render_to_response('disability.html',context_instance=RequestContext(request))



def constraints(request,id):
	""" Any special consideration for the physically challenged person """
	if request.method == 'POST' :
		post_req = request.POST
		try:
			person =  PersonalInfo.objects.get(pk=id)
		except Exception:
			return HttpResponse("Error in more_information , No such user exists")		
		post_req = request.POST
		constraints = Constraints()
		constraints.uid = person
		if post_req.get('night_shift',"No") == '1':
			constraints.night_shift = "Y"
		else:
			constraints.night_shift = "N"

		if post_req.get('relocated',"No") == '1':
			constraints.relocatable = "Y"
		else:
			constraints.relocatable = "N"

		if post_req.get('special_assistance','No') ==1:
			constraints.special_assistance = 'Y'
		else:
			constraints.special_assistance = 'N'	

		constraints.assistance_descr  = post_req.get("assistance_descr","No")
		constraints.save()		
		return redirect('/home/')

	else:
		return render_to_response('constraints.html',context_instance=RequestContext(request))


def JobInfoGetter(request):
	""" Get the requirements for the job """
	if request.method == 'POST':
		post_req = request.POST
		job = JobDescriptor()
		job.post = post_req.get('post',None)
		if post_req.get('location') == '1':
			job.location = 'B'
		elif post_req.get('location') == '2':
			job.location = 'K'
		elif post_req.get('location') == '3':
			job.location = 'M'
		elif post_req.get('location') =='4':
			job.location = 'G'
		job.qualification = post_req.get('quali')
		
		if post_req.get('o',None):
			job.who_can_o = 'Y'
		if post_req.get('b',None):
			job.who_can_b = 'Y'
		if post_req.get('h',None):
			job.who_can_h = 'Y'

		if post_req.get('time') == 1:
			job.night_shift = 'N'
		else:
			job.night_shift = 'Y'
		job.description = post_req.get('descr')
		job.save()

		rlist = algo.abilityEngine(post_req)
		return render_to_response('result.html',{'rlist':rlist},context_instance=RequestContext(request))
		
	return render_to_response('jobdescr.html',context_instance=RequestContext(request))