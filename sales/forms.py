from django import forms



# This form contains all possible vars from paypal for IPN.

""" The db need this
payer_email = models.EmailField(default = 'j@j.com')

    # Send this to the customer along with their order details.
    ipn_track_id = models.CharField(max_length=50, default = 'na')

    first_name = models.CharField(max_length=50, default = 'na')
    last_name  = models.CharField(max_length=50, default = 'na')
    created = models.DateTimeField('date_of_purchase', default=timezone.now())

# txn_info is a dict of all of the transaction information in JSON format.

    txn_info = fields.JSONField("transaction_info", default = txn_default)
"""

class SalesTestForm(forms.Form):
    payer_email = forms.EmailField(label = 'payer_email', max_length=200)
    ipn_track_id = forms.CharField(label = 'ipn_track_id', max_length=50)

    first_name = forms.CharField(label = 'first_name', max_length=50)
    last_name  = forms.CharField(label = 'last_name', max_length=50)

    option_selection1_1 = forms.CharField(label = 'product1', max_length=32)
    option_selection1_2 = forms.CharField(label = 'product2', max_length=32)

    option_selection2_1 = forms.EmailField(label = 'Email delivary one', max_length=200)
    option_selection2_2 = forms.EmailField(label = 'Email delivary two', max_length=200)

    payment_type = forms.CharField(label = 'payment_type', max_length=32)
    payment_status = forms.CharField(label = 'payment_status', max_length=32)




