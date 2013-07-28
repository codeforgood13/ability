from django.contrib import admin
from shakti.models import Constraints,Skills,Qualification,PersonalInfo
from shakti.models import Orthopedic,Vision,Hearing,Other,JobDescriptor

admin.site.register(Constraints)
admin.site.register(Skills)
admin.site.register(Qualification)
admin.site.register(PersonalInfo)
admin.site.register(Orthopedic)
admin.site.register(Vision)
admin.site.register(Hearing)
admin.site.register(Other)
admin.site.register(JobDescriptor)


