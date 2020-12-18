from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

# Used to check if the userName is in the db
from django.core.exceptions import ObjectDoesNotExist


myName = "http://www.thehyperdream.com/"


# This does nothing, I just used it for testing.
def index(request):
    return HttpResponse("Hello, world. You're at the sales index.")





# My ipnListener
# See here at paypal for  help:
# https://developer.paypal.com/docs/classic/ipn/integration-guide/IPNImplementation/

import requests

# I got this from:
# https://www.pythonanywhere.com/user/timetable/files/home/timetable/superDream/paypal/standard/ipn/views.py?edit
# There are other nice tidbits in there that you will need for this handler.
from django.http import QueryDict

from forms import SalesTestForm
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from .models import PaypalTestDB, PaypalDB, ClientDB
# PaypalTestDB is the same as PaypalDB.
# PaypalDB = payer_email, ipn_track_id, first_name, last_name, created, txn_info
# txn_info is a dict of all of the transaction information in JSON format.

# ClientDB has client_email, first_name, last_name, created


"""


WARNING:
Your sandbox account is scrambled, you tried to buy some art with one of
the sandbox visa numbers but your art.html was pointed at your live paypal.
paypal black listed your fake visa and now you cannot use it in the
sandbox I think.  I also deleted one of my sandbox accounts, dpotschka@yahoo.com.
I get an error message from paypal when I try to delete any of the other 3 accounts.
The software won't even allow me to enter the checkbox on two of the accounts,
that is normal you can't delete those.

Thanks for submitting your question. Use this reference number for follow up: #170109-000558
Responses to your inquiry will be sent from the PayPal email support@paypal-techsupport.com.
Please ensure that your email inbox is setup to receive emails from this address and check
your spam folders for responses when necessary.

If you need to update your question and you already have an account, log in,
click the Your Account tab, and select the question to open and update it.

Errors I get at paypal sandbox:
I created another sandbox account dpotschka11@gmail.com
When trying to verify it I get this error:
"Sandbox account you are trying to link is associated with another developer account."

They said don't make a fake account with dpotschka11@gmail.com

I'm logged into the developer account https://developer.paypal.com/developer/accounts/
with my dpotschka@yahoo password.
--


dpotschka-1@yahoo.com - when I try to delete this acccount I get this error:
"We're sorry, something went wrong during account deletion.  Some of the test
accounts you had selected may not have deleted.  Please try again."

When I put my cursor over the check box for the following accounts my cursor
changes into a red circle with a red line going through the circle:
dpotschka-facilitator@yahoo.com
dpotschka-buyer@yahoo.com
They told me you can't delete those two accounts.

I was able to successfully delete this account but I think that it is
still linked to the https://developer.paypal.com/developer/accounts?event=linkAccountAssociated
dpotschka@yahoo.com
dpotschka@yahoo.com is also my log in name for paypal as well, maybe that is where
the problem is?

The problem could also be that your buttons on art.html are linked to the old
dpotschka@yahoo.com sandbox merchant account.

I have created two more accounts:
dpotschkaMerchant@yahoo.com
dpotschkaBuyer@yahoo.com

I will try to reconfigure my buttons to snyc with those.

--



Classic test api credentials from my paypal sandbox:
https://developer.paypal.com/developer/accounts/

Classic TEST API Credentials


For the Business (Seller?) account.
Username:
dpotschka_api1.yahoo.com

Password:
EDE26KDBHB6D8XHZ

Signature:
Arnhf-KmFgPkXda2u8sfypVPGHhSAVKcT65TnUhfm.sM1-FL67GwNm1C

I also have an account (Business-Pro) so I can test credit card purchases.
Probably don't need this as I just did a credit card test and it went through.
Dec 14/16 4:10pm.
dpotschka-1@yahoo.com

----

For the facilitator  account.
Username:
dpotschka-facilitator_api1.yahoo.com

Password:
ZLAMH6J8ZVPG964Y

Signature:
A-FEKf0j25vkV6jbthfPjtVqOvTjA2uRousp7oMKCKo53Vy8VMGSyiuu
----

The fake credit card number in this one no longer works.
dpotschka-buyer@yahoo.com
4214 0262 9675 5795
expires: 01/22
csc: 454
--

Information about my fake buyer for testing in sandbox.
Email ID:
dpotschka11@gmail.com
This account is not verified.

password: phar....

Phone Number:
613-437-6831

Credit Card Number, visa:
4214 0229 4984 6875

expires: 01/22
csc: 454  I just made this up since they don't have it.
Bank Account
Account Number:


Routing Number:


"""

# ipn_track_id=a1a701f8ebfd8


# You must comment these next two out for "The first tester".
@require_POST
@csrf_exempt
def ipnListener(request):

    '''This module processes PayPal Instant Payment Notification messages (IPNs).
    '''

    VERIFY_URL_PROD = 'https://www.paypal.com/cgi-bin/webscr'
    VERIFY_URL_TEST = 'https://www.sandbox.paypal.com/cgi-bin/webscr'

    # Switch as appropriate
    VERIFY_URL = VERIFY_URL_PROD
    #VERIFY_URL = VERIFY_URL_TEST

    # CGI preamble
    #print("content-type: text/plain")
    #print()

    #if request == 'POST':
    if request.method == 'POST':

        """
After receiving the IPN message from PayPal, your listener returns an empty
HTTP 200 response to PayPal. Otherwise, PayPal resends the IPN message.
I do this at the bottom of this function.
        headers = {'status': '200 OK'}
        requests.post('https://www.sandbox.paypal.com/cgi-bin/webscr', headers=headers)

        """

        #r.raise_for_status
# Sends back the source code for their home page, buy paypal now etc.
        #return render(request, 'sales/salesTest.html', {'invalid': r.text})

        # I got QueryDict from paypal views.
        # NOTE: QueryDict will put all the values into a list.
        data = QueryDict(request.body).copy()
        #data = QueryDict(request.body, encoding=encoding).copy()

        #return render(request, 'sales/salesTest.html', {'data': data})

        """
returns:
<QueryDict: {u'option_selection1_2': [u'Hand'],
             u'option_selection1_1': [u'monkey'],
             u'last_name': [u'Potschka'],
             u'payment_status': [u'lkj'],
             u'first_name': [u'David'],
             u'payer_email': [u'dpotschka@yahoo.com'],
             u'option_selection2_1': [u'dpotschka@yahoo.com'],
             u'option_selection2_2': [u'dpotschka11@gmail.com'],
             u'csrfmiddlewaretoken': [u'izRl9mcqNyHrBwc2VuC3Kg0n5MizecqTojX2VVIXTAa5imw0qAimbgsWVK3jFSIm'],
             u'ipn_track_id': [u'7653'],
             u'payment_type': [u'instant']}>


You can access the values just like a regular dictionary:
data['first_name'] = David
        """

        # Read and parse query string
        #param_str = sys.stdin.readline().strip()
        #params = urllib.parse.parse_qsl(param_str)

        # Add '_notify-validate' parameter, paypal says put it first?
        #params.append(('cmd', '_notify-validate'))

        params = []
        params.append(('cmd', '_notify-validate',))
        for key, value in data.iteritems():
            item = (key, value,)
            params.append(item)

        #return render(request, 'sales/salesTest.html', {'params': params})


    # Post back to PayPal for validation
        headers = {'content-type': 'application/x-www-form-urlencoded', 'host': 'www.paypal.com'}
        r = requests.post(VERIFY_URL, params=params, headers=headers, verify=True)
        r.raise_for_status()

        #return render(request, 'sales/salesTest.html', {'params': params})

    # Check return message and take action as needed

        #The first tester.
        """
        if r.text == 'VERIFIED':
            return render(request, 'sales/salesTest.html', {'verified': r.text})
        elif r.text == 'INVALID':
            return render(request, 'sales/salesTest.html', {'invalid': r.text})
        else:
            return render(request, 'sales/salesTest.html', {'know': 'did not work'})
        """

        """
        #The second tester.
        if r.text == 'VERIFIED':
            worked = PaypalTestDB(payment_date='Yea', payment_status='Yea', first_name='Yea', last_name='Yea', payer_email='Yea')
            worked.save()
        elif r.text == 'INVALID':
            # You cannot iteritems over a QueryDict object.
            data2 = dict(data)
            sendProduct(data2)

            return render(request, 'sales/salesTest.html', {'know': data2})
            #worked = PaypalTestDB(payment_date='Yea2', payment_status='Yea2', first_name='Yea2', last_name='Yea2', payer_email='Yea2')
            #worked.save()
        else:
            worked = PaypalTestDB(payment_date='Yea3', payment_status='Yea3', first_name='Yea3', last_name='Yea3', payer_email='Yea3')
            worked.save()
        """



        # the final
        if r.text == 'VERIFIED':

            loadPaypalDB(data)
            loadClientDB(data)

# paypal is screwing up and sending multiple IPN's for the same transaction, this will
# cause this code to send the product over and over again, patch it up.  I changed the
# HttpResponse(status=200) (below) from 204 too 200, but I havn't tested it yet with real money.

            if data['payment_type']=='instant' or data['payment_status']=='Completed':
                # You cannot iteritems over a QueryDict object.
                data2 = dict(data)
                #ERROR: I removed this as the 200 code isnt getting to paypal.
                # Put it back in once you fix that ipn crap.
                result = sendProduct(data2)

                # For testing
                #return render(request, 'sales/salesTest.html', {'know': result})

            else:
                # Email me and tell me that a clients cheaque hasn't cleared yet.
                # I will send them the product by hand.

                #ERROR: I removed this as the 200 code isnt getting to paypal.
                # Put it back in once you fix that ipn crap.
                data2 = dict(data)

                #pendingPayment(data2)

        elif r.text == 'INVALID':

            """
            # Testing r.text=='VALID' locally, you have to do it from this 'INVALID' BLOCK.

            loadPaypalDB(data)

            if data['payment_type']=='instant' or data['payment_status']=='Complete':
                # You cannot iteritems over a QueryDict object.
                data2 = dict(data)
                result = sendProduct(data2)

                # For testing
                return render(request, 'sales/salesTest.html', {'know': result})

            else:
                # Email me and tell me that a clients cheaque hasn't cleared yet.
                # I will send them the product my hand.
                data2 = dict(data)
                pendingPayment(data2)

            """

            # Load the PaypalTestDB with the invalid data to see what is going on.
            loadPaypalTestDB(data)

        else:
            # Load the PaypasTestDB with the invalid data to see what is going on.
            loadPaypalTestDB(data)



    # Paypal expects this or they will continue to send the ipn.
    # Try moving this line up to the top of this def if you still get
    # multiple IPN requests for the same order.
    return HttpResponse(status=200)

    #return HttpResponse('<h1>dave was here</h1>')

    #return HttpResponse(200)

    #return '', 200
    #return HttpResponse(status=200)

    # This might only work in the sandbox.  A 204 means everything is ok and no data was sent.
    #return HttpResponse(status=204)

    #return HttpResponse("Hello, world. You're at the ipnListener.  This is a stub so an error message is not returned.")


####################### End def ipnListener


"""
    #The rest of this code is for testing.
    else:  # Display the form for testing.

    # NOTE:  Anyone can trigger this ipnListener by typing it in the address bar.
    # Actually I tried that and it no longer gets here when you do that, must be those decorators.
        #worked = PaypalTestDB(payment_date='Yea4', payment_status='Yea4', first_name='Yea4', last_name='Yea4', payer_email='Yea4')
        #worked.save()

        form = SalesTestForm()
# This is outside the first 'if block' in case the form is not valid.
        return render(request, 'sales/salesTest.html', {'form': form})


    return HttpResponse("Hello, world. You're at the ipnListener.  This is a stub so an error message is not returned.")

"""



# PaypalTestDB is now the same as PaypalDB.
# PaypalDB = payer_email, ipn_track_id, first_name, last_name, created, txn_info
# txn_info is a dict of all of the transaction information in JSON format.

from django.core.mail import EmailMessage
import re
import os


def sendProduct(data):
    """
    Get the items and email address's, and email them to the client.
    email the client the invoice.
    """

    artNameAndEmail = []

    for key, value in data.iteritems():

        # Put the product name and associated email address into a tuple then
        # put that tuple in a list, I made the names of the art the
        # same as the directory that they are located in.
        # The name of the art keys start with this "option_selection1_ " then a number.

        # The email keys start with this "option_selection2_ " then a number.
        # I am now using data['payer_email'] as the email address.

        if re.match('option_selection1_', key):  # The value is the artsName.

# NOTE: QueryDict will put all the values into a list.
# The dict is scrambling the order and your artName and it's
# associated email address aren't lining up for your tuple list.  So...

            #lastDigit = key[-1]
            email = data['payer_email'][0]
            #email = data['option_selection2_' + lastDigit][0]

            tupleIt = (value[0], email,)
            artNameAndEmail.append(tupleIt)

    #return artNameAndEmail
# returns:
# [(u'Hand', u'dpotschka11@gmail.com'), (u'monkey', u'dpotschka@yahoo.com')]


    """
>>> x = [1, 2, 3]
>>> y = [4, 5, 6]
>>> zipped = zip(x, y)
>>> zipped
[(1, 4), (2, 5), (3, 6)]
>>> x2, y2 = zip(*zipped)
>>> x == list(x2) and y == list(y2)
True
    """

    """
    Getting the art and book.

mail = EmailMessage(subject, text, ['from EMAIL_ADDRESS'], [to email])
mail.attach(image.name, image.read(), image.content_type)
mail.send()

For help see your bookmarks at folder:
pythonAnyWhere/get files django attach email.
https://docs.djangoproject.com/en/1.10/ref/files/file/


I think file_object is the path from the media root.
image = File(file_object)

The name of the file including the relative path from MEDIA_ROOT.
image.name

image.read(num_bytes=None)
Read content from the file. The optional size is the number of bytes to read;
if not specified, the file will be read to the end.

    """

# artNameAndEmail looks like this for two purchases of art:
# [(u'Hand', u'dpotschka11@gmail.com'), (u'monkey', u'dpotschka@yahoo.com')]
    for client in artNameAndEmail:

        content = 'artNameAndEmail: ' + str(client)

# client[0] is the directory of the art and client[1] is where the email
# is being sent to, the clients email address.  There are two images in each folder.
# I am sending one email for every two images in the directory.

        folder = '/home/timetable/superDream/myDream/static/myDream/theArt/' + client[0]

# walkData is a tuple (dirpath, dirnames, filenames).  They are lists of strings.
# And the order in the tuple is (dirpath, dirnames, filenames).  os.walk will also
# get the folders below your target folder.  I don't have any directores below the target folder.
# walkData looks like this (['dirPath1', 'dirPath2'], ['dirName1', 'dirName2'], ['fileName1', 'fileName2'])
        walkData = os.walk(folder)
        twoImages = []
        for dirPath, dirNames, fileNames in walkData:
            sendTwoEmails = False  # Your two mountains (4 images) are to large to email together.
            for fn in fileNames:

                image = folder + '/' + fn
                twoImages.append(image)
                if fn == 'firstFrostForest.jpg':
                    sendTwoEmails = True

        mail = EmailMessage(
    # Title of the email.
                    "Thank You for your Order - see attached files!",

    # The clients invoice and letter from me.
                    content + """

                    %s

                    Thank You for your order!

                    Cheers,

                        Dave

                    dave@theHyperDream.com
                    """ %('ipn_track_id = ' + data['ipn_track_id'][0]),

    # The email is from me.
                    'dave@thehyperdream.com',

    # The email is being sent to the client.
                    [client[1]],

    # This header is for when I click on reply at my hyperdream account, I reply to the
    # clients email when I send them the product.
                    headers = {'Reply-To': 'dave@thehyperdream.com' }
                )

        image1 = twoImages[0]
        image2 = twoImages[1]
        mail.attach_file(image1)
        mail.attach_file(image2)

        book = '/home/timetable/superDream/myDream/static/myDream/books/motivate/MotivateAnyone.pdf'
        mail.attach_file(book)

        mail.send()

# CAUTION:  You can only send max email size to yahoo of 40mb.  Your mountain pictures
# with the book are about 47mb.  You will have to send two emails.

        if sendTwoEmails:

            mail2 = EmailMessage(
    # Title of the email.
                    "Extra Mountains!  Thank You for your Order - see attached files!",

    # The clients invoice.
                    """
                    Thank You for your order!

                    %s

                    Here are the free extra mountains
                    Frost No Rose

                    Cheers,

                        Dave

                    dave@theHyperDream.com
                    """%('ipn_track_id = ' + data['ipn_track_id'][0]),

    # The email is from me.
                    'dave@thehyperdream.com',

    # The email is being sent to the client.
                    [client[1]],

    # This header is for when I click on reply at my hyperdream account, I reply to the
    # clients email when I send them the product.
                    headers = {'Reply-To': 'dave@thehyperdream.com' }
                )

            frostNoRose = '/home/timetable/superDream/myDream/static/myDream/theArt/frostNoRose/FrostNoRose.jpg'
            frostNoRose2x = '/home/timetable/superDream/myDream/static/myDream/theArt/frostNoRose/FrostNoRose2x.jpg'
            mail2.attach_file(frostNoRose)
            mail2.attach_file(frostNoRose2x)

            mail2.send()


    mailMe = EmailMessage(
    # Title of the email.
                    "Dave somebody bought some art, Yea!",

    # My message to me.
                    "Yea Dave, people like my book!",

    # The email is from me.
                    'dave@thehyperdream.com',

    # The email is being sent to me.
                    ['dave@thehyperdream.com'],

    # This header is for a reply.  Don't need to reply to myself ha ha.
                    headers = {'Reply-To': 'dave@thehyperdream.com' }
                )

    mailMe.send()

    # For Testing
    return twoImages
    #return folder
    #return artNameAndEmail


def loadClientDB(data):

# This code works but it loads duplicate emails if the user or paypal emails me more than once.
    """
    client = ClientDB(client_email = data['payer_email'], first_name = data['first_name'],\
    last_name = data['last_name'])
    client.save()
    """
    # This will be the new way to do this part once I get the sandbox working again so I can test it.
    # First check to see if the clients email is already in the db.  Don't save it
    # everytime they make a purchase or everytime paypal screws up and resends an IPN.
    # This code is similar to /myDream/davesHappyFamily/signPost.py file.

# This code works in /smallHandlers.py def contact(request):
    try:
        ClientDB.objects.get(client_email = data['payer_email'])
    except ObjectDoesNotExist:
        client = ClientDB(client_email = data['payer_email'], first_name = data['first_name'],\
        last_name = data['last_name'])
        client.save()

# Comment out this code if the code above works first.  Then open up
# the code below this one to load the loadPaypalDB.  You will have to wait for an order for
# one of your dvd/s to come through.  Also try moving the 200 response to the top of the
# def ipnListener.
def loadPaypalDB(data):
    purchase = PaypalDB(payer_email = data['payer_email'], ipn_track_id = data['ipn_track_id'],\
                        first_name = data['first_name'], last_name = data['last_name'],\
                        txn_info = data)
    purchase.save()

    """
    # This will be the new way to do this part once I get the sandbox working again so I can test it.
    # First check to see if the ipn_track_id is already in the db.  Don't save it
    # everytime paypal screws up and resends an IPN.
    # This code is similar to /myDream/davesHappyFamily/signPost.py file.

    try:
        PaypalDB.objects.get(ipn_track_id = data['ipn_track_id'])
    except ObjectDoesNotExist:
        purchase = PaypalDB(payer_email = data['payer_email'], ipn_track_id = data['ipn_track_id'],\
                        first_name = data['first_name'], last_name = data['last_name'],\
                        txn_info = data)
        purchase.save()

    """


def loadPaypalTestDB(data):
    purchase = PaypalTestDB(payer_email = data['payer_email'], ipn_track_id = data['ipn_track_id'],\
                        first_name = data['first_name'], last_name = data['last_name'],\
                        txn_info = data)
    purchase.save()




def pendingPayment(data):
    """ If the client uses a check and it hasn't cleared yet...
        Just send myself the clients ipn_track_id and their payer_email,
        I can check the db after to send them the product by hand.
    """

    product = []
    for key, value in data.iteritems():
        if re.match('option_selection1_', key):  # The value is the artsName.
            product.append(value[0])

    content = 'ipn_track_id: ' + data['ipn_track_id'][0] + ', payer_email: ' + data['payer_email'][0] + " " + str(product)

# WARNING:  You can only send max email size to yahoo of 40mb.  Your mountain pictures
# with the book are about 47mb.  You will have to send two emails.

    email = EmailMessage(
# Title of the email.
                "Dave, client payed by check, waiting for clearence!",

# The clients ipn_track_id and email address.
                content,

# The email server is me.
                'dave@thehyperdream.com',

# The email is being sent to me.
                ['dave@thehyperdream.com'],

# This header is for when I click on reply at my hyperdream account, I reply to the
# clients email when I send them the product.
                headers = {'Reply-To': data['payer_email'][0] }
            )
    email.send()


########################## End def pendingPayment()


    # Fields for a buyer who is using a Paypal account or credit card
    # to make their purchase.  This is an example of someone who bought 3 items.
    # I have stripped out the stuff I don't need, although I save everything in the db.

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
    txn_id=3MT24968PY143235R
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
    ipn_track_id=72c8be1bdfe10
    receipt_id=4458-4457-7274-7131     # For credit card payers.

I will set this db up so that I have individual fields for:
    payer_email=dpotschka-buyer@yahoo.com
    payment_status=Completed           # For credit card payers.  Should equal 'Completed'
    payment_type=instant     # credit card buyers don't get this.  Should equal 'instant'

    first_name=test
    last_name=buyer
    created

and all the data is also in one dictionary.
    """

"""

My seventh test, more than one item and the buyer is using their
paypal account to buy the goods.  Again this ID is incorrect.
Your transaction ID for this payment is: 3U790843KF891290B.

mc_gross=50.00
&protection_eligibility=Ineligible
&item_number1=
&tax=0.00
&item_number2=
&payer_id=ZVNCWN7KV8GBQ
&item_number3=
&payment_date=16:07:53 Dec 15, 2016 PST
&option_name2_1=Email for delivery required
&option_name2_2=Email for delivery required
&option_name2_3=Email for delivery required
&option_selection1_1=Fire
&payment_status=Completed
&option_selection1_2=PurpleIce
&option_selection1_3=sharkMonkey
&charset=windows-1252
&mc_shipping=0.00
&mc_handling=0.00
&first_name=test
&mc_fee=1.75
&notify_version=3.8
&custom=
&payer_status=verified
&business=dpotschka@yahoo.com
&num_cart_items=3
&mc_handling2=0.00
&mc_handling3=0.00
&verify_sign=ARyNDMbKwa-zLx7AtfPa-etrhyTVAIQnb6s7EwjR8.DulozkPOxedphZ
&payer_email=dpotschka-buyer@yahoo.com
&mc_shipping1=0.00
&mc_shipping2=0.00
&mc_shipping3=0.00
&tax1=0.00
&tax2=0.00
&tax3=0.00
&option_name1_1=acquiring
&option_name1_2=acquiring
&option_name1_3=acquiring
&txn_id=3MT24968PY143235R
&payment_type=instant
&option_selection2_1=dpotschka11@gmail.com
&last_name=buyer
&option_selection2_2=dpotschka11@gmail.com
&item_name1=DavesShoppingItemName
&receiver_email=dpotschka@yahoo.com
&option_selection2_3=dpotschka11@gmail.com
&item_name2=DavesShoppingItemName
&payment_fee=1.75
&item_name3=DavesShoppingItemName
&quantity1=1
&quantity2=1
&receiver_id=6S9JN4DKMU5SU
&quantity3=1
&txn_type=cart
&mc_gross_1=20.00
&mc_currency=USD
&mc_gross_2=20.00
&mc_gross_3=10.00
&residence_country=CA
&test_ipn=1
&transaction_subject=
&payment_gross=50.00
&ipn_track_id=72c8be1bdfe10


--

My Sixth test is for a buyer with a paypal account and using the 'view cart button'.
Your transaction ID for this payment is: 6GA87296JC894493X.
--

My fifth test for visa, using view cart button.
Your receipt number for this payment is: 2660-7887-8679-1662.
That matches the receipt number in the ipn.
--


My forth test:
ID for this payment is: 47H32015PD1353933.
I still do not see the ID in this test either.
--


My third test is for a buyer with a paypal account.  Paypal returns
this transaction ID for this payment is: 3U8427297S3088528,
to the buyer.  Yet I do not see it below.  And no receipt Id either.

mc_gross=140.00
&protection_eligibility=Ineligible
&item_number1=
&tax=0.00
&payer_id=ZVNCWN7KV8GBQ
&payment_date=14:31:33 Dec 15, 2016 PST
&option_name2_1=Email for delivery required
&option_selection1_1=Ingrid
&payment_status=Completed
&charset=windows-1252
&mc_shipping=0.00
&mc_handling=0.00
&first_name=test
&mc_fee=4.36
&notify_version=3.8
&custom=
&payer_status=verified
&business=dpotschka@yahoo.com
&num_cart_items=1
&mc_handling1=0.00
&verify_sign=Ai4qGBvHMY6.1Qfr5VRqWjAV6GXSAODQQV0Yn2HwrnS7KYXfpYjceg4e
&payer_email=dpotschka-buyer@yahoo.com
&mc_shipping1=0.00
&tax1=0.00
&option_name1_1=acquiring
&memo=I love you Dave
&txn_id=8SS95922LD055025H
&payment_type=instant
&option_selection2_1=dpotschka11@gmail.com
&last_name=buyer
&item_name1=DavesShoppingItemName
&receiver_email=dpotschka@yahoo.com
&payment_fee=4.36
&quantity1=1
&receiver_id=6S9JN4DKMU5SU
&txn_type=cart
&mc_gross_1=140.00
&mc_currency=USD
&residence_country=CA
&test_ipn=1
&transaction_subject=
&payment_gross=140.00
&ipn_track_id=ebebc3c8800e


My second ipn test message for visa:
This is for the 'add to cart button', I bought 3 items, jewel, Rashida, glowlyswirl.
Paypal returns the reciept number to the buyer as confirmation.

first_name=David Potschka
&mc_shipping=0.00
&mc_currency=USD
&payer_status=unverified
&payment_fee=6.97
&payment_gross=230.00
&txn_type=cart
&num_cart_items=3
&mc_handling=0.00
&verify_sign=AQU0e5vuZCvSg-XJploSa.sGUDlpAYBaE4uwtqG-E.FvjSOqHDTlI4Qw
&payer_id=4CF6EQ5TCA9FN
&option_selection2_1=dpotschka11@gmail.com    # Where they shall be delivered.
&option_selection2_2=dpotschka11@gmail.com
&option_selection2_3=dpotschka11@gmail.com
&charset=windows-1252&tax1=0.00
&receiver_id=6S9JN4DKMU5SU
&tax2=0.00
&tax3=0.00
&mc_handling1=0.00
&mc_handling2=0.00
&mc_handling3=0.00
&item_name1=DavesShoppingItemNam
&tax=0.00
&item_name2=DavesShoppingItemName
&item_name3=DavesShoppingItemName
&payment_type=instant
&mc_shipping1=0.00
&mc_shipping2=0.00
&mc_shipping3=0.00
&txn_id=4VF67501YE864604
&mc_gross_1=10.00
&quantity1=1
&mc_gross_2=140.00
&quantity2=1
&item_number1=
&protection_eligibility=Ineligible
&mc_gross_3=80.00
&quantity3=1&item_number2=
&item_number3=
&custom=
&option_selection1_1=Jewel       # The names of the paintings.
&option_selection1_2=Rashida
&business=dpotschka@yahoo.com
&option_selection1_3=glowySwirl
&residence_country=CA
&last_name=ytre
&payer_email=dave@thehyperdream.com
&option_name2_1=Email for delivery required
&option_name2_2=Email for delivery required
&option_name2_3=Email for delivery required
&payment_status=Completed
&payment_date=20:48:23 Dec 14, 2016 PST
&transaction_subject=
&receiver_email=dpotschka@yahoo.com
&mc_fee=6.97&notify_version=3.8
&receipt_id=4458-4457-7274-7131
&mc_gross=230.00&test_ipn=1
&option_name1_1=acquiring
&option_name1_2=acquiring
&option_name1_3=acquiring
&memo=I love you so much Dave!
&ipn_track_id=f1a7498ac0fdd

----



My First ipn test message for visa:
This is for a single "buy Now" button where you can only buy one item at a time.
Paypal returns the reciept number to the buyer as confirmation.

mc_gross=10.00
&protection_eligibility=Ineligible
&payer_id=4CF6EQ5TCA9FN
&tax=0.00
&payment_date=19:05:25 Dec 14, 2016 PST
&payment_status=Completed
&charset=windows-1252
&first_name=Jjjjjjjjjj              # The persons first name.
&option_selection1=gimpy1        # The name of the painting.
&mc_fee=0.59
&notify_version=3.8
&custom=
&payer_status=unverified
&business=dpotschka@yahoo.com
&quantity=1
&verify_sign=AwD4sJJmdrzDKNGw7KMAMuZSx1AHAADAfOUKtHGxe3zoG.5au2wnRVIx
&payer_email=dave@thehyperdream.com            # The buyers email address.
&option_name1=davesDropDownName
&memo=I love Dave
&txn_id=6F745253UU0984410
&payment_type=instant
&last_name=kjhg                          # The buyers last name.
&receiver_email=dpotschka@yahoo.com
&payment_fee=0.59
&receiver_id=6S9JN4DKMU5SU
&txn_type=web_accept
&item_name=testArt
&mc_currency=USD&item_number=
&residence_country=CA
&test_ipn=1
&receipt_id=0518-0568-4085-6022        # This is what the buyer gets.
&handling_amount=0.00
&transaction_subject=
&payment_gross=10.00
&shipping=0.00
&ipn_track_id=bd1d9d49ee746




NOTES about the ipn listener example from paypal.

First I have the original code then I add notes to the original code.



+#!/usr/bin/python

'''This module processes PayPal Instant Payment Notification messages (IPNs).
'''

import sys
import urllib.parse
import requests

VERIFY_URL_PROD = 'https://www.paypal.com/cgi-bin/webscr'
VERIFY_URL_TEST = 'https://www.sandbox.paypal.com/cgi-bin/webscr'

# Switch as appropriate
VERIFY_URL = VERIFY_URL_TEST

# CGI preamble
print("content-type: text/plain")
print()

# Read and parse query string
param_str = sys.stdin.readline().strip()
params = urllib.parse.parse_qsl(param_str)

# Add '_notify-validate' parameter
params.append(('cmd', '_notify-validate'))

# Post back to PayPal for validation
headers = {'content-type': 'application/x-www-form-urlencoded', 'host': 'www.paypal.com'}
r = requests.post(VERIFY_URL, params=params, headers=headers, verify=True)
r.raise_for_status()

# Check return message and take action as needed
if r.text == 'VERIFIED':
    pass
elif r.text == 'INVALID':
    pass
else:
    pass

########################## End Original code.



#!/usr/bin/python


'''
    This is an IPN listener.
    This module processes PayPal Instant Payment Notification messages (IPNs).
'''

# PAYPAL will send IPNs to:
# http://www.frogTransactions.appspot.com/ipn-code-samples-master/python/paypal_ipn.py
# You can view your IPNs on the IPN History page.
# If necessary, you can resend IPN messages from that page:
# https://www.paypal.com/ca/cgi-bin/webscr?cmd=_display-ipns-history

# See here for more details:
# https://developer.paypal.com/docs/classic/ipn/ht_ipn/

# Here is what most of that page above says:

# To receive and process IPN messages:
#
# Create a listener that:
#
# Receives an IPN message sent from PayPal.
# Confirms to PayPal that the message was received.
# Verifies that it is a valid IPN message using the request-response handshaking required by PayPal.
# Processes the IPN messages according to your needs.

#
# Capture the IPN messages that PayPal sends to your listener
#
# After receiving an IPN message from PayPal, you must respond to PayPal with
# a POST message that is an exact copy of the received message but
# with "cmd=_notify-validate" added to the end of the message.

# When PayPal receives your POST message, it sends a message back to your
# listener to indicate the validity of the initial notification.
# PayPal's message has an HTTP status code of 200 and a body that contains either
# VERIFIED or INVALID.

# Parse the message for information on the transaction referenced by the IPN,
# the type of notification sent, and the associated transaction status. Take the
# appropriate action(s) based on the notification received.

# Log in to your PayPal business account and specify the Notification URL to your IPN
# listener. For detailed instructions about how to specify the Notification URL,
# see Identifying your IPN listener to PayPal. As an example, the web server
# where you host a PHP listener might resemble the following URL:
#
# http://www.example.com/ipnListener/paypal_ipn.py
# mine is:
# http://www.frogTransactions.appspot.com/ipn-code-samples-master/python/paypal_ipn.py
# You can view your IPNs on the IPN History page.
# If necessary, you can resend IPN messages from that page:
# https://www.paypal.com/ca/cgi-bin/webscr?cmd=_display-ipns-history


# In addition to enabling the IPN service and setting the Notification URL
# location through your PayPal account, you can also set the location using
# the NOTIFYURL parameter in an API call. By dynamically setting the Notification
# URL, you can set up different listeners for different needs (such as
# if you are supporting different merchant sites with a single PayPal account).

# PayPal sends IPN messages for every type of transaction or transaction status
# update (including payment and subscription notifications), and each notification
# type contains a unique set of fields. You need to configure your listener to
# handle the fields for every type of IPN message you might receive,
#
# depending on the types of PayPal transactions you support. For a complete guide
# on the different types of IPN messages and the data fields associated with
# each type, see the IPN Integration Guide:
# https://developer.paypal.com/docs/classic/ipn/integration-guide/IPNIntro/

# Consider the following processes in your notification handler to properly direct
# the notifications and to guard against fraud:
#
# Use the Transaction ID value to ensure you haven't already processed the notification.
# Confirm the status of the transaction, and take proper action depending on value.
# For example, payment response options include Completed, Pending, and Denied.
# Don't send inventory unless the transaction has completed!
#
# Validate the e-mail address of the receiver.
# Verify the item description and transaction costs with those listed on your website
# and catalog.
# Use the values of txn_type or reason_code of a VERIFIED notification to determine your
# processing actions.




import sys


#ImportError: No module named parse, I couldn't fine it either.

import urllib.parse


# http://docs.python-requests.org/en/master/user/quickstart/#make-a-request
# Uses sockets, must have billing enabled.

import requests


# For production.

VERIFY_URL_PROD = 'https://www.paypal.com/cgi-bin/webscr'


# For testing in the sandbox.

VERIFY_URL_TEST = 'https://www.sandbox.paypal.com/cgi-bin/webscr'


# Switch as appropriate to one of the above.

VERIFY_URL = VERIFY_URL_TEST


# CGI preamble

print("content-type: text/plain")
print()



# Receives an IPN message sent from PayPal.
# Read and parse query string

param_str = sys.stdin.readline().strip()
params = urllib.parse.parse_qsl(param_str)


# After receiving an IPN message from PayPal, you must respond to PayPal with
# a POST message that is an exact copy of the received message but
# with "cmd=_notify-validate" added to the end of the message.


# Add '_notify-validate' parameter

params.append(('cmd', '_notify-validate'))


# Post back to PayPal for validation

headers = {'content-type': 'application/x-www-form-urlencoded', 'host': 'www.paypal.com'}


# This line sends the message back to paypal.  I read in the docs somewhere
# that you must use https to send this.  If so TEST this stuff by sending
# messages back and forth from whatdoesthefroggot to frogtransactions.

r = requests.post(VERIFY_URL, params=params, headers=headers, verify=True)


# IMPORTANT:  Paypal expects the post within 30 seconds so save the original
# message after the above post statement ie Do Your db stuff in the "if block below".
# use the params var above for the data.

# When PayPal receives your POST message, it sends a message back to your
# listener to indicate the validity of the initial notification.
# PayPal's message has an HTTP status code of 200 and a body that contains either
# VERIFIED or INVALID.

# PayPal sends a single word back - either VERIFIED (if the message matches
# the original) or INVALID (if the message does not match the original).

r.raise_for_status()


# Check return message and take action as needed.
# I guess you call a handler from here to load an html page telling the user it is ok
# to download their art etc.  Load stuff into a db so you can access it later.

# Important: After you have authenticated an IPN message (received a VERIFIED response from
# PayPal), you must perform these important checks before you can assume that the IPN is
# both legitimate and has not already been processed:
# Check that the payment_status is Completed.
#
# If the payment_status is Completed, check the txn_id (transaction id)
# against the previous PayPal
# transaction that you processed to ensure the IPN message is not a duplicate.
# Check that the receiver_email is an email address registered in your PayPal account.
# Check that the price (carried in mc_gross) and the currency (carried in mc_currency)
#
# are correct for the item (carried in item_name or item_number).
# Once you have completed these checks, IPN authentication is complete. Now, you
# can update your database with the information provided and initiate any back-end
# processing that's appropriate.

if r.text == 'VERIFIED':
    pass
elif r.text == 'INVALID':
    pass
else:
    pass



# IPN Simulator
#
# Because the most complex part of implementing and IPN solution is creating your
# listener, PayPal provides templates and examples of listener code to help you. And to
# help you in testing your listener code, PayPal provides an IPN Simulator tool
# that you can use to send test IPN messages to the URL at which your listener
#
# is running. The IPN Simulator tool lets you verify that your listener is receiving IPN
# messages and handling them correctly. IPN Simulator notifications include a test_ipn
# variable, which is not found in live IPN messages, so the IPN test messages can be
# distinguished from the real IPN messages.
#
# See IPN Simulator for details on using the IPN Simulator.
#
# https://developer.paypal.com/docs/classic/ipn/integration-guide/IPNSimulator/


# Passing Custom Data
#
# The custom variable is a pass-through variable that allows you to pass your own custom
# data to PayPal, and pass it back to your listener. For example, you may want to
# pass a user ID and/or part number with your payment call or PayPal button.
# This variable allows you to pass that data to PayPal with the payment API
#
# call or button click when your customer leaves your website and goes to PayPal to
# make a payment. Then when the payment is processed, the IPN sends that data
# back to the listener page, so that on a successful payment, the listener page has
# the payment status from the IPN values, along with the user ID for the customer that
# made the purchase, and the part number of the item that was paid for.
#
# The custom variable is ignored by PayPal and is never presented to your customer,
# it's simply passed to PayPal and then back to your listener. There is only
# one custom variable accepted by the IPN, however, if you need to have multiple
# variables passed through, as in the case of a user ID and a part number,
#
# you can use a delimiter, such as a comma, to split the custom variable into multiple
# values. Then, on the listener page, you can parse the value of the custom variable
# based on the delimiter, to retrieve each of the separate individual values that you need.
#
# Note: The length of the custom variable is limited to 256 characters.
# For example, if you are using PayPal buttons, in the button form code, you just
# need to add an extra hidden input form variable to set a value for the custom variable.
#
# <input type="hidden" name="custom" value="[UserID],[PartNumber]"/>



# Other important notes from:
# https://developer.paypal.com/docs/classic/ipn/integration-guide/IPNIntro/


# The IPN message service does not assume that your listener will receive
# all IPN messages. Because the Internet is not 100% reliable, IPNs can
# get lost or be delayed. To address these issues, the IPN message service
# includes a retry mechanism that re-sends a message at various intervals until
#
# your listener acknowledges receipt. An IPN message may be present up to four
# days after the original was sent. The maximum number of retries is 15.

# This resend algorithm can lead to situations in which PayPal re-sends an IPN
# message at the same time you are sending back the original message.
# In this case, you should send your response again, to address the possibility that
# PayPal did not receive your first response. You must also ensure that you do
# not process the transaction associated with an IPN message twice.
# Use a try accept block davee.

# The IPN message service is not a real-time service. As a result, your
# listener may not receive an IPN message for many seconds after an event occurs.
# As a result, your checkout flow should not depend upon receiving an IPN message
# to complete. If it does, your checkout flow will be slow during periods of heavy
# system load and complicated, since it must handle retries.

# Supplement your IPN with Payment Data Tranfere (PDT); THIS only sends one message
# but it is in real time.
# You can use IPN with other notification mechanisms. For example,
# you can use Payment Data Transfer (PDT) or the API to obtain

# real-time information about a transaction and let IPN notify you of
# any changes after the transaction occurs.

# Every IPN message you receive from PayPal includes a User-Agent HTTP
# request header whose value is PayPal IPN ( https://www.paypal.com/ipn ).
# Do not use this header to verify that an IPN really came from PayPal and
# has not been tampered with.

# After PayPal verifies an IPN, your listener or administrative software should make
# these additional checks:
#
# Verify that you are the intended recipient of the IPN message. To do this, check
# the email address in the message. This check prevents another merchant from
# accidentally or intentionally using your listener.
#
# Verify that the IPN is not a duplicate. To do this, save the transaction ID and
# last payment status in each IPN message in a database and verify that the current
# IPN's values for these fields are not already in this database.
#
# Note: You can't rely on transaction ID alone to screen out duplicates,
# as this scenario shows:
# 1) PayPal sends you an IPN notifying you of a pending payment.
# 2) PayPal later sends you a second IPN telling you that the payment has completed.
# However, both IPNs contain the same transaction ID; therefore, if you were using
# just transaction ID to identify IPNs, you would to treat the
#
# "completed payment" IPN as a duplicate.
# Ensure that you receive an IPN whose payment status is "completed" before shipping
# merchandise or enabling download of digital goods. Because IPN messages can be sent
# at various stages in a transaction's progress, you must wait for the IPN whose
# status is "completed' before handing over merchandise to a customer.
#
# Verify that the payment amount in an IPN matches the price you intend to
# charge. If you do not encrypt your button code, it's possible for someone to
# capture a button-click message and change the price it contains. If you
# don't check the price in an IPN against the real price, you could accept a lower
# payment than you want.



#####


# Using a different listener.

# If you enable the IPN service, PayPal sends messages to the IPN listener at
# the URL you specify in your account profile. If you want, you can override
# this URL in order to associate a different IPN listener with a specific transaction.
# To do this, you can either:
#
# Specify the URL of a different listener in your definition of a PayPal Payment
# Standard button or Pass the URL of a different listener to a call of a PayPal API operation.
# Maybe something like this davee <input type="hidden" name="cmd" value="_cart">
# You will have to look up the correct name and value should be the url to the listener.


####


# A list of variables sent with an IPN and PDT:
# https://developer.paypal.com/docs/classic/ipn/integration-guide/IPNandPDTVariables/

# An example:

# Variable             Notes
#
# Information about you:

# receiver_email = gm_1231902686_biz@paypal.com    Check email address to make sure that this is not a spoof
# receiver_id = S8XGHLYDW9T3S
# residence_country = US

# Information about the transaction:

# test_ipn = 1    Testing with the Sandbox
# transaction_subject =
# txn_id = 61E67681CH3238416    Keep this ID to avoid processing the transaction twice
# txn_type = express_checkout    Type of transaction

# Information about your buyer:

# payer_email = gm_1231902590_per@paypal.com
# payer_id = LPLWNMTBWMFAY
# payer_status = verified
# first_name = Test
# last_name = User
# address_city = San Jose
# address_country = United States
# address_state = CA
# address_status = confirmed
# address_country_code = US
# address_name = Test User
# address_street = 1 Main St
# address_zip = 95131

# Information about the payment:

# custom =    Your custom field
# handling_amount = 0.00
# item_name =
# item_number =
# mc_currency = USD
# mc_fee = 0.88
# mc_gross = 19.95
# payment_date = 20:12:59 Jan 13, 2009 PST
# payment_fee = 0.88
# payment_gross = 19.95
# payment_status = Completed    Status, which determines whether the transaction is complete
# payment_type = instant    Kind of payment
# protection_eligibility = Eligible
# quantity = 1
# shipping = 0.00
# tax = 0.00

# Other information about the transaction:

# notify_version = 2.6    IPN version; can be ignored
# charset = windows-1252
# verify_sign = AtkOfCXbDm2hu0ZELryHFjY-Vb7PAUvS6nMXgysbElEn9v-1XcmSoGtf



##################


# Some Notes about using the IPN simulator.

# https://developer.paypal.com/docs/classic/ipn/integration-guide/IPNSimulator/

# To use the IPN simulator, you must be logged into the PayPal Developer site,
# and your listener must be running at your notification URL on your web server.



"""












