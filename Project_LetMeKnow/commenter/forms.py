from django import forms

from commenter.models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = [

            "creation_date",
        ]


class ContactForm(forms.Form):
    email = forms.EmailField()
    subject = forms.CharField(max_length=50)
    message = forms.CharField(widget=forms.Textarea(attrs={"row": 2}))
