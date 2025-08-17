from django import forms
from django.contrib.auth.models import User
from .models import Post
from taggit.forms import TagWidget

# post Form
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']
        widgets = {
            'tags': TagWidget(),
        }

# User Profile Update Form
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

    # Optional: add validation rules
    def clean_content(self):
        content = self.cleaned_data.get("content")
        if len(content.strip()) < 3:
            raise forms.ValidationError("Comment must be at least 3 characters long.")
        return content
