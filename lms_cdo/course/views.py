from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from lms.models import Course, CourseProgress
from .models import CourseItem, CourseContent
from django.http import JsonResponse

# Create your views here.
@login_required
def course(request, course_id):
    context = {
        'Course': Course.objects.get(id=course_id),
        'CourseProgress': CourseProgress.objects.filter(user=request.user.id),
        'course_item': CourseItem.objects.filter(course=course_id),
    }
    return render(request, 'course/course.html', {'context': context})

def fetch_content(request):
    item_id = request.GET.get('id')
    content = CourseContent.objects.filter(course_item_id=item_id).first()
    if content:
        return JsonResponse({'content': content.content})
    else:
        return JsonResponse({'content': 'No content available.'}, status=404)