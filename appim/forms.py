from django import forms
from .models import Comment

class CommentForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField(required=False)
    website = forms.URLField(required=False)
    content = forms.CharField(widget=forms.Textarea)