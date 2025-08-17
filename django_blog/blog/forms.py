from django import forms
from django.contrib.auth.models import User
from .models import Post
from taggit.forms import TagWidget

# ✅ Post Form
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']
        widgets = {
            'tags': TagWidget(),
        }

# ✅ User Profile Update Form
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']
