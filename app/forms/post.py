from django import forms

from app.models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title", "content", "image",)
