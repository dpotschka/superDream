
Davee Read these for setting up your website connections etc.


All the stuff in this file is from the tutorials:

This one is for setting up deploy on pa and use in conjuction with the
one below.
pythonAnywhere Django docs.
https://help.pythonanywhere.com/pages/FollowingTheDjangoTutorial
In that file where you see this;
mkvirtualenv django17 --python=/usr/bin/python3.4

I used this intsead;
mkvirtualenv django17 --python=/usr/bin/python2.7
I got some ssl error messages regarding urllib3 but I
think I will be using urllib2.
Installed django 1.10.3

This one is for setting up locally and on production, most of it.
Official Django website docs.
https://docs.djangoproject.com/en/1.10/intro/tutorial01/

--





1.


Always make sure your virtualenv is active when working on the
django tutorial.  If you need to reactivate it later, maybe if
you close your bash console and open a new one, the command is:

workon django17

cd mysite, or where ever you app is for everything from here on.
That is where the manage.py is.
Use <ls> command to see the files and directories underneath your current directory.
That's a small L in <ls>...


If you want the python shell:
python manage.py shell
To import a db type:
from myFrog.models import User
from myFrog.models import PendingUser

To run the app locally (close google app engine first) then:
python manage.py runserver
http://localhost:8000/polls/


Don't forget to change this stuff first:


In:
https://www.pythonanywhere.com/user/timetable/files/var/www/timetable_pythonanywhere_com_wsgi.py?edit
That is found on:
https://www.pythonanywhere.com/user/timetable/webapps/#tab_id_timetable_pythonanywhere_com
It is the "web" tab at pythonAnywhere.com
In the 'Code:' section, scroll down and look for this;
WSGI configuration file:/var/www/timetable_pythonanywhere_com_wsgi.py
Goto that file and set stuff up.  Lots of more set up stuff follows.



In:
/timetable/mysite/mysite/settings.py
To run locally you need leave it blank:
ALLOWED_HOSTS = []
# Local:
STATIC_ROOT = 'c:/Daves_Python_Programs/pythonAnyWhere/mysite/myPolls/static'

For production set
ALLOWED_HOSTS = ["timetable.pythonanywhere.com"]
# Production:
STATIC_ROOT = '/home/timetable/mysite/myPolls/static'

In:
/timetable/mysite/mysite/wsgi.py
Production set
path = '/home/timetable/mysite'
# For local.
path = 'c:/Daves_Python_Programs/pythonAnyWhere/mysite'

Don't forget to run this everytime you add a static file:
python manage.py collectstatic  see 16 if you don't want to.

This gets your db sqlite3, it is in the pa docs above.
CAUTION:
run these if you ever make any changes to your db models.
From the virtual environment /superFrog run:
python manage.py makemigrations
python manage.py migrate

WARNING:
In a db model;
Don't define a __str__() with a 'pass' as a statement
or the db will fuck up when using the interprater.
You must return something, like the userName.

--


Set up your directory structures the same way as done in this example
web site (mysite).
Django is set up to search all apps in one web site (mysite).  A website can
have more than one app.

You need to nest your templates down so that Django doesn't grab templates
from one of your other apps.  Same with static files.
https://docs.djangoproject.com/en/1.10/howto/static-files/

like you have here:
/mysite/myPolls/templates/myPolls/index.html

mysite is your website and myPolls is an application in that website.

--

You have two template directories (one for myPolls)
https://www.pythonanywhere.com/user/timetable/files/home/timetable
    /mysite/myPolls/templates/myPolls
has detail.html, index.html and results.html and that's all in it.

and a second template folder here (to format the html of your admin page)
https://www.pythonanywhere.com/user/timetable/files/home/timetable/mysite
   /templates/admin/base_site.html
Which is driven by /mysite/myPolls/admin.py
I also had to create that admin directory.  According to the tutorial 7.

You also have two admin directories,
the second one is for static files and is in:
/mysite/myPolls/static/admin

In lesson 7 of the tutorial when you get to this part:
"Now create a directory called admin inside templates, and
copy the template admin/base_site.html from within the
default Django admin template directory in the source code
"of Django itself (django/contrib/admin/templates) into that directory.

You must enter this url to get that file, it is hidden:
https://www.pythonanywhere.com/user/timetable/files/usr/local/lib/python2.7/dist-packages/django/contrib/admin/templates/admin

I got it here already:
<!--
{% extends "admin/base.html" %} {% block title %}
{{ title }} | {{ site_title|default:_('Django site admin') }}{% endblock %}

{% block branding %}

to get your own title, delete this entire next line and type in what ever uwant.
{{ site_header|default:_('Django administration') }}

{% endblock %} {% block nav-global %}{% endblock %}
-->

change it to this:

{% extends "admin/base.html" %}
{% block title %}{{ title }} | {{ site_title|default:_('Django site admin') }}
{% endblock %}

{% block branding %}
Dave is a cool administrator

{% endblock %} {% block nav-global %}{% endblock %}


CAUTION: The tutorial 7 says to get the index.html file as well from the
above hidden url, but when you put that index.html file in this dir
/mysite/templates/admin/ it fucks shit up.  I think django is doing this
for us now in the background somewhere.  So I just got rid of that file
and now everything works great.


then,

Set
mysite/settings.py
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',

        'DIRS': [os.path.join(BASE_DIR, 'templates')],...


-- End To Format the html of your admin page


We'll discuss in more detail in the reusable apps tutorial why we do this
multiple template and admin directories.  It's so we can turn
myPolls into a package and store it in python27/site-packages/lib
We want the package functionality to be seperate from mysite.  See 18
below.  I did the package thing it works great but you can't do it
online because pa controls which packages go into /lib
https://docs.djangoproject.com/en/1.10/intro/reusable-apps/





---- End 1



2.

This is found on the very front of pythonAnywhere and is the first pointer
to your web site files.  Set it up to do that.
/var/www/timetable_pythonanywhere_com_wsgi.py

---- End 2


3.

To log into the virtual environment for Django type <workon django17>.
When using the bash console don't forget to cd mysite.
type <python manage.py shell>, to get ipython integrated developer shell.
type exit() to exit either of the above two, they are independant you can't
be in both at the same time unles you open up two shells.

---- End 3


4.

In:
/timetable/mysite/manage.py

set
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")


---- End 4


5.

In:
/timetable/mysite/mysite/settings.py

For production set
ALLOWED_HOSTS = ["timetable.pythonanywhere.com"]

To run locally you need leave it blank:
ALLOWED_HOSTS = []

and watch out for this:

# Application definition

INSTALLED_APPS = [

    # Watch out for this I think it was autogenerated, should be
    # a cap P here  |  I worked a fix for it though.
    'myPolls.apps.MypollsConfig',

--

set
ROOT_URLCONF = 'mysite.urls'

set
WSGI_APPLICATION = 'mysite.wsgi.application'


If you want to use a different db, I believe you set it here:

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/  #databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

--

set
TIME_ZONE = 'America/Vancouver'


This is already set for you:
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'

See 15 below for more on these two and media files, but this is all you need for now.

These get your javascrit, image, css, and fonts files.
# Production:
STATIC_ROOT = '/home/timetable/mysite/myPolls/static'

# Local:
STATIC_ROOT = 'c:/Daves_Python_Programs/pythonAnyWhere/mysite/myPolls/static'




---- End 5


6.

In:
/timetable/mysite/mysite/urls.py

That is your first url mapper and points to the handlers and
additional url mappers.
Goto that file for more detailed help.


---- End 6



7.

In:
/timetable/mysite/mysite/wsgi.py

That is your second wsgi pointer (see 2 above).

set
path = '/home/timetable/mysite'

# For local.
path = 'c:/Daves_Python_Programs/pythonAnyWhere/mysite'


set
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")


---- End 7



8.


In:
/timetable/mysite/myPolls/admin.py

Register you db models here.


---- End 8


9.

In:
/timetable/mysite/myPolls/apps.py

# Watch out for this, I think it was autogenerated, should be a cap P
# here  |
class MypollsConfig(AppConfig):
    name = 'myPolls'


---- End 9


10.

In:
/timetable/mysite/myPolls/models.py

This is where you declare your class db models.

---- End 10


11.  Tests


See the tutorial on how to access these tests from bash.
https://docs.djangoproject.com/en/1.10/intro/tutorial05/

In:
/timetable/mysite/myPolls/tests.py

Django will look here for testing from bash.  Write your own tests
there are some in here we did for the mysite project.

# django will automatically run these tests when you run
# 'python manage.py test myPolls' from bash /mysite
# It sets up its own temporary db to do this.


from myPolls.models import Question
You can do that because /myPolls has __init__.py file in it.


reverse explained:
https://docs.djangoproject.com/en/1.10/ref/urlresolvers/#reverse

from django.urls import reverse
return HttpResponseRedirect(reverse('url_name'))
This looks through all urls defined in your project for the url
defined with the name url_name and returns the actual url /foo/.

This means that you refer to the url only by its name attribute - if
you want to change the url itself or the view it allows you to
do this by editing one place only - urls.py.


---- End 11 Tests.



12.

In:
/timetable/mysite/myPolls/urls.py

That is your second url mapper (see 6 above).


# This tells django which app the urls belong to
# when using the url tag var in an html file, see
# templates/myPolls/index.html.  It is very important to set this.
See the bottom of tutorial 3:
https://docs.djangoproject.com/en/1.10/intro/tutorial03/

Hit ctrl F in chrome to search for a string.

set
app_name = 'myPolls'


---- End 12



13.

In:
/timetable/mysite/myPolls/views.py

This is where all your handlers reside.
Very cool, visit it and learn the way Django does stuff.


---- End 13



14.

In
/mysite/myPolls/templates/myPolls

That is where your html files are and
NOTE how the final "myPolls" directory is nested down after templates,
Django will search all apps with a templates folder and it will pick
the first html file after that templates folder

that matches your path/name.html so if you have more than
one app running on the same web site (ie you will have more than
one templates folder) you BETTER MAKE DAM SURE YOU
NEST YOUR FINAL DIRECTORY AFTER THE templates directory!!!
Do NOT store html files like this /templates/name.html


The same goes for static files (css, javascript):

Static file namespacing

Just like templates, we might be able to get away with putting our
static files directly in myPolls/static (rather than creating another
MyPolls subdirectory), but it would actually be a bad idea.
Django will choose the first static file it finds whose name

matches, and if you had a static file with the same name
in a different application, Django would be unable to distinguish
between them. We need to be able to point Django at the
right one, and the easiest way to ensure this is by namespacing

them. That is, by putting those static files inside another directory
named for the application itself.

---- End 14


15.

Make your life easy and use the virtual environment (with the console bash)
and the turorial to auto set up most of the stuff for you.

These two tutorials work together.  PythonAnywhere is a bit different
from developing locally so you must follow both tutorials at the same time.

pythonAnywhere Django docs.
https://help.pythonanywhere.com/pages/FollowingTheDjangoTutorial

Official Django website docs.
https://docs.djangoproject.com/en/1.10/intro/tutorial01/



---- End 15



16.


How to setup static files in Django
There are 3 main things to do:

set STATIC_ROOT in settings.py
run manage.py collectstatic
set up a Static Files entry on the PythonAnywhere Web tab.
Optionally, you can also customise STATIC_URL, if you want to
use a static URL prefix other than /static/

Set STATIC_ROOT in settings.py

The STATIC_ROOT variable in settings.py defines the single folder
you want to collect all your static files into. Typically, this
would be a top-level folder inside your project, eg:


# Local:
STATIC_ROOT = 'c:/Daves_Python_Programs/pythonAnyWhere/mysite/myPolls/static'

# Production:
STATIC_ROOT = "/home/myusername/myproject/static"

# or, eg,
STATIC_ROOT = os.path.join(BASE_DIR, "static")
The important thing is this needs to be the full, absolute path
to your static files folder.

From bash virtual environment shell (see 3 above)
Run manage.py collectstatic

This command collects up all your static files from each of
your app folders (including the static files for the admin app)
and from any other folders you specify in settings.py, and copies
them into STATIC_ROOT.

You need to re-run this command whenever you want to publish new
versions of your static files.

(Optionally) change STATIC_URL

If you really must, you can change the default STATIC_URL,
which is /static/, to being a different prefix, like /assets/, or whatever
it may be. You'll probably want to use the {% static %} template
tag with this in your html file. There's more info in the django docs.

Set up a static files mapping

Finally, set up a static files mapping to get our web servers
to serve out your static files for you.

Go to the Web tab on the PythonAnywhere dashboard
Go to the Static Files section
Enter the same URL as STATIC_URL in the url section (typically, /static/)
Enter the path from STATIC_ROOT into the path section (the full
path, including /home/username/etc)
Then hit Reload and test your static file mapping by going to
retrieve a known static file.

Eg, if you have a file at /home/myusername/myproject/static/css/base.css,
go visit http://www.your-domain.com/static/css/base.css
or just run your web page with some pretty colors.

Serving static files in development

Django does have an alternative for serving static files during
development, which can avoid the need for you to run collectstatic
whenever you make changes to your files, but it comes at the cost of
putting an extra processing burden on the Python parts of your app.
If you really want to use this, you'll find more info in the django docs.

Media files

If you're using Django's default uploaded files handling, then
you'll need to set up a similar static files mapping from MEDIA_URL
to MEDIA_ROOT...

--

Warning

I think this refers to using command:
python manage.py collectstatic


Of course the {% static %} template tag is not available for use
in static files like your stylesheet which aren’t generated by
Django. You should always use relative paths to link your
static files between each other, because then you can
change STATIC_URL (used by the static template tag to
generate its URLs) without having to modify a bunch of
paths in your static files as well.


---- End 16


17.

Git stuff.


https://help.github.com/articles/pushing-to-a-remote/

To get your PA files on your local machine you have to push them to
github first (use PA bash),  You may have to pull the github files
to PA first to integrate the two repos.

then you can pull them from github to your local directory using
your local bash.
cd into your local directory first.

Always commit any changes before pushing or pulling.

Me on github:
https://github.com/dpotschka/mysite

Me on pythonAnyWhere (pa):
https://www.pythonanywhere.com/user/timetable/files/home/timetable/mysite

Me on my local machine:
c:/Daves_Python_Programs/pythonAnyWhere/mysite.

So from paw /mysite, but first do the commit thing below...
git push https://github.com/dpotschka/mysite
user name = dpotschka@yahoo.com
password = ph.....2

To pull from git to local machine:
open gitbash or git shell on local machine, navigate to /mysite
git pull https://github.com/dpotschka/mysite
user name = dpotschka@yahoo.com
password = ph.....2
blah blah yeah!
--


Type help to get help with commands.

To initialize a new repository (repo):
goto the directory where you want the repo to be.
git init

Get repository (repo) setup here and a lot more:
http://www.njedesign.com/github-basic-commands-for-creating-and-pushing-to-repository/

to add files or directory:
git add mysite/
then
git commit

To exit (for pa) a message while doing a "git commit":
hit <esc>
then
:wq and the commit will happen.

To exit a message on local just save the message then close the FILE THEN
close the editor.

You can also do:
git commit <file name>

And for when you have been altering stuff do this afterwords:
git add --all
git commit --all
then add a message like your name and the date then
<esc> :wq



To force a merge from githup.com to pa when pulling from pa.
git merge --a and
git merge -a
do both in a certain order.

git help commit -a
using the -a switch with the commit command to automatically "add" changes
from all known files (i.e. all files that are already listed in the index)
and to automatically "rm" files in the index that have been removed from
the working tree, and then perform the actual commit.

More useful commands:
Use the https if you don't have ssh,
free accounts at pa don't have ssh.

Use this when pushing to github.com from local.
git push --set-upstream https://github.com/dpotschka/mysite master

git clone <repo URL from GitHub>
cd into the newly-cloned directory.
git diff
git push  <url>
git pull  <url>


for debugging

git status
git branch -a
and
git log


Committer: timetable <timetable@24dcaea7d349>
Your name and email address were configured automatically based
on your username and hostname. Please check that they are accurate.
You can suppress this message by setting them explicitly:
    git config --global user.name "Your Name"
    git config --global user.email you@example.com

20:56 ~/mysite (master)$ git config --global user.name "timetable"
20:58 ~/mysite (master)$ git config --global user.email dpotschka@yahoo.com
20:59 ~/mysite (master)$

--

cleaning and shrinking your git, do this before your quota gets over 70% or
you won't have room to do it:

you can call git gc --aggressive --prune, which will perform garbage collection
in your repository and prune old objects. do you have a lot of binary files
(archives, images, executables) which change often? those usually lead to
huge .git folders (remember, git stores snapshots for each revision
and binary files compress badly)

git will take up about 1.75 times your original files.  My original files are
currently equal to 295mb and my git is 520mb.  My total disk usage (du) is
795mb Jan 7/19.  See your hacking section for du commands.

--



--------------------------- End 17 Git stuff



18.  Re-using your myPolls app as a django/python package.


This will NOT work online at pa because they won't allow you to add a
package to python/sit-packages/lib, you must ask them to add packages.

I did this locally and it worked.  Follow the tutorial here:
https://docs.djangoproject.com/en/1.10/intro/reusable-apps/

Some changes you must do:
A few things to django-myPolls/setup.py there are instructions in that file.

When you pip install the package it goes into c:/Python27/site-packages/lib/myPolls
which is correct.  I noticed that the directory lib is not in alphabetical order.
Anyway, when you pip install, you must be in or not?
c:/Daves_Python_Programs/pythonAnyWhere/mysite

then I moved the zip file so it would be less typing
pip install c:/django-myPolls-0.1.zip  or the old location, it is still in there
pip install c:/Daves_Python_Programs/pythonAnywhere/django-myPolls/dist/django-myPolls-0.1.zip

You will also have to run the server again.

I have unistalled it again and put things back to normal
so that my local site is still the same as pa.
I will leave the /django-myPolls though so you don't have to go through the entire
tutorial again.  All you will have to do is delete myPolls from /mysite if you want
to put myPolls back into the python lib as a package.  Just do pip install..


More things you must do:

see /django_myPolls.egg-info/PKG-INFO for more setup info.
/django-myPolls/README.rst they are similar.  I created them
from the tutorial.

In /mysite/mysite/settings.py

INSTALLED_APPS = [
    change this next bit
    'myPolls.apps.MypollsConfig',
	to
	'myPolls',

CAUTION:
Application labels (that is, the final part of the dotted path to
application packages) must be unique in INSTALLED_APPS. Avoid
using the same label as any of the Django contrib packages,
for example auth, admin, or messages.


In /mysite/mysite/urls.py you must

Include the myPolls URLconf in your project urls.py like this:
urlpatterns = [
    url(r'^myPolls/', include('myPolls.urls')),...


Quick start (In summary Davee)
-----------

1. Add "myPolls" to your INSTALLED_APPS setting

(mysite/mysite/settings.py) like this::

    INSTALLED_APPS = [
        ...
        'myPolls',
    ]

2. Include the polls URLconf in your project urls.py like this::

    url(r'^myPolls/', include('myPolls.urls')),

3. Run `python manage.py migrate` to create the myPolls models.
I didn't do number 3 and it still worked.  Because the db is holding state
for git pull probably.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a poll (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/myPolls/ to participate in the poll.


https://docs.djangoproject.com/en/1.10/howto/static-files/

Try altering (mysite/mysite/settings.py) :
STATIC_ROOT = 'c:/Daves_Python_Programs/pythonAnyWhere/mysite/myPolls/static'

change it to (DONE it still works)
STATIC_ROOT = os.path.join(BASE_DIR, "static")

or get rid of it.  (DONE it still works without the static root)
AND
There is no STATIC_ROOT when you first create a new project.

CAUTION: It may still work because you are not using any static files.


----------- End 18.  Re-using your myPolls app as a django/python package.




19.  Paypal setup


My Paypal modules are in here:
https://www.pythonanywhere.com/user/timetable/files/home/timetable/.virtualenvs/django17/lib/python2.7/site-packages/paypal/standard/ipn
I may have to move them to get access them.

See help here:
http://django-paypal.readthedocs.io/en/stable/standard/ipn.html

http://stackoverflow.com/questions/757809/django-paypal-setup
https://github.com/johnboxall/django-paypal
https://github.com/spookylukey/django-paypal



----------------------- End 19.  Paypal setup



20.  Hacking PAW

The file you are currently reading is here:  just for
reference for all of the following;
https://www.pythonanywhere.com/user/timetable/files/home/timetable/superDream/Davee_ReadMe.txt?edit
--

To navigate to your home directory, use "cd" or "cd ~"
21:19 ~ $ dir
README.txt
superDream
www.theHyperDream.com.combined.cert
www.theHyperDream.com.csr
www.theHyperDream.com.key
--

To navigate up one directory level, use "cd .."
Takes you to the parent directory.

To navigate to the previous directory (or back), use "cd -"

get a directory listing by typing
dir

You should be able to copy files and directories and move them around
like this.  Try this it works:
00:49 ~ $ cd /

00:49 / $     # The https://www.pythonanywhere.com/user/timetable/files/ directory Davee.
That's as far back as you can go.

00:49 / $ dir
bin   dev  home  lib64  mnt  proc  run   srv  tmp  var
boot  etc  lib   media  opt  root  sbin  sys  usr
00:49 / $ cd hom

00:52 /home $ dir
timetable
00:52 /home $ cd timetable
00:52 ~ $    # The timetable directory Davee.

See if you can get into these two places to move those paypal files around:
Yes you can...
https://www.pythonanywhere.com/user/timetable/files/usr/local/lib/python2.7/dist-packages/django/contrib/admin/templates/admin
https://www.pythonanywhere.com/user/timetable/files/home/timetable/.virtualenvs/django17/lib/python2.7/site-packages/paypal/standard/ipn
https://www.pythonanywhere.com/user/timetable/files/home/timetable/superDream

--

Coping files in Bash:
http://stackoverflow.com/questions/3643848/copy-files-from-one-directory-into-an-existing-directory

What you want is:
t1 and t2 are directories, copy everything from t1 into t2.
cp -R t1/. t2/
The dot at the end tells it to copy the contents of the current directory,
not the directory itself.  This method also includes hidden files and folders.
Use the full directory path, you must be outside the destinations.
Tested it and it works that way.


Here's one I did:

At non virtual environment bash.  Directory:
https://www.pythonanywhere.com/user/timetable/files/home/timetable/
which is just   ~ $


copied
.virtualenvs/django17/lib/python2.7/site-packages/jsonfield/.

To:
superDream/sales/jsonfield/

You must create the target directory first (eg jsonfield).

----

Here is another one I did, all on one line:
cp -R superDream/django-popup-forms/. superDream/popup/


And I did this one.
cp -R superDream/popup/. superDream/myDream/popup/

--

How to find what's using up all your space
Open up a Bash console and use the du ("disk-usage") to find out how much space
is being used in various places in your file storage:

See here for switches:
https://ss64.com/bash/du.html

Disk Usage - report the amount of disk space used by the specified files and for each subdirectory.

Syntax
      du [options]... [file]...
With no arguments, `du' reports the disk space for the current directory.
Normally the disk space is printed in units of 1024 bytes, but this can be overridden

OPTIONS
-a
--all
Show counts for all files, not just directories.


du -hs /tmp ~/.[!.]* ~/* | sort -h


------------------------------ End 20.  Hacking PAW


Set up SSL


Nov 19/19
They have a free ssl now at paw that is just one click to set up and it auto renews so
you never have to do any of the following again.  See Here:
https://help.pythonanywhere.com/pages/HTTPSSetup
DONE


--


What follows is the old way...



First use the instuctions found here to create your key and your csr:
https://help.pythonanywhere.com/pages/SSLOwnDomains/
you must use www.thehyperdream.com as your web site common name.


Then goto your ssl provider namecheap.com and activate your certificate ie
paste your csr into the form.

For DCV verification use: http

Then:
Specify who we should send the SSL certificate and the bundle/chain file to
answer: dave@thehyperdream.com

Then:
You download the domain control validation DCV file from namecheap.
You will find this file at your namecheap account follow these instructions to download it:
https://www.namecheap.com/support/knowledgebase/article.aspx/10025/68/how-to-complete-httpbased-validation#find
The file name is something like this:
AD0AC50BCB5650CAA8781523EEA222DC.txt    This was the one from 2018.

Then:
Upload the validation file TO:
/home/timetable/superDream/myDream/templates/myDream/AD0AC50BCB5650CAA8781523EEA222DC.txt

Then
www.thehyperdream.com/.well-known/pki-validation/
You have that url mapper that uses this, it is in your first url mapper for
thehyperdream.com
/home/timetable/superDream/superDream/urls.py

This is what it looks like:
You will have to change this long hash.txt file name to the new one (the one
you just downloaded from namecheap) and put that file name in here.
This is to verify who I am DCV.                                            file.function
url(r'^.well-known/pki-validation/AD0AC50BCB5650CAA8781523EEA222DC.txt', sslVerify.sslVerify, name='sslVerify'),

Then
Put that name/location of the text file in your server/render logic function here:
/home/timetable/superDream/myDream/sslVerify.py
DONE

Then ask them NAMECHEAP to verify your http Domain Control Validation DCV.

Here are the words you say to them:
To namecheap:
I am a web master,
I need your ssl department, to ping my web site for ssl http DCV

user: timetable11
pin:4622  get your new pin first, they will give you one in the chat.
They need to ping this.
https://www.thehyperdream.com/.well-known/pki-validation/AD0AC50BCB5650CAA8781523EEA222DC.txt

Then
They will email you the certificate and the bundle/chain.

Then follow the rest of the instructions at:
https://help.pythonanywhere.com/pages/SSLOwnDomains/

1.  www.theHyperDream.com.combined.cert  DONE
2.  www.thehyperdream.com.csr
3.  www.thehyperdream.com.key
Put those 3 files into here:
/home/timetable
DONE
The last two files are put into the above directory for
you when you create them with the PAW Bash console.
Back up all those files on your hard drive.


Make sure you have a space between the certificates in your
www.theHyperDream.com.combined.cert  file.


----------------------- End Set up SSL




                             INDEX


    CONTENTS                                                LINE NUMBER


mkvirtualenv django17                                        15



17.  Git stuff.                                             611


20.  Hacking PAW                                             875


