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
	('NA','N/A')
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
	""" Model for information of a person looking for a job"""
	code = models.CharField(max_length=10);
	name = models.CharField(max_length=40,blank=False,null=False,)
	dob = models.DateField(null=False,blank=False)
	gender = models.CharField(max_length=10, choices=CHOICES)
	location = models.TextField()
	email = models.EmailField(max_length=30, default='testuser@mail.com')
	mobile_num = models.CharField(max_length=15, default='+9129089998')
	maritial_status = models.CharField(max_length=10, choices=STATUS) 

class Tracker(models.Model):
	uid = models.ForeignKey('PersonalInfo')
	placed = models.CharField(max_length=10, choices=STATUS)
	details = models.CharField(max_length=10, default=None)
	doj = models.DateField(default=None)

class Skills(models.Model):
	uid = models.ForeignKey('PersonalInfo')
	projects = models.TextField()
	computer_skills = models.TextField()
	speciality = models.TextField()


class Qualification(models.Model):
	uid = models.ForeignKey('PersonalInfo')
	eduIndex = models.IntegerField(max_length=10)
	other_desc = models.TextField(default=None,blank=True)


class Constraints(models.Model):
	uid = models.ForeignKey('PersonalInfo')
	night_shift = models.CharField(max_length=10, choices=OPTION_CHOICES)
	relocatable = models.CharField(max_length=8, choices=OPTION_CHOICES)
	special_assistance = models.CharField(max_length=8, choices=OPTION_CHOICES)
	assistance_descr = models.CharField(max_length=200, default=" May need help")


class Orthopedic(models.Model):
	uid = models.ForeignKey('PersonalInfo')
	rleg_amputee = models.CharField(max_length=10, choices=OPTION_CHOICES)
	lleg_amputee = models.CharField(max_length=10, choices=OPTION_CHOICES)
	rhand_amputee = models.CharField(max_length=10, choices=OPTION_CHOICES)
	lhand_amputee = models.CharField(max_length=10, choices=OPTION_CHOICES)
	orthopedic_aid =  models.CharField(max_length=50)

class Vision(models.Model):
	uid = models.ForeignKey('PersonalInfo')	
	severity = models.CharField(max_length=10, choices=VISION_LEVELS)


class Hearing(models.Model):
	uid = models.ForeignKey('PersonalInfo')	
	hearing_aid = models.CharField(max_length=5, choices=OPTION_CHOICES,default='N')
	level = models.CharField(max_length=10, choices=HEARING_LEVELS)


class Other(models.Model):
	uid = models.ForeignKey('PersonalInfo')
	other_description = models.TextField()

class JobDescriptor(models.Model):
	post = models.CharField(max_length=1000)
	location = models.CharField(max_length=20, choices=CITIES)
	qualification = models.TextField(null=False)
	who_can_o = models.CharField(max_length=5, choices=OPTION_CHOICES)
	who_can_b =  models.CharField(max_length=5, choices=OPTION_CHOICES)
	who_can_h =  models.CharField(max_length=5, choices=OPTION_CHOICES)
	night_shift = models.CharField(max_length=5, choices=OPTION_CHOICES)
	skills_required = models.TextField()