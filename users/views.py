from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import WriterProfile
from blog.models import Post
from .forms import UserUpdateForm, WriterProfileUpdateForm
from django.contrib import messages

def login(request):
    return render(request, 'users/login')


def about(request,pk):
    user= User.objects.get(username=pk)
    profile = WriterProfile.objects.get(user=user)
    cxt = {'user':user, 'profile':profile}
    return render(request, 'users/about.html', cxt)


def dashboard(request, pk):
    user= User.objects.get(username=pk)
    profile = WriterProfile.objects.get(user=user)
    posts = Post.objects.filter(author=user)
    cxt = {'profile':profile,'posts':posts}
    return render(request, 'users/index.html',cxt)


def setting(request):
    profile = WriterProfile.objects.get(user=request.user)
    if request.method == 'POST':
        if request.FILES.get('avatar') == None:
            profile.avatar = profile.avatar
            profile.name = request.POST.get('name')
            request.user.email = request.POST.get('email')
            profile.bio = request.POST.get('bio')
            profile.location = request.POST.get('location')
            profile.profession = request.POST.get('profession')
            profile.social_media1 = request.POST.get('social_media1')
            profile.social_media2 = request.POST.get('social_media2')
            profile.social_media3 = request.POST.get('social_media3')
            profile.social_media4 = request.POST.get('social_media4')
            request.user.save()
            profile.save()
            messages.success(request, 'User Successfully Updated')
            return redirect('dashboard',pk=request.user)
            
        elif request.FILES.get('avatar') != None:
            profile.avatar = request.FILES.get('avatar')
            profile.name = request.POST.get('name')
            request.user.email = request.POST.get('email')
            profile.bio = request.POST.get('bio')
            profile.location = request.POST.get('location')
            profile.profession = request.POST.get('profession')
            profile.social_media1 = request.POST.get('social_media1')
            profile.social_media2 = request.POST.get('social_media2')
            profile.social_media3 = request.POST.get('social_media3')
            profile.social_media4 = request.POST.get('social_media4')
            request.user.save()
            profile.save()
            messages.success(request, 'User Successfully Updated')
            return redirect('dashboard',pk=request.user)
    cxt = {'profile':profile}
    return render(request, 'users/setting.html', cxt)