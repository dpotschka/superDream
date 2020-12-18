
from django.http import HttpResponseRedirect
from django.shortcuts import render
from ..models import User, PendingUser

from ..forms import LogOnForm
# Used to check if the userName is in the db
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.hashers import check_password

from util import make_secure_val


# DAVEE test , close the broswer and see if the cookie is deleted.
def logOn(request):

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = LogOnForm(request.POST)
        # check whether it's valid:
        if form.is_valid():

            # process the data in form.cleaned_data as required
            userName = form.cleaned_data['userName']
            password = form.cleaned_data['password']

            # See if the userName is in either PendingUser db
            # or User db.  A new user will be in PendingUser.
            whichDB = ''

            try:
                PendingUser.objects.get(pendingUserName = userName)
                whichDB = 'pending'
            except ObjectDoesNotExist:
                try:
                    User.objects.get(userName = userName)
                except ObjectDoesNotExist:
                    # Send errorMessage
                    return render(request, 'myDream/logOn.html',
                    {'form': form, 'errorMessage': 'You entered an invalid nickname.'})


# A new user will be in PendingUser.
            if whichDB == 'pending':
                userInfo = PendingUser.objects.values_list('pendingUserName','password',
                'email', 'created').filter(pendingUserName = userName)
                """
Here is what userInfo looks like, a tuple in a list.
<QuerySet [(u'bill', u'pbkdf2_sha256$30000$6FGO4mYDlJdQ$99lm/cor6XB5ltN8lGbp8ApfluXu+HSbXs02fWdrcKU=',
u'b@b.com', datetime.datetime(2016, 11, 19, 20, 28, 17, 890930, tzinfo=<UTC>))]>
                """
                correctPass = check_password(password, userInfo[0][1])

                if correctPass:
                    # Add the user info to the User db.
# CAUTION:  All fields must have a value if no default is given in models.py
# I now give default created=timezone.now() in models.py

                    theUser = User(userName = userName, email = userInfo[0][2],\
                        password = userInfo[0][1]) #, created = timezone.now() )
                    theUser.save()

# Set cookie and redirect to the main page, index.html.
                    user = User.objects.get(userName = userName)
                    userId = str(user.id)

# make_secure_val returns the 'userId|hash'.
                    cookie_val = make_secure_val(userId)
                    request.session['cookie_val'] = cookie_val

                    # Delete the user info from the PendingUser db.
                    user = PendingUser.objects.filter(pendingUserName = userName)
                    user.delete()

                    return HttpResponseRedirect('/myDream/books/')

                else:
                    return render(request, 'myDream/logOn.html',
                    {'form': form, 'errorMessage': 'You entered an invalid password'})

            else:  # An old user who is in the User db.

                userInfo = User.objects.values_list('userName','password',
                'email', 'created').filter(userName = userName)
                correctPass = check_password(password, userInfo[0][1])

                if correctPass:
# Set cookie and redirect to the main page, index.html
                    user = User.objects.get(userName = userName)
                    userId = str(user.id)

                    cookie_val = make_secure_val(userId)
                    request.session['cookie_val'] = cookie_val
                    return HttpResponseRedirect('/')

                else:
                    return render(request, 'myDream/logOn.html',
                    {'form': form, 'errorMessage': 'You entered an invalid password'})


    else: # GET the form.
        form = LogOnForm()
        return render(request, 'myDream/logOn.html',{'form': form})


"""
check_password(password, encoded)
It takes two arguments: the plain-text password to check, and the
full value of a user's password field in the database to check
against, and returns True if they match, False otherwise.

db queries
https://docs.djangoproject.com/en/1.10/topics/db/queries/

"""
