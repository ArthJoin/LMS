from django.shortcuts import render, redirect
from django.views import View 
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404

from .models import Blog, Comments
from .forms import BlogForm, CommentForm
from accounts.models import User


# Create your views here.
class ViewAllBlogs(View):   
    @method_decorator(login_required)
    def get(self, request):
        blogs = Blog.objects.all().order_by('-created_at')
        context = {
            'title': 'Список блогов',
            'blogs': blogs,
        }

        return render(request, 'blog/home.html', context=context)
    
class ViewBlog(View):
    def get(self, request, blog_id):
        blog = get_object_or_404(Blog, pk=blog_id)
        comments = blog.comments.all()
        form = CommentForm()
        context = {
            'title': 'Детали блога',
            'blog': blog, 
            'comments': comments,
            'form': form,
        }

        return render(request, 'blog/blog_detail.html', context=context)
    def post(self, request, blog_id):
        blog = get_object_or_404(Blog, id=blog_id)
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = blog
            comment.author = request.user
            comment.save()
            return redirect('blogs:blog_detail', blog_id=blog_id)
        comments = blog.comments.all()
        context = {
            'blog': blog,
            'comments': comments,
            'form': form,
        }
        return render(request, 'blog/blog_detail.html', context)


class CreateBlogView(View):     # создать
    @method_decorator(login_required)
    def get(self, request):
        form = BlogForm()
        context = {'form': form}
        return render(request, 'blog/create_blog.html', context=context)

    @method_decorator(login_required)
    def post(self, request):
        form = BlogForm(request.POST)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user  # Устанавливаем автора как текущего пользователя
            blog.save()
            return redirect('blogs:home')
        return render(request, 'blog/create_blog.html', {'form': form})
    


class ProfileView(View):        # личный профиль
    def get(self, request):
        user = request.user
        blogs = Blog.objects.filter(author=user).order_by('-created_at')

        context = {
            'title': 'Мой профиль',
            'user': user,
            'blogs': blogs,
        }
        
        return render(request, 'accounts/profile.html', context=context)
    

class EditBlog(View):   # редактировать
    def get(self, request, blog_id):
        blog = Blog.objects.get(id=blog_id)
        form = BlogForm(blog.to_json())

        context = {
            'title': 'Редактировать блог',
            'form': form,
            'blog': blog,
        }

        return render(request, 'blog/edit_blog.html', context=context)
    
    def post(self, request, blog_id):
        blog = get_object_or_404(Blog, id=blog_id)
        form = BlogForm(request.POST, request.FILES, instance=blog)

        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('blogs:home'))
        else:
            context = {
                'title': 'Редактировать блог',
                'form': form,
                'blog': blog,
                'error': 1,
            }
            return render(request, 'blog/edit_blog.html', context=context)

class DeleteBlog(View): # удаление
    def get(self, request, blog_id):
        blog = Blog.objects.get(id=blog_id)
        blog.delete()

        return redirect(reverse_lazy('accounts:profile'))
    

class LikeView(View):
    def post(self, request, content_type, content_id):
        if content_type == 'blog':
            content = get_object_or_404(Blog, id=content_id)
        elif content_type == 'comment':
            content = get_object_or_404(Comments, id=content_id)
        else:
            return redirect('blogs:home')
        
        if request.user in content.likes.all():
            content.likes.remove(request.user)
        else:
            content.likes.add(request.user)
        
        if content_type == 'blog':
            return redirect('blogs:blog_detail', blog_id=content.id)
        else:
            return redirect('blogs:blog_detail', blog_id=content.post.id)