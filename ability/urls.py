from django.conf.urls import patterns, include, url
from shakti.models import *
# from shakti.models import PersonalInfo
# from shakti.models import Skills
from shakti import views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
# admin.site.register(PersonalInfo)
# admin.site.register(Constraints)


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ability.views.home', name='home'),
    # url(r'^ability/', include('ability.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^home/',views.home,name='home' ),
    url(r'^personal/', views.personal,name='submit'),
	url(r'^skills/(?P<id>\d+)/', views.skills,name='skills' ),    
    url(r'^more_information/(?P<id>\d+)/',views.more_information,name='more_info'),
    url(r'^constraints/(?P<id>\d+)/',views.constraints,name='constraints'),
    url(r'^job_descr/',views.JobInfoGetter,name='description')
    # url(r'^result/',views.)

)
