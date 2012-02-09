from django import forms
from posts.models import *

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['user', 'pub_date']

class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        exclude = ['pub_date']

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ['user']