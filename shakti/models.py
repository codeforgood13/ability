from django.db import models

CHOICES = (('M','male'),
	('F','female'),
	)

STATUS = (('T','True'),
		('F','False'),
		)

VISION_LEVELS = (
	('B','Blind'),
	('L','Low Vision'),
	)

OPTION_CHOICES = (
	('Y','Yes'),
	('N','No'),
	)

HEARING_LEVELS = (
	('P','Partial'),
	('C','Complete'),
	)

CITIES = (('B','Bangalore'),
	('K','Kolkatta'),
	('M','Bombay'),
	('G','Gandhi Nagar'),
	)

CATEGORIES = (('O','Orthopedic'),
	('V','Visionary'),
	('H','Hearing'),
	)

LATEST = (
	('T','XII'),
	('D','Diploma'),
	('UG','U.G'),
	('PG','P.G'),
	('O','Others'),
	)


# Create your models here.
class PersonalInfo(models.Model):
	code = models.CharField(max_length=10);
	name = models.CharField(max_length=40,blank=False,null=False,)
	dob = models.DateField(null=False,blank=False)
	gender = models.CharField(max_length=5, choices=CHOICES)
	address = models.TextField()
	email = models.EmailField(max_length=30, default='testuser@mail.com')
	mobile_num = models.CharField(max_length=15, default='+9129089998')
	maritial_status = models.CharField(max_length=10, choices=STATUS) 

class Tracker(models.Model):
	uid = models.ForeignKey('PersonalInfo')
	placed = models.CharField(max_length=10, choices=STATUS)
	details = models.CharField(max_length=10, default=None)
	doj = models.DateField(default=None)

class Skills(models.Model):
	projects = models.TextField()
	computer_skills = models.TextField()
	speciality = models.TextField()


class Qualification(models.Model):
	tenth_perc = models.CharField(max_length=10)
	latest_degree = models.CharField(max_length=10, choices=LATEST)
	other_desc = models.TextField(default=None,blank=True)


class Constraints(models.Model):
	uid = models.ForeignKey('PersonalInfo')
	night_shift = models.CharField(max_length=10, choices=OPTION_CHOICES)
	relocatable = models.CharField(max_length=8, choices=OPTION_CHOICES)
	special_assistance = models.CharField(max_length=8, choices=OPTION_CHOICES)
	assistance_descr = models.CharField(max_length=200, default=None)


class Orthopedic(models.Model):
	uid = models.ForeignKey('PersonalInfo')
	rleg_amputee = models.CharField(max_length=10, choices=OPTION_CHOICES)
	lleg_amputee = models.CharField(max_length=10, choices=OPTION_CHOICES)
	rhand_amputee = models.CharField(max_length=10, choices=OPTION_CHOICES)
	lhand_amputee = models.CharField(max_length=10, choices=OPTION_CHOICES)

class Vision(models.Model):
	uid = models.ForeignKey('PersonalInfo')	
	severity = models.CharField(max_length=10, choices=VISION_LEVELS)


class Hearing(models.Model):
	uid = models.ForeignKey('PersonalInfo')	
	hearing_aid = models.CharField(max_length=5, choices=OPTION_CHOICES)
	level = models.CharField(max_length=10, choices=HEARING_LEVELS)

class Other(models.Model):
	uid = models.ForeignKey('PersonalInfo')
	other_description = models.TextField()

class JobDescriptor(models.Model):
	post = models.CharField(max_length=10)
	location = models.CharField(max_length=20, choices=CITIES)
	qualification = models.TextField(null=False)
	who_can = models.TextField(max_length=20, choices=CATEGORIES)
	night_shift = models.CharField(max_length=5, choices=OPTION_CHOICES)
	skills_required = models.TextField()


