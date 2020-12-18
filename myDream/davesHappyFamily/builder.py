from django.views import generic
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse

# Used to send an excel file to a user, see function def sendExcel
from django.conf import settings
# from django.http import HttpResponse   this is above

# Used to check if the email is in the db
from django.core.exceptions import ObjectDoesNotExist
from ..models import User

from sales.models import ClientDB

from ..forms import ChangePasswordForm, ForgotForm, ContactForm, SurvivesForm
# from davesHappyFamily, The '.' is the directory we are in ie davesHappyFamily
from util import text_password, valid_pass, check_secure_val

from django.core.mail import send_mail
from django.contrib.auth.hashers import make_password, is_password_usable,\
                                        check_password

from ..popup import popup_forms
#from superDream import .popup
#from ..popup import popup_forms

# I PUT THESE HANDLERS in alphabetical order.





#  This is scrap. not building for clients on paw.  But leave it in here or
# your whole website will crash.

"""
def davesBuilder(request):

    return render(request, 'myDream/davesBuilderFront.html')
"""

# Don't confuse this with the above, it is a completely seperate branch, note the path.
# Not using this landing page mobirise bootstrap it is scrap.

"""
def webSiteBuilder(request):

#https://www.pythonanywhere.com/user/timetable/files/home/timetable/superDream/myDream/static/webSiteBuilder/index.html


# I shall dump all the webSiteBuilder files into the template/webSiteBuilder Directory.
    return render(request, 'myDream/webSiteBuilder/index.html')

#return render(request, 'myDream/static/webSiteBuilder/index.html')

"""



# So FOR MY GOOGLE AD the client clicks on theHyperDream.com/myDream/websitebuilder
# and this redirects them to https://david-potschkas-five-star-project.webflow.io/

def webSiteBuilder(request):

    return HttpResponseRedirect('https://thehyperdream.webflow.io')




