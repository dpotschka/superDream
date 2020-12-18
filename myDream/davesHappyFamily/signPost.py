

from django.shortcuts import render

# The '..' means two directories up ie myFrog/davesHappFamily/forms.py
from ..forms import UserInfoForm
from ..models import User, PendingUser

# Used to check if the userName is in the db
from django.core.exceptions import ObjectDoesNotExist

# from davesHappyFamily, The '.' is the directory we are in ie davesHappyFamily
from .util import text_password

from django.core.mail import send_mail

from django.contrib.auth.hashers import make_password, is_password_usable



body =  """
Dear %s:

Your account has been approved.

Please Log On with your password and nickname.
You can change your password after you LogOn if you want to.

Your password is all lower case letters:  %s
Log On here:
https://www.theHyperDream.com/myDream/logOn/


Feel free to contact me if you have any questions.
dave@theHyperDream.com

Cheers,

   Dave




"""


from django.core.mail import EmailMessage
def signPost(request):

    """
    First we come here as a GET 'if request.method != POST' and render the blank
    form.  Then when the user submits the form we come here again and process
    the newGuy's info.  The form is at signUp.html via forms.py

    """
    if request.method == 'POST':

# create a form instance and populate it with data from the request:
        form = UserInfoForm(request.POST)
        # check whether it's valid:
        if form.is_valid():

            # process the data in form.cleaned_data as required
            userName = form.cleaned_data['userName']
            email = form.cleaned_data['email']

# See if the userName is already taken.
            nameTaken = False
            try:
                User.objects.get(userName = userName)
                nameTaken = True
            except ObjectDoesNotExist:
                try:
                    PendingUser.objects.get(pendingUserName = userName)
                    nameTaken = True
                except ObjectDoesNotExist:
                    nameTaken = False

            if nameTaken:
# Tell the user the nickname is already taken, please pick a different name.
                return render(request, 'myDream/signUp.html',
                    {'form': form, 'nameTakenMessage': 'That name is not\
                    available, please pick a different nickname.'})

# Create password, put the new users data in the pendingUser db,
# send verification email and redirect to thankyou/verification message.
            else:
                textPass = text_password()
                password = make_password(textPass, salt=None, hasher='default')
                passWorks = is_password_usable(password)

# Use check for the login handler.
#check = check_password(textPass, hashPassword)

# Put the users name in the pendingUser db.  You must remove there
# name from the pending db once they log on for the first time and add
# their name to the User db at that time as well.  If a person never
# verifies their email you must clean the PendingUser db every two weeks.
# Remove any entries more than 2 weeks old.

# CAUTION:  All fields must have a value if no default is given in models.py
# I now give default created=timezone.now() in models.py
                if passWorks:
                    newGuy = PendingUser(email = email, pendingUserName = userName,
                    password = password)
                    newGuy.save()

# Send a verification email, should be inside the 'if passWorks' block.
# Subject # Message # From Sender # To You and many more in a list.

                    email = EmailMessage(
        # Title of the email.
                        userName + ' You Are Super Super Cool',

        # What the I wrote.  Var from above.  Your account is approved.
                        body % (userName, textPass),

        # The email is from me.
                        "dave@theHyperDream.com",

        # The email is being sent to the client.
                        [email],

        # This header is for the user to reply.
                        headers = {'Reply-To': 'dave@theHyperDream.com'}
                    )
                    email.send()


                    """
                    send_mail(
                        userName + ' You Are Super Super Cool',
                        body % (userName, textPass),
                        'dave@thehyperdream.com',
                        [email],
                        fail_silently=False,
                            )
                    """

# Tell the user to check their email inbox for the verification email.
                    return render(request, 'myDream/signUpResults.html')

                    # This also works, using a handler.
                    #return HttpResponseRedirect(reverse('myDream:test'))

# If a GET, or any other method, happens we'll create a blank form.
# We come here first from the index.html when the user clicks on
# sign up.  This will also display errors automatically from django
# if 'form' is not valid above at line 49.
    else:
        form = UserInfoForm()
# This is outside the first 'if block' in case the form is not valid.
    return render(request, 'myDream/signUp.html', {'form': form})


# This works:
#url = 'myFrog:test'
#return HttpResponseRedirect(reverse(url))

# Does not work.  You must use the name of the url mapper like above.
# name='test'
#return HttpResponseRedirect(reverse('test/?userName=' + userName + '&email=' + email))
#return HttpResponseRedirect(reverse('test/'))

# See reverse below.


################ End signPost()



"""


# Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
# https://docs.djangoproject.com/en/1.10/ref/urlresolvers/
https://docs.djangoproject.com/en/1.10/intro/tutorial04/



Query the sqlite3 db:
https://docs.djangoproject.com/en/1.10/topics/db/queries/
https://docs.djangoproject.com/en/1.10/topics/db/sql/


########


password stuff

make_password(password, salt=None, hasher='default')
Creates a hashed password in the format used by this application
<algorithm>$<iterations>$<salt>$<hash>.

It takes one mandatory argument: the password in plain-text.
Optionally, you can provide a salt and a hashing algorithm to
use, if you don't want to use the defaults (first entry of
PASSWORD_HASHERS setting).


check_password(password, encoded)
It takes two arguments: the plain-text password to check, and the
full value of a user's password field in the database to check
against, and returns True if they match, False otherwise.

############### End password stuff


Different ways to get form data:
see this first:
https://docs.djangoproject.com/en/1.10/topics/forms/
https://docs.djangoproject.com/en/1.10/ref/forms/

http://stackoverflow.com/questions/4706255/how-to-get-value-from-form-field-in-django-framework


def contact(request):

# If the form has been submitted...
    if request.method == 'POST':

# A form bound to the POST data
        form = ContactForm(request.POST)
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            # ...

            print form.cleaned_data['my_form_field_name']

# Redirect after POST
            return HttpResponseRedirect('/thanks/')

    else:
        form = ContactForm() # An unbound form

    return render_to_response('contact.html', {
        'form': form,
    })


def my_view(request):

    if request.method == 'POST':
        print request.POST.get('my_field')

        form = MyForm(request.POST)

        print form['my_field'].value()
        print form.data['my_field']

        if form.is_valid():

            print form.cleaned_data['my_field']
            print form.instance.my_field

            form.save()
            print form.instance.id  # now this one can access id/pk


########### End Different ways to get form data

"""



