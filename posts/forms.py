from django import forms
from posts.models import *

def make_custom_datefield(f):
    formfield = f.formfield()
    if isinstance(f, models.DateField):
        formfield.widget.format = '%m/%d/%Y'
        formfield.widget.attrs.update({'class':'datePicker', 'readonly':'true'})
    return formfield
    
class PostForm(forms.ModelForm):
    formfield_callback = make_custom_datefield
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
