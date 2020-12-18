from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from django.utils import timezone

# Create your models here.

# CAUTION:  All fields must have a value if no default is given.

@python_2_unicode_compatible  # For python 2 support.
class User(models.Model):

# This is a hashpass and contains the algo$iterations$salt$hash.
    password = models.CharField(max_length=200)
    userName = models.CharField(max_length=200)

# How many votes you have made so far.
    numVotes = models.IntegerField(default=0)
    email = models.CharField(max_length=200)

# Don't use these they don't see the admin page.
# verbose_name='date_user_joined', auto_now=True

# Give it a better name for the admin db label date_user_joined
    created = models.DateTimeField('date_user_joined', default=timezone.now())

# returns a string instead of a reference to an object.
# You also need this for the decorator above.
# You could return any of the char fields above to the view.py
    def __str__(self):
#       'pass'
# CAUTION: Don't put 'pass' in here or the interprater will fuck up
# trying to return a non unicode object.
        return self.userName



################### End User




@python_2_unicode_compatible  # For python 2 support.
class PendingUser(models.Model):

# This is a hashpass and contains the algo$iterations$salt$hash.
    password = models.CharField(max_length=200)
    pendingUserName = models.CharField(max_length=200)

    email = models.CharField(max_length=200)


# Don't use these they don't see the admin page.
# verbose_name='date_user_joined', auto_now=True

# Give it a better name for the admin db label date_user_joined
    created = models.DateTimeField('date_pendingUser_joined', default=timezone.now())

# returns a string instead of a reference to an object.
# You also need this for the decorator above.
# You could return any of the char fields above to the view.py
    def __str__(self):
        'pass'
# CAUTION: Don't put 'pass' in here or the interprater will fuck up
# trying to return a non unicode object.
        return self.pendingUserName



################### End PendingUser



"""

To clear the sessions db I tried:
python manage.py clearsessions
It did not work because chrome remembers them for a spell.
It worked for firefox.


Some ways to access the db, there are 3.  I will use the first way below.


But first see this; interacting with more than one db.
NO DON'T, I'm not using multiple db, just multiple tables.
https://docs.djangoproject.com/en/1.10/topics/db/multi-db/


1.  Executing custom SQL directly

This is how I am going to do it.  It is the most robust and you
actually access the db directly.

See here three quarters of the way down the page:
https://docs.djangoproject.com/en/1.10/topics/db/sql/


Sometimes even Manager.raw() isn't quite enough: you might need to perform
queries that don't map cleanly to models, or directly execute UPDATE, INSERT,
or DELETE queries.

In these cases, you can always access the database directly, routing around
the model layer entirely.

The object django.db.connection represents the default database connection.
To use the database connection, call connection.cursor() to get a cursor
object. Then, call cursor.execute(sql, [params]) to execute the SQL and
cursor.fetchone() or cursor.fetchall() to return the resulting rows.

For example:

from django.db import connection

def my_custom_sql(self):
    with connection.cursor() as cursor:
        cursor.execute("UPDATE bar SET foo = 1 WHERE baz = %s", [self.baz])
        cursor.execute("SELECT foo FROM bar WHERE baz = %s", [self.baz])
        row = cursor.fetchone()

    return row
Note that if you want to include literal percent signs in the query,
you have to double them in the case you are passing parameters:

cursor.execute("SELECT foo FROM bar WHERE baz = '30%'")
cursor.execute("SELECT foo FROM bar WHERE baz = '30%%' AND id = %s", [self.id])
If you are using more than one database, you can use django.db.connections
to obtain the connection (and cursor) for a specific database.
django.db.connections is a dictionary-like object that allows you
to retrieve a specific connection using its alias:

from django.db import connections
cursor = connections['my_db_alias'].cursor()
# Your code here...

By default, the Python DB API will return results without their
field names, which means you end up with a list of values, rather
than a dict. At a small performance and memory cost, you can return
results as a dict by using something like this:


2. Perform raw SQL queries.  See the same docs as above.


3.  This reference has lots of commands and stuff you can use for above.


# See here:  https://docs.djangoproject.com/en/1.9/ref/models/querysets/#values-list
# flat takes it out of the list and turns it into a string, only good
for one object.

An example from my logOn()/handler.

dbPass = PendingUser.objects.values_list('pendingUserName','password',
'email', 'created').filter(pendingUserName = userName)
here is wat dbPass looks like, a tuple in a list.

<QuerySet [(u'bill', u'pbkdf2_sha256$30000$6FGO4mYDlJdQ$99lm/cor6XB5ltN8lGbp8ApfluXu+HSbXs02fWdrcKU=',
u'b@b.com', datetime.datetime(2016, 11, 19, 20, 28, 17, 890930, tzinfo=<UTC>))]>









"""