from dashboard.feeds import *
from dashboard.models import *
from dashboard.views import *
from django.conf.urls import *
import rcos.views
import observatory.urls
import settings

urlpatterns = patterns('',
    
    # RCOS views
    (r'^donor/$', rcos.views.donor),
    (r'^students/$', rcos.views.students),
    (r'^courses/$', rcos.views.courses),
    (r'^talks/$', rcos.views.talks),
    (r'^programming-competition/$', rcos.views.progcomp),
    (r'^achievements/$', rcos.views.achievements),
    (r'^urp-application/$', rcos.views.urpapplication),
    (r'^links-and-contacts/$', rcos.views.linksandcontacts),
    (r'^talk-sign-up/$', rcos.views.talksignup),
    (r'^irc/$', rcos.views.irc),
    (r'^faq/$', rcos.views.faq),
    (r'^calendar/$', rcos.views.calendar),
    (r'^howtojoin/$', rcos.views.howtojoin),
    (r'^past-projects/$', rcos.views.past_projects),
    (r'^$', rcos.views.index),
    
    (r'^', include(observatory.urls)),
)
