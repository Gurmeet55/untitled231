from django import forms
class RegistrationForm1(forms.Form):
    name = forms.CharField(label="Enter Your Name", max_length=200)
    email = forms.CharField(label="Enter Your Email", max_length=200, widget=forms.EmailInput)
    contact = forms.CharField(label="Enter Your Contact", max_length=200)
    address = forms.CharField(label="Enter Your Address", max_length=200)
    password = forms.CharField(label="Enter Your Password", max_length=200,widget=forms.PasswordInput)




class loginform1(forms.Form):
    email=forms.CharField(label="Enter Your Email", max_length=200, widget=forms.EmailInput)
    password= forms.CharField(label="Enter Your Password", max_length=200,widget=forms.PasswordInput)

class empdetail(forms.Form):
    e_name = forms.CharField(label="Enter emp Name", max_length=200)
    email = forms.CharField(label="Enter email", max_length=200)

    jobtitle= forms.CharField(label="Enter emp jobtitle", max_length=200)
    specialization=forms.CharField(label="Enter emp specialization ", max_length=200)
    Experince=forms.CharField(label="Enter emp  Experince ", max_length=200)

