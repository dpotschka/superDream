# This contains functions for making passwords etc.
# Just do:
# from davesHappyFamily import util.make_password, ..., ... etc.


import random
import string
# This is a hasing library to create a secure value.
import hmac

#from string import letters




# For Making cookies


# 's' should be the user id or something specific to the user.
# It is stored left of the |.

secret = 'qdkfadkj39534857z938O457'
def make_secure_val(s):

    # We switch the comma to '|' as the comma doesn't work on gae.
    return "%s|%s" % ( s, hmac.new(secret, s).hexdigest() )

# This checks to see if the hash is a secure val.
def check_secure_val(h):

# You can't split a none type, so h had better exist or else you get an error.
# You will get this error if you are not logged in and you try to post a blog.
    if h:
        val = h.split('|')[0]
        if h == make_secure_val(val):
            return val

################### End For Making cookies



def text_password():
    """ The automatic password for new users"""
    return (''.join(random.choice(string.letters) for x in xrange(8)) ).lower()



def valid_pass(passw):
    if len(passw) < 8 or (len(passw) > 20):
        return False
    return True



