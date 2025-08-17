from django import forms
from .models import Post
from taggit.forms import TagWidget  # ✅ import

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']
        widgets = {
            'tags': TagWidget(),  # ✅ allows tagging input
        }
