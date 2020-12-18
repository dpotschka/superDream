from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

from django.utils import timezone
from django.views import generic

from .models import User, PendingUser
from davesHappyFamily.util import check_secure_val

# Hardwire the logo with this:
#<a href="http://www.thehyperdream.com/"><img id="logoNet" height="15%" width="15%" src="/static/myDream/webImages/buttons/logoNet/hyperDreamLogo1.jpg" onmouseover="getid(this);" /></a>

myName = "https://www.thehyperdream.com/"

# Create your views here.

# Using generic views from Lesson 4 at:
# https://docs.djangoproject.com/en/1.10/intro/tutorial04/
# Next, we're going to remove our old index, detail, and results
# views and use Django's generic views instead.

# I put most of the documentation from the tutorial after these
# class definitions (with corrections I might add).  READ IT OFTEN.
# Basically Django can take a class definition and a db model
# and fill in your template.html automatically with "generic views".

# It automatically runs the get_queryset() within a class
# declaration using the as_view() imported
# "from django.views import generic" (above) via the the url mapper at:
# /superFrog/myFrog/urls.py



# Using to test stuff.

class TestView(generic.DetailView):
    #model = User
    template_name = 'myDream/test.html'

# If you want to over ride that pk slug error for a DetailView
# you need this one
    def get_object(self):
        pass
        #return get_object_or_404(User, pk=request.session['


######################## End class TestView




class IndexView(generic.ListView):
    """ Displays the index page, my main front page! """

    """ context_object_name, template_name and get_queryset() are all
    django dependant.  They all work together to pass info to the
    index.html
    """

# Use the  context_object_name 'myVars' to pass the dict/db/object
# returned from the get_queryset() to index.html.  'myVars' is in index.html
    context_object_name = 'myVars'

# This is found at /myDream/templates/myDream/index.html
# template_name is django dependant.
    template_name = 'myDream/index.html'


# You need this or django has a spazz, it wants a db or some kind of object
# for a generic ListView.  This is called over riding the get_queryset.
# This will be automatically run when the url mapper comes here.  Its
# return is sent to the template via context_object_name = 'myVars'
# above.  'myVars' is the object in the index.html file which holds
# all information returned from this function get_queryset.
# Access the information in the index.html file like this eg 'myVars.go'
# The name of the dict being returned from get_queryset could be called
# anything, django is smart, it knows.

# Can't pass a loader and can't pass stuff into a loader either.  fuck
#"{% url 'myFrog:fiveSeconds' %}"

    def get_queryset(self):

        cookie_val = self.request.session.get('cookie_val')
        valid_cookie = check_secure_val(cookie_val)

        myVars = {}


# I am not using any cookies at this time Oct 21/19


        if valid_cookie:

            userId = cookie_val.split('|')[0]
            user = User.objects.get(id = userId)

            myVars['thanks'] = 'Hello '
            myVars['user'] = user.userName + '!  <br><br>'

            myVars['logPath'] = myName + "myDream/logOut/"
            logOutButton = '<img id="logOut" height="50" width="15%" src="/static/myDream/webImages/buttons/logOut/logOut1.jpg" onmouseover="getid(this);" />'
            myVars['logWords'] = logOutButton

            myVars['changePasswordPath'] = myName + "myDream/changePassword/"
            changePasswordButton = '<img id="password" height="50" width="15%" src="/static/myDream/webImages/buttons/password/password1.jpg" onmouseover="getid(this);" /></a>'
            myVars['changePasswordWords'] = changePasswordButton

            """
            myVars['yourProfilePath'] = myName + "myDream/yourProfile/"
            yourProfileButton = '<img id="yourProfile" height="50" width="15%" src="/static/myDream/webImages/buttons/yourProfile/yourProfile1.jpg" onmouseover="getid(this);" />'
            myVars['yourProfileWords'] = yourProfileButton
            """

        else:  # Not logged in or invalid cookie/session.

            myVars['logPath'] = myName + "myDream/logOn/"
            logOnButton = '<img id="logOn" height="50" width="15%" src="/static/myDream/webImages/buttons/logOn/logOn1.jpg" onmouseover="getid(this);" />'
            myVars['logWords'] = logOnButton

            myVars['signUpPath'] = myName + "myDream/signPost/"
            signUpButton = '<img id="signUp" height="50" width="15%" src="/static/myDream/webImages/buttons/signUp/signUp1.jpg" onmouseover="getid(this);" />'
            myVars['signUpWords'] = signUpButton

            myVars['logOnMan'] = '"Sign Up" so you can read the book and see all the art work.  No credit card required!  <br><br>'


        myVars['messagePath'] = myName + "myDream/message/"
        message = '<img id="message" height="15%" width="15%" src="/static/myDream/webImages/buttons/message/message1.jpg" onmouseover="getid(this);" />'
        myVars['messageWords'] = message

        myVars['fiveSecondsPath'] = myName + "myDream/fiveSeconds"
        quick = '<img id="quick" height="15%" width="15%" src="/static/myDream/webImages/buttons/quick/quick1.jpg" onmouseover="getid(this);" />'
        myVars['fiveSecondsWords'] = quick

        myVars['survivesPath'] = myName + "myDream/survives/"
        #guitarVideosButton = '<img id="guitarVideos" src="/static/myDream/webImages/buttons/guitarVideos/dgv1.jpg" onmouseover="getid(this);" />'
        #survivesButton = '<img id="survives" height="300" width="250" src="/static/myDream/adImages/survives/adLink.jpg" />'
        #myVars['survivesWords'] = survivesButton
        myVars['survivesWords'] = "Free Stuff"

# ******** Start here for my current buttons.

        '''
        myVars['logoPicPath'] = 'https://thehyperdream.webflow.io/thegoods#team'
        '''
        logoPicButton = '<img id="logoPic" style="margin-bottom:2%;" height="68px" width="68px" src="/static/myDream/webImages/LogoF240x240.png" />'
        myVars['logoPicWords'] = logoPicButton

        '''
        myVars['newLogoWordsPath'] = 'https://thehyperdream.webflow.io/thegoods#team'
        '''
        newLogoWordsButton = '<img id="newLogoWords" height="100px" width="100px" src="/static/myDream/webImages/words.png" />'
        #newLogoWordsButton = '<img id="newLogoWords" style="margin-left:20px; margin-top:20px" height="150px" width="150px" src="/static/myDream/theArt/words.png" />'
        myVars['newLogoWords'] = newLogoWordsButton

        '''
        myVars['lovePath'] = 'https://thehyperdream.webflow.io/thegoods#team'
        '''
        loveButton = '<img id="love" height="100px" width="100px" src="/static/myDream/webImages/love2F.png" />'
        myVars['love'] = loveButton

        myVars['artForSalePath'] = myName + "myDream/artForSale/"
        #artForSaleButton = '<img id="artForSale" src="/static/myDream/webImages/buttons/artForSale/artForSale1.jpg" onmouseover="getid(this);" />'
        artForSaleButton = '<img id="artForSale" height="25px" width="141px" src="/static/myDream/webImages/buttons/artForSale/artForSale1.png" onmouseover="getid(this);" />'
        myVars['artForSaleWords'] = artForSaleButton

        myVars['guitarVideosPath'] = myName + "myDream/guitarVideos/"
        #guitarVideosButton = '<img id="guitarVideos" src="/static/myDream/webImages/buttons/guitarVideos/dgv1.jpg" onmouseover="getid(this);" />'
        guitarVideosButton = '<img id="guitarVideos" height="25px" width="141px" src="/static/myDream/webImages/buttons/guitarVideos/dgv1.png" onmouseover="getid(this);" />'
        myVars['guitarVideosWords'] = guitarVideosButton

        myVars['booksPath'] = myName + "myDream/books/"
        #booksButton = '<img id="books" src="/static/myDream/webImages/buttons/books/books1.jpg" onmouseover="getid(this);" />'
        booksButton = '<img id="books" height="25px" width="141px" src="/static/myDream/webImages/buttons/books/books1.png" onmouseover="getid(this);" />'
        myVars['booksWords'] = booksButton

        myVars['contactPath'] = myName + "myDream/contact/"
        #contact = '<img id="contact" src="/static/myDream/webImages/buttons/contact/contact1.jpg" onmouseover="getid(this);" />'
        contact = '<img id="contact" height="25px" width="141px" src="/static/myDream/webImages/buttons/contact/contact1.png" onmouseover="getid(this);" />'
        myVars['contactWords'] = contact

        myVars['contactPath2'] = myName + "myDream/contact/"
        #contact = '<img id="contact2" src="/static/myDream/webImages/buttons/contact/contact1.jpg" onmouseover="getid(this);" />'
        contact = '<img id="contact2" height="25px" width="141px" src="/static/myDream/webImages/buttons/contact/contact1.png" onmouseover="getid(this);" />'
        myVars['contactWords2'] = contact

        myVars['stockMarketPath'] = myName + "myDream/stockMarketPortfolio/"
        stocks = '<img id="stocks" height="25px" width="141px" src="/static/myDream/webImages/buttons/stocks/stocks1.png" onmouseover="getid(this);" />'
        myVars['stockMarketWords'] = stocks

        '''
        myVars['builderPath'] = "https://thehyperdream.webflow.io/"
        builder = '<img id="builder" height="25px" width="141px" src="/static/myDream/webImages/buttons/builder1.png" onmouseover="getid(this);" />'
        myVars['builderWords'] = builder
        '''

        myVars['thdPath'] = "https://www.theHyperDream.com/"
        thd = '<img id="thd" height="25px" width="141px" src="/static/myDream/webImages/buttons/thd1.png" onmouseover="getid(this);" />'
        myVars['thdWords'] = thd

        '''
        myVars['theFrogPath'] = "http://www.whatdoesthefroggot.appspot.com/"
        theFrog = '<img id="theFrog" height="25px" width="141px" src="/static/myDream/webImages/buttons/theFrog/theFrog1.png" onmouseover="getid(this);" />'
        myVars['theFrogWords'] = theFrog
        '''

        return myVars



########################## End class IndexView




class Message(generic.DetailView):

    #model =
    template_name = 'myDream/message.html'

    context_object_name = 'myVars'

    myVars = {}

    def get_object(self):
        pass


class YourProfile(generic.DetailView):

    #model =
    template_name = 'myDream/yourProfile.html'

    context_object_name = 'myVars'

    myVars = {}

    def get_object(self):
        pass





"""

NOTES:


Popup forms framework for Django

All of the following popup stuff was found here:
https://github.com/joinourtalents/django-popup-forms
And you might want to go there to better read it although I have added some notes
where you see these 11 stars ***********

Problem

To have easy way to show popup window, holding any form, from any page of the website
(examples: send message from user profile or from list of profiles; apply/withdraw to pool from list of companies, etc.)
This popup window should be pre-loaded, i.e. there should not be HTTP request to server in order to open popup window
In case form error occurs (some fields are missing, email format is wrong, etc.) the same
form should be re-populated in the same page, indicating errors
After form is submitted, user should be redirected to either the same, or specified page
Solution


The solution consists of 4 components:


1.  Template tag, rendering popup form and link for opening it:

{% popup_form 'id1' popup_forms.ApplyForm '/talent/apply/6/' 'popup_forms/apply_to_pool.html' %}
{% popup_form 'id2' popup_forms.SomeModelForm '/talent/apply/6/' 'popup_forms/apply_to_pool.html' kwarg1=... kwarg2=... %}


2.  Decorator for view function, that is processing popup form submission, and exception to handle form errors:

import popup_forms

@popup_forms.handler
def form_view(request):
    if request.method == 'POST':
        form = ApplyForm(request.post)
        if not form.is_valid():
            return popup_forms.OpenFormResponse(request, form)
        # ...
        # ... FORM PROCESSING GOES HERE ...
        # ...
        return popup_forms.CloseFormResponse(request)
    else:
        return redirect('failure_url')
        # or raise Http404
        # or just popup_forms.CloseFormResponse(request)


3.  Template to render the form, derived from popup_forms/base.html
no notes for this section except for this optional bit.

(optional) context processor (popup_forms.context_processors.popup_forms), that puts all
PopUp form classes to context, in order not to pass it each time in view:

in settings:

POPUP_FORMS = ('messages.forms.WriteMessageForm',
               'talentbutton.forms.ApplyForm',
               'talentbutton.forms.ConfirmForm',)
in template it could be accessed:

{{ popup_forms.WriteMessageForm }}, etc.


4.  Decorator to conditionally display popup form on page load (for example, to fill in
some missing information after registration/login):


***********
They just had @show_popup_form... here;

@popup_forms.show_popup_form('/account/register/details/',
                 lambda request: 'register-details' in request.session)
def some_my_view(request):
    ...
    *********** I believe this is just the underlying page eg index.html



Use case is following:

Template tags renders the form, together with link:

*********** maybe change onclick to onload

<a href="..." onclick="open the form">Link Title</a>
<div class="hidden_form">
    <form>...</form>
</div>

When user clicks on link, the form, already pre-loaded in template, just makes visible.

User fills form, and submits it. POST request goes to form processing URL.

If form is valid, it is processed, handler returns CloseFormResponse to close the
popup form, and user is redirected to success url (which by default is the referrer page where popup form was rendered).

If form contains errors, handler returns OpenFormResponse, it is handled by decorator,
which stores form data AND ERROR DATA in session, and redirects back to referring view.

The {% popup_form %} tag then finds data, stored by decorator, and re-populates form
making it VISIBLE (not hidden) - user sees the same form, with errors.

Conditions

There is no separate template to be rendered by form processing view. That's why form
processing view should not render anything: it just porcesses forms, and makes redirects.
If the view renders something, the decorator raises exception.

Disadvantages

If there are many links in the page, for each link a separate form is rendered hiddenly.
However, HTML of the form does not take much space (less than 1000 characters).
Right now we have problem to scroll page to the same position after re-populating form with errors, but it can be resolved.


############# End Popup forms framework for Django




# reverse is like redirect in gae.
# If the URL accepts arguments, you may pass them in args.
# It stops the db from being written to a second time if the user
# hits the back button.
# https://docs.djangoproject.com/en/1.10/ref/urlresolvers/
https://docs.djangoproject.com/en/1.10/intro/tutorial04/



Generic view notes:

Davee I think you should use a DetailView when you are passing
a var/object/additional url to the url mapper and use a
ListView when you are not passing anything additional.

More info from:
http://stackoverflow.com/questions/9777121/django-generic-views-when-to-use-listview-vs-detailview

If you're going to add forms to edit the posts, it might make
sense to use a ListView instead.  A DetailView should not be
paginated, it's intended to be used with one object only.

Question;
I'm looking at the detail view of a tag that just so happens
to have a huge list of posts that I want paginated. I could
easily have written it as a listview, but then I would have
had to add the tag back to the context. Which seems backwards.

Answer; you can add MultipleObjectMixin to your DetailView,
which allows you to reuse pagination. You just need to ensure
self.object_list is set to the queryset of filtered objects
you want to paginate.
--

From Django docs:
https://docs.djangoproject.com/en/1.10/intro/tutorial04/
We're using two generic views here: ListView and DetailView.
Respectively, those two views abstract the concepts
of "display a list of objects" and "display a detail page
for a particular type of object."

Each generic view needs to know what model it will be acting
upon. This is provided using the model attribute.
The DetailView generic view expects the primary key value captured
from the URL to be called "pk", so we've changed question_id to pk

for the generic views in the url mapper found at:
/mysite/myPolls/urls.py

By default, the DetailView generic view uses
a template called <app name>/<model name>_detail.html. In
our case, it would use the template "myPolls/question_detail.html".
The template_name attribute is used to tell Django to use
a specific template name instead of the autogenerated default template
name.

We also specify the template_name for the results list
view - this ensures that the results view and the detail view
have a different appearance when rendered, even though they're
both a DetailView behind the scenes.

Similarly, the ListView generic view uses a default template
called <app name>/<model name>_list.html; we use template_name to
tell ListView to use our existing "myPolls/index.html" template.

AND
IMPORTANT ************************************

From mysite/myPolls

In previous parts of the tutorial, the templates have been
provided with a context that contains the question and
latest_question_list context variables. For DetailView
the question variable is provided automatically - since

we're using a Django model (Question), Django is able to
determine an appropriate name for the context variable (ie Davee 'question').

I am going to over-ride that because it is a dumb idea (very confusing).
  I have added
context_object_name = 'latest'

The original class DetailView had no such declaration yet django was
able to find 'question' var in the detail.html file.

However, for ListView, the automatically generated context
variable is question_list. To override this we provide the

context_object_name attribute, specifying that we want to use
latest_question_list instead (as it is named in our index.html file).
As an alternative approach, you
could change your templates to match the new default context
variables - but it's a lot easier to just tell Django to
use the variable you want.


########################## End Generic view notes




# The old way.
#def index(request):
#    return HttpResponse("Hello, world. You're at the myFrog index.")

"""






