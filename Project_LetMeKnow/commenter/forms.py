from django import forms


class ContactForm(forms.Form):
    email = forms.EmailField()
    subject = forms.CharField(max_length=50)
    message = forms.CharField(widget=forms.Textarea(attrs={"row": 2}))
