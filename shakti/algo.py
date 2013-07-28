from shakti.models import *
from operator import itemgetter as attr

def getObject(Category, profile):
	print profile
	print 'id', profile['id']
	try:
		return Category.objects.get(uid_id=profile['id'])
	except:
		return Category()

def getDict(obj):
	returnDict = {}
	if obj:
		for key, value in obj.__dict__.items():
			if key == 'id':
				returnDict['some'+key] = value
			else:
				returnDict[key] = value
	return returnDict

def mergeDicts(profile, *categories):

	for category in categories:
		profile.update(getDict(getObject(category, profile)))
	return profile

def abilityEngine(request):
	personalinfoTable = PersonalInfo.objects.all()

	database = []
	for person in personalinfoTable:
		profile = {}
		# Populate the personal details
		profile.update(getDict(person))
		profile["id"] = profile["someid"]

		profile.update(mergeDicts(profile, Skills, Qualification, Constraints, Orthopedic, Vision, Hearing, Other))
		database.append(profile)




	resultset = []
	tempexact = []
	tempnotexact = []
	if request.get('night_shift', 'N') == "Y":
		resultset= sorted(database,key=attr('night_shift'),reverse=True)
	else:
		resultset = database
	for person in resultset:
		if person['location'] == request.get('location',None):
			tempexact.append(person)
		else:
			tempnotexact.append(person)
	resultset=tempexact + sorted(tempnotexact,key=attr('relocatable'),reverse=True)
	tempexact = []
	tempnotexact = []
	for person in resultset:
		if request['quali'] <= person['eduIndex']:
			tempexact.append(person)
		else:
			tempnotexact.append(person)
	resultset = sorted(tempexact, key=attr('eduIndex')) + tempnotexact
	try:
		resultset = sorted(resultset,key=attr('doj'))
	except:
		pass
	for i in xrange(len(resultset)):
		resultset[i]['skillcount'] = 0
		for skill in [s.strip() for s in request['descr'].split(',')]:
			try:
				if skill in [r.strip() for r in resultset[i]['skills'].split(',')]:
					resultset[i]['skillcount'] += 1
			except:
				pass
	resultset = sorted(resultset,key=attr('skillcount'),reverse=True)
	tempexact = []
	tempnotexact = []
	for person in resultset:
		flag = 1
		try:
			if not (Orthopedic.objects.get(uid_id=person['id']) and request['o'] == 'Y'):
				flag = 0
		except:
			pass
		try:
			if not (Hearing.objects.get(uid_id=person['id']) and request['h'] == 'Y'):
				flag = 0
		except:
			pass
		try:
			if not (Vision.objects.get(uid_id=person['id']) and request['b'] == 'Y'):
				flag = 0
		except:
			pass
		if flag == 1:
			tempexact.append(person)
		else:
			tempnotexact.append(person)
	resultset = tempexact + tempnotexact
	return resultset
