from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible


from .jsonfield import fields
#from jsonfield import JSONField
#from .fields import JSONField


from django.utils import timezone


@python_2_unicode_compatible  # For python 2 support.
class ClientDB(models.Model):

    """
    This db captures the clients email address after paypal
    sends me an ipn.
    """

    client_email = models.EmailField(default = 'm@m.com')
    first_name = models.CharField(max_length=50, default = 'Super Client')
    last_name  = models.CharField(max_length=50, default = 'na')

    #pledgeAmount = models.IntegerField('Pledge_Amount', default = 0)

    created = models.DateTimeField('clients_first_purchase', default=timezone.now())



    def __str__(self):

        return self.client_email


###################### End ClientDB




"""
You can do this in a db Davee.
default

Field.default
The default value for the field. This can be a value or a callable object.
If callable it will be called every time a new object is created.

The default can't be a mutable object (model instance, list, set, etc.), as
a reference to the same instance of that object would be used as the default
value in all new model instances. Instead, wrap the desired default in a
callable. For example, if you want to specify a default dict for JSONField,
use a function:

def contact_default():
    return {"email": "to1@example.com"}

contact_info = JSONField("ContactInfo", default=contact_default)

"""
def txn_default():
    return {"email": "dave@theHyperDream.com"}

@python_2_unicode_compatible  # For python 2 support.
class PaypalDB(models.Model):

    # Fields for a buyer who is using a Paypal account or credit card
    # to make their purchase.  This is an example of someone who bought 3 items.

    """
    mc_gross=50.00     # real
    mc_gross_1=20.00   # A dict key/strings value/reals.
    mc_gross_2=20.00
    mc_gross_3=10.00

    num_cart_items=3         # Integer
    option_selection1_1=Fire   # A dict of key/strings value/strings.
    option_selection1_2=PurpleIce
    option_selection1_3=sharkMonkey

    residence_country=CA
    txn_id=3MT24968PY143235R   # This did not correlate correctly when testing.
    payer_id=ZVNCWN7KV8GBQ     # This is the buyer.
    payment_date=16:07:53 Dec 15, 2016 PST  # A string, not date time field.

A dict of key/strings value/strings.
The user may want me to send to different emails.
    option_selection2_1=dpotschka11@gmail.com
    option_selection2_2=dpotschka11@gmail.com
    option_selection2_3=dpotschka11@gmail.com

A dict of key/strings, value/integers
    quantity1=1
    quantity2=1
    quantity3=1

    receiver_id=6S9JN4DKMU5SU    # This  is me
    payment_gross=50.00   # A real.
    receipt_id=4458-4457-7274-7131     # For credit card payers.


I will set this db up so that I have individual fields for:
    payer_email=dpotschka-buyer@yahoo.com  # Just use the first one in the list.
    payment_status=Completed           # For credit card payers.  Should equal 'Completed'
    payment_type=instant     # Credit card buyers don't get this.  Should equal 'instant'

    ipn_track_id=72c8be1bdfe10  # Send this to the customer.
    first_name=test
    last_name=buyer
    created

and all the data is also in one dictionary field called txn_info.
    """

# This data is in seperate fields so I have something to search if necessary.
    payer_email = models.EmailField(default = 'j@j.com')

    # Send this to the customer along with their order details.
    ipn_track_id = models.CharField(max_length=50, default = 'na')

    first_name = models.CharField(max_length=50, default = 'na')
    last_name  = models.CharField(max_length=50, default = 'na')
    created = models.DateTimeField('date_of_purchase', default=timezone.now())

# txn_info is a dict of all of the transaction information in JSON format.

    txn_info = fields.JSONField("transaction_info", default = txn_default)

    def __str__(self):

        return self.payer_email


@python_2_unicode_compatible  # For python 2 support.
class PaypalTestDB(models.Model):
# This data is in seperate fields so I have something to search if necessary.
    payer_email = models.EmailField(default = 'j@j.com')

    # Send this to the customer along with their order details.
    ipn_track_id = models.CharField(max_length=50, default = 'na')

    first_name = models.CharField(max_length=50, default = 'na')
    last_name  = models.CharField(max_length=50, default = 'na')
    created = models.DateTimeField('date_of_purchase', default=timezone.now())

# txn_info is a dict of all of the transaction information in JSON format.

    txn_info = fields.JSONField("transaction_info", default = txn_default)

    def __str__(self):

        return self.payer_email




