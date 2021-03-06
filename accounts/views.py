from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import get_user_model
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import Profile

# Create your views here.
def signup(request):
    if request.user.is_authenticated:
        return redirect('posts:list')
    
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user)
            auth_login(request, user)
            return redirect('posts:list')
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/form.html', context)

def login(request):
    if request.user.is_authenticated:
        return redirect('posts:list')
        
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(request.GET.get('next') or 'posts:list')
    else:
        form = AuthenticationForm()
        next_url = request.GET.get('next', '')
    context = {
        'form': form,
        'next': next_url,
    }
    return render(request, 'accounts/login.html', context)

@login_required
def logout(request):
    auth_logout(request)
    return redirect('posts:list')

def people(request, username):
    people = get_object_or_404(get_user_model(), username=username)
    context = {'people': people,}
    return render(request, 'accounts/people.html', context)

@login_required
def update(request):
    if request.method == 'POST':
        # pass
        form = UserCustomChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('people', request.user.username)
    else:
        form = UserCustomChangeForm(instance=request.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/update.html', context)

@require_POST
@login_required
def delete(request):
    user = request.user
    user.delete()
    return redirect('posts:list')

@login_required
def password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('posts:list')
    else:
        form = PasswordChangeForm(request.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/password.html', context)

@login_required
def profile_update(request):
    profile = Profile.objects.get_or_create(user=request.user)
    if request.method == "POST":
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if profile_form.is_valid():
            profile_form.save()
            return redirect('people', request.user.username)
    else:
        profile_form = ProfileForm(instance=request.user.profile)
    context = { 'profile_form': profile_form,}
    return render(request, 'accounts/profile_update.html', context)

@login_required
def follow(request, user_pk):
    people = get_object_or_404(get_user_model(), pk=user_pk)
    # people이 팔로워하고 있는 모든유저에 현재 접속 유저가 있다면, 언팔로우 
    if request.user in people.followers.all():
        people.followers.remove(request.user)
    #아니면 팔로우
    else:
        people.followers.add(request.user)
    return redirect('people', people.username)