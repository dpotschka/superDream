from django import forms



class ChangePasswordForm(forms.Form):
    email = forms.EmailField(label = 'Your Email', max_length=200)
    oldPassword = forms.CharField(label = 'Your Old Password', max_length=32, widget=forms.PasswordInput)
    newPassword = forms.CharField(label = 'Your New Password', max_length=32, widget=forms.PasswordInput)
    newPasswordAgain = forms.CharField(label = 'Your New Password again', max_length=32, widget=forms.PasswordInput)



class ContactForm(forms.Form):
    contact_name = forms.CharField(required=True)
    contact_email = forms.EmailField(required=True)
    content = forms.CharField(required=True, widget=forms.Textarea)

    pledgeAmount = forms.IntegerField(required=True, min_value=0)

    #stopRobot = forms.CharField(required=True)



    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['contact_name'].label = "Your name:"
        self.fields['contact_email'].label = "Your email:"
        self.fields['content'].label = "How may I help you?"

        self.fields['pledgeAmount'].label = "How much money (in $US) are you thinking about investing?  (current minimum is $10k).  Please enter zero if you are contacting me for other reasons..."

        #self.fields['stopRobot'].label = "What is 6*3?"






######################### End ContactForm


class ForgotForm(forms.Form):
    email = forms.EmailField(label = 'Your Email', max_length=200)



class LogOnForm(forms.Form):

    userName = forms.CharField(label='Your Nickname', max_length=100)
    password = forms.CharField(label = 'Your Password', max_length=32, widget=forms.PasswordInput)



# I'm calling the user's name, nickname instead, it is funner.
class UserInfoForm(forms.Form):
    """For a new user to sign up."""

    userName = forms.CharField(label='Your Nickname', max_length=100)
    email = forms.EmailField(label = 'Your Email', max_length=200)


class SurvivesForm(forms.Form):
    email = forms.EmailField(label = 'Your Email', max_length=200)




