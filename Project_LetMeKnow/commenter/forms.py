from django import forms
from django.contrib.auth.forms import UserCreationForm, UsernameField
from commenter.models import Comment, Product
from django.contrib.auth import get_user_model

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = []



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = [

            "creation_date",
            "like",
            "dislike",
        ]


class ContactForm(forms.Form):
    email = forms.EmailField()
    subject = forms.CharField(max_length=50)
    message = forms.CharField(widget=forms.Textarea(attrs={"row": 2}))

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
