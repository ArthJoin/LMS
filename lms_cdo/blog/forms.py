from django import forms
from .models import Blog, Comments
from tinymce.widgets import TinyMCE


class BlogForm(forms.ModelForm):
    image = forms.ImageField(
        required=False, 
        label='Blog image'
    )

    class Meta:
        model = Blog
        fields = ['title', 'short_discription', 'content', 'image']

        widgets = {
            'title': forms.TextInput(attrs={'placeholder':'Введите заголовок блога', 'class': 'form-control w-100'}),
            'short_discription': forms.TextInput(attrs={'placeholder':'Введите короткое описание', 'class': 'form-control w-100'}),
            'content': TinyMCE(),
        }

    def __init__(self, *args, **kwargs):
        super(BlogForm, self).__init__(*args, **kwargs)
        self.fields['image'].required = False
        self.fields['image'].widget.attrs.update({'class': 'form-control'})


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['content']