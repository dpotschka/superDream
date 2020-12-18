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


# I am temporarily sending my art traffic from paw to my art page on webflow.  Dec 29/18
# So I can rebuild my art page on paw, see handler artForSale2 below this one.

"""
def artForSale(request):

    return HttpResponseRedirect('https://david-potschkas-five-star-project.webflow.io/thegoods#artistic')
"""
# This is for updating, there is no button on my web site point to it.
def artForSale2(request):

    return render(request, 'myDream/art2.html')

"""
https://www.thehyperdream.com/myDream/artForSale2/
"""

def artForSale(request):

    return render(request, 'myDream/art2.html')



"""
    # cookie = 'userId|hash'
    try:
        cookie_val = request.session['cookie_val']
        valid_cookie = check_secure_val(cookie_val)

        if valid_cookie:
# Fill in their email for them on the purchase form.
            userId = cookie_val.split('|')[0]
            user = User.objects.get(id = userId)
            email = user.email
            return render(request, 'myDream/art.html', {'email':email})
        else:
            return HttpResponseRedirect('logOn/')

    except:
        return HttpResponseRedirect('logOn/')

    """



def baby(request):

    """ Redirect for ad miriicle baby"""
    return HttpResponseRedirect('http://f8392gwmtaj6cu0jx9jkbbuz2n.hop.clickbank.net/')



def books(request):

    return render(request, 'myDream/books.html')
    """
    # cookie = 'userId|hash'
    try:
        cookie_val = request.session['cookie_val']
        valid_cookie = check_secure_val(cookie_val)
        if valid_cookie:
            return render(request, 'myDream/books.html')
        else:
            return HttpResponseRedirect('logOn/')

    except:
        return HttpResponseRedirect('logOn/')

    """



def changePassword(request):

    if request.method == 'POST':
        form = ChangePasswordForm(request.POST)

        if form.is_valid():

            # process the data in form.cleaned_data as required
            email = form.cleaned_data['email']
            oldPassword = form.cleaned_data['oldPassword']
            newPassword = form.cleaned_data['newPassword']
            newPasswordAgain = form.cleaned_data['newPasswordAgain']

            """
Get the users password associated with their email and check it against
the oldPassword.  Make sure their new password is 8 chars long and it
matches their newPasswordAgain.  Hash their password and update the db.

            """
            try:
                user = User.objects.get(email = email)
            except ObjectDoesNotExist:
                return render(request, 'myDream/changePassword.html',\
                {'form': form, 'errorMessage': "You entered an invalid email"})

            correctPass = check_password(oldPassword, user.password)

            if correctPass:
# See if the new passwords are at least 8 chars long and the same.
# Password for Dave at gmail is odzcfyge
                newPassValid = valid_pass(newPassword)
                newPassAgainValid = valid_pass(newPasswordAgain)

                if newPassValid and newPassAgainValid:

                    if newPassword == newPasswordAgain:
                        user.password = make_password(newPassword, salt=None, hasher='default')
                        user.save()
                        return render(request, 'myDream/changePasswordResults.html')
                    else:
                        return render(request, 'myDream/changePassword.html',\
                        {'form': form, 'errorMessage': "Error:  You did not type the same new password twice."})

                else:
                    return render(request, 'myDream/changePassword.html',\
                    {'form': form, 'errorMessage': "Error:  Your new password must be longer than 7 characters and less than 31."})

            else:
                return render(request, 'myDream/changePassword.html',\
                {'form': form, 'errorMessage': "You entered an invalid Old Password"})




    else:  # GET the form
        form = ChangePasswordForm()

# This is outside the first 'if block' in case the form is not valid.
    return render(request, 'myDream/changePassword.html', {'form': form})


################# End changePassword




from django.core.mail import EmailMessage
from django.template import Context
from django.template.loader import get_template

from sales.models import ClientDB
# client_email, first_name, last_name, created


# add to your views

# YOU SHOULD BE CATCHING THESE emails IN A DATA BASE...DONE.  Now exclude the emails which are noreply@...DONE.

def contact(request):

# this is where you found this code:
# https://hellowebapp.com/news/tutorial-setting-up-a-contact-form-with-django/

    form_class = ContactForm

    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get(
                'contact_name'
            , '')
            contact_email = request.POST.get(
                'contact_email'
            , '')
            form_content = request.POST.get('content', '')

            #pledgeAmount = request.POST.get('pledgeAmount', '')


            # Email the profile with the
            # contact information
            template = get_template('myDream/contact_template.txt')
            context = Context({
                'contact_name': contact_name,
                'contact_email': contact_email,
                'form_content': form_content,

            })
            content = template.render(context)


            email = EmailMessage(
# Title of the email.
                "Dave, mail from a client!",

# What the client wrote.  Var from above.
                content,

# The email is from me.
                'dave@thehyperdream.com',
                #"https://www.thehyperdream.com" +'',

# The email from the client is being sent to me.
                ['dave@thehyperdream.com'],

# This header is for when I click on reply at my hyperdream account, I reply to the
# clients contact_email.
                headers = {'Reply-To': contact_email }
            )
            email.send()

# Put the users email data into the clientDB.
            """
            client = ClientDB(client_email = contact_email, first_name = contact_name,\
            last_name = contact_name)
            client.save()
            """
# Only save the email in the ClientDB if their email is not already in there.
            try:
                ClientDB.objects.get(client_email = contact_email)
            except ObjectDoesNotExist:
                """
                To get rid of the noreply@... put an if statement around the next block of code.
                If client_email does not start with "noreply@" then do the next block.

                ^	Match start of string	^Dear
                eg r'^Dear' will match any string starting with the word Dear.

                To stop the robots, what is 6*3?
                if stopRobot=="18":

                """
                #if not (r'^noreply@' == contact_email[0:7]):
                if not ('noreply' in contact_email):
                    if not ('no-reply' in contact_email):
                        client = ClientDB(client_email = contact_email, first_name = contact_name,\
                        last_name = contact_name)
                        client.save()

                """
                client = ClientDB(client_email = contact_email, first_name = contact_name,\
                last_name = contact_name)
                client.save()
                """


            return render(request, 'myDream/clientSentEmailSuccess.html')


    return render(request, 'myDream/contact.html', {'form': form_class,})




###################### End contact


# This downloads my complete list of dvds I have for sale.  For clients to buy.
def davesList(requst):

    with open("/home/timetable/superDream/myDream/static/myDream/davesList.docx", "rb") as davesList:
        data = davesList.read()
    response = HttpResponse(data,content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
    response['Content-Disposition'] = 'attachment; filename=davesList.docx'
    return response




###################### End davesList


class FiveSeconds(generic.DetailView):
    """ Gives the user theinstructins for building a web page in 5 seconds."""
    #model = Question

    template_name = 'myDream/fiveSecondWebPage.html'

    #context_object_name = 'build'

    def get_object(self):
        pass


# Forgot nickname or password handler.

body =  """
Dear %s:

Here is the information you requested.

Your nickname is %s
Your new password is %s
Your password is all lower case letters.

Please Log On with your new password and nickname.
You can change your password after you LogOn if you like.

Feel free to contact me if you have any questions.
dave@theHyperDream.com

Cheers,

   Dave

https://www.theHyperDream.com


"""



def forgot(request):
    """ Send the user their nickname and a new password if they forgot either."""
    if request.method == 'POST':
        form = ForgotForm(request.POST)

        if form.is_valid():

            # process the data in form.cleaned_data as required
            email = form.cleaned_data['email']

# Get them a new password and update the db.
            textPass = text_password()
            password = make_password(textPass, salt=None, hasher='default')
            passWorks = is_password_usable(password)

            if passWorks:
                """
If you must pick up multiple vars from a db you can do it this way so you
don't get an exception thrown, pick up one at a time.
Instead of worrying about getting an exception from this:
                #user = User.objects.get(email = email)
                # You can do it this way:
 go  = Content.objects.filter(name="baby").first()
 Now go variable could be either the object you want or None
              """
                try:
                    user = User.objects.get(email = email)
                except ObjectDoesNotExist:
                    return render(request, 'myDream/forgot.html',\
                    {'form': form, 'errorMessage': "You entered an invalid email"})

                user.password = password
                user.save()
                """
                User.objects.filter(email = email).update(password = password)
Just a fair warning... if you use the update method like this then any
signals attached to that model or other "code stuff" won't run against the objects.
So You might want to use the old 'get' and 'save' functions one after the other.
                """

# Get thier nickname.
                nickname = user.userName

# Send them an email.
# Send a verification email, should be inside the 'if passWorks' block.
# Subject # Message # From Sender # To You and many more in a list.
                send_mail(
                    nickname + ' Here is the info you requested',
                    body % (email, nickname, textPass),
                    'dave@theHyperDream.com',
                    [email],
                    fail_silently=False,
                        )

# Tell the user to check their email inbox for the verification email.
                return render(request, 'myDream/forgotResults.html')

    else:  # GET the form
        form = ForgotForm()

# This is outside the first 'if block' in case the form is not valid.
    return render(request, 'myDream/forgot.html', {'form': form})


##################### forgot




def guitarVideos(request):

    return render(request, 'myDream/guitarVideos.html')


def logOut(request):
    del(request.session['cookie_val'])
    return HttpResponseRedirect('/')


def paymentReceived(request):

    return render(request, 'myDream/paymentReceived.html')

    """
    # cookie = 'userId|hash'
    cookie_val = request.session['cookie_val']
    userId = cookie_val.split('|')[0]

    user = User.objects.get(id = userId)
    email = user.email

    return render(request, 'myDream/paymentReceived.html', {'email': email})
    """


# I had to hard wire the path and the filename to get this to work.
# I also had to put the word 'request' in as an arg.
# WARNING: You should be using a form in the html file for security.

#path = "https://www.pythonanywhere.com/user/timetable/files/home/timetable/superDream/myDream/static/myDream"
#filename = "risk-analysis.xlsx"

# The path isn't working tried these so far:

# "/home/timetable/superDream/myDream/static/myDream/risk-analysis.xlsx"
# "home/timetable/superDream/myDream/static/myDream/risk-analysis.xlsx"
# "/myDream/static/myDream/risk-analysis.xlsx"
# "/myDream/static/myDream/"
# "home/timetable/superDream/myDream/static/myDream/"
# "home/timetable/superDream/myDream/static/myDream/"
# "/home/timetable/superDream/myDream/static/myDream/"
# "/home/timetable/superDream/myDream/static/myDream"
# "/user/timetable/files/home/timetable/superDream/myDream/static/myDream"
# "https://www.pythonanywhere.com/user/timetable/files/home/timetable/superDream/myDream/static/myDream"

# def sendExcel(path="/home/timetable/superDream", filename="risk-analysis.xlsx"):
#    with open(path, "rb") as excel:

def sendExcel(request):

    with open("/home/timetable/superDream/myDream/static/myDream/risk-analysis.xlsx", "rb") as excel:
        data = excel.read()
    response = HttpResponse(data,content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=myDreamStockMarketPortfolio.xlsx'
    return response


# response['Content-Disposition'] = 'attachment; filename=myDreamStockMarketPortfolio.xlsx'
#response['Content-Disposition'] = 'attachment; filename=%s' % filename

# response = HttpResponse(data,content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
# response = HttpResponse(content_type='application/vnd.ms-excel')


# I got help from this one from here:
# https://stackoverflow.com/questions/12881294/django-create-a-zip-of-multiple-files-and-make-it-downloadable
def sendTrades(request):

    with open("/home/timetable/superDream/myDream/static/myDream/screenShotOfTradesMade1.zip", "rb") as zTrades:
        data = zTrades.read()
    response = HttpResponse(data, content_type = "application/x-zip-compressed")
    response['Content-Disposition'] = 'attachment; filename=screenShotOfTradesMade1.zip'
    return response


def sendTrades2(request):

    with open("/home/timetable/superDream/myDream/static/myDream/screenShotOfTradesMade2.zip", "rb") as zTrades:
        data = zTrades.read()
    response = HttpResponse(data, content_type = "application/x-zip-compressed")
    response['Content-Disposition'] = 'attachment; filename=screenShotOfTradesMade2.zip'
    return response



def sendStockMarketBook(request):

    with open("/home/timetable/superDream/myDream/static/myDream/stockMarketSolution_2017pdf2.pdf", "rb") as stockBook:
        data = stockBook.read()
    response = HttpResponse(data, content_type = "application/pdf")
    response['Content-Disposition'] = 'attachment; filename=stockMarketSolution_2017pdf2.pdf'
    return response



def stockMarketPortfolio(request):

    return render(request, 'myDream/stockMarketPortfolio.html')



def survives(request):
    """
    Render the survives page and capture the clients email
    into the ClientDB.
    """

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SurvivesForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            email = form.cleaned_data['email']

            # Put the email address into the ClientDB
            client = ClientDB(client_email = email, first_name = 'survives', last_name = 'survives')
            client.save()
            form = SurvivesForm()  # Clears the form.
            #return http.HttpResponseRedirect('')

            thanks = """Thank You For Your Email Address.  I will let you know if I <br>
            find anymore cool products or information!<br><br>

            Cheers,<br><br>

            Dave
            """
            return render(request, 'myDream/survives.html', {'form': form, 'thanks': thanks})

    else:
        form = SurvivesForm()

    return render(request, 'myDream/survives.html', {'form': form})



def vehicle(request):

    """ Redirect for ad cats"""
    return HttpResponseRedirect('http://8fd01ctn32m8hxarukj2p7uu61.hop.clickbank.net/')


def cats(request):

    """ Redirect for ad vehicle"""
    return HttpResponseRedirect('http://8a4acg-i-amdfz62qnq1w95oa5.hop.clickbank.net/')

def gout(request):

    """ Redirect for ad gout"""
    return HttpResponseRedirect('http://potschka.goutcode.hop.clickbank.net/?rd=v3')


def horse(request):

    """ Redirect for ad horse"""
    return HttpResponseRedirect('http://638a7g-gwargjq9mj4mculgtxu.hop.clickbank.net/')

def dunk(request):

    """ Redirect for ad dunk"""
    return HttpResponseRedirect('http://8b91fnsftxo9hwe-e4v4pdrbzp.hop.clickbank.net/')



def money(request):

    """ Redirect for ad money"""
    return HttpResponseRedirect('http://c41c8mzix7walkdbgqhb5kekdx.hop.clickbank.net/')


def phone(request):

    return render(request, 'myDream/phone.html')


