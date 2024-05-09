from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, reverse
from .models import Category, Course, CourseProgress
from accounts.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
import logging

logger = logging.getLogger(__name__)

# Create your views here.

@login_required
def  home(request):
    return render(request, 'lms/home.html')


@login_required
def  catalog(request):
    context = {
        'categories': Category.objects.all(),
        'title': 'Catalog',
        'courses': Course.objects.all(),
    } 
    return render(request, 'lms/catalog.html', {'context': context})

@login_required
def catalog_detail(request, category_id):
    Categorys = get_object_or_404(Category, id=category_id)
    Courses = Categorys.courses.all()
    context = {
        'title' : Category.__str__(Categorys),
        'courses' : Courses,
    }
    return render(request, 'lms/catalog_detail.html', {'context': context})

@login_required
def course_detail(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    is_enrolled = CourseProgress.objects.filter(user=request.user, course=course).exists()
    context = {
        'title' : 'Course Detail',
        'course': course,
        'is_enrolled': is_enrolled,
    }
    return render(request, 'lms/course_detail.html', {'context': context})

@login_required
@require_POST
def assign_course(request, course_id):
    logger.info(f"Attempting to assign course {course_id} to user {request.user.id}")
    course = get_object_or_404(Course, pk=course_id)
    enrollment, created = CourseProgress.objects.get_or_create(
        user=request.user,
        course=course
    )
    logger.info(f"Course assignment {'created' if created else 'found'} for course {course_id}")
    return HttpResponseRedirect(reverse('course_detail', args=(course.id,)))

@login_required
@require_POST
def unassign_course(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    CourseProgress.objects.filter(user=request.user, course=course).delete()
    return HttpResponseRedirect(reverse('course_detail', args=(course.id,)))

@login_required
def learning(request):
    current_user = get_object_or_404(User, id=request.user.id)
    context = {
        'user' : current_user,
        'title': 'My learning',
        'courses': CourseProgress.objects.filter(user=request.user),
    }
    return render(request, 'lms/learning.html', {'context' : context})