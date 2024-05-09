from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, reverse, redirect
from django.urls import reverse 
from django.contrib.auth import login
from django.http import JsonResponse
from .models import User, Student
from lms.models import Course, CourseProgress
from .forms import StudentAddForm, ProfileUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash


# Create your views here.
def validate_username(request):
    username = request.GET.get("username", None)
    data = {"is_taken": User.objects.filter(username__iexact=username).exists()}
    return JsonResponse(data)


def register(request):
    if request.method == "POST":
        form = StudentAddForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Account created successfully")

            return redirect(reverse("login"))
        else:
            messages.error(
                request, f"Somthing is not correct, please fill all fields correctly."
            )
    else:
        form = StudentAddForm(request.POST)

    return render(request, "registration/register.html", {"form": form})



@login_required
def profile(request):
        courses = CourseProgress.objects.filter(user=request.user)
        current_user = get_object_or_404(User, id=request.user.id)
        context = {
            'user' : current_user,
            'title': request.user.get_full_name,
            'courses': courses,
        }
        return render(request, "accounts/profile.html", context)



@login_required
def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, "Your password was successfully updated!")
            return redirect("profile")
        else:
            messages.error(request, "Please correct the error(s) below. ")
    else:
        form = PasswordChangeForm(request.user)
    return render(
        request,
        "registration/password_change.html",
        {
            "form": form,
        },
    )


@login_required
def edit_profile(request, profile_id):
    # instance = User.objects.get(pk=pk)
    instance = get_object_or_404(User, pk=profile_id)
    if request.method == "POST":
        form = ProfileUpdateForm(request.POST, request.FILES, instance=instance)
        full_name = instance.get_full_name
        if form.is_valid():
            form.save()

            messages.success(request, ("Student " + full_name + " has been updated."))
            return redirect("profile")
        else:
            messages.error(request, "Please correct the error below.")
    else:
        form = ProfileUpdateForm(instance=instance)
    return render(
        request,
        "accounts/edit_student.html",
        {
            "title": "Edit-profile",
            "form": form,
        },
    )