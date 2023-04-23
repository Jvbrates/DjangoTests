from django import forms


class sendMail(forms.Form):
    mail = forms.EmailField(label="To: ", max_length=100)
    text = forms.CharField(label="Text")
