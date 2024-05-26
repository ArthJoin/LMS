from django import forms
from .models import Blog
from tinymce.widgets import TinyMCE


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'content']

        widgets = {
            'title': forms.TextInput(attrs={'placeholder':'Введите заголовок блога', 'class': 'form-control w-100'}),
            'content': TinyMCE(),
        }
        