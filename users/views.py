from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import WriterProfile, UserProfile
from blog.models import Post
from .forms import UserUpdateForm, WriterProfileUpdateForm
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse



def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username Taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.error(request, "Email in Use")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                user_model = User.objects.get(username=username)
                new_profile = WriterProfile.objects.create(user=user_model, id=user_model.id)
                new_profile.save()
                login(request, user)
                return redirect('setting')
        else:
            messages.error(request, "Passwords Don't Match")
            return redirect('register')
    return render(request, 'users/register.html')





def about(request,pk):
    user= User.objects.get(username=pk)
    profile = WriterProfile.objects.get(user=user)
    posts = Post.objects.filter(author=user)
    cxt = {'user':user, 'profile':profile, 'posts':posts}
    return render(request, 'users/about.html', cxt)


@login_required(login_url='login-writer')
def dashboard(request):
    user = request.user
    if request.user.is_staff:
        profile = WriterProfile.objects.get(user=user)
        posts = Post.objects.filter(author=user)
    else:
        return redirect('401')
    cxt = {'profile':profile,'posts':posts}
    return render(request, 'users/index.html',cxt)


@login_required(login_url='login')
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
            return redirect('dashboard')
            
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
            return redirect('dashboard')
    cxt = {'profile':profile}
    return render(request, 'users/setting.html', cxt)


def loginWriter(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "User Does not Exist")
            return redirect('login-writer')
        
        user = authenticate(request, username=username, password=password)

        if user != None and user.is_staff:
            login(request, user)
            return redirect('dashboard')
        elif user!= None and user != user.is_staff:
            messages.warning(request, "Please enter the correct username and password for a Writter account. Note that both fields may be case-sensitive.")
            return redirect('login-writer')
        else:
            messages.error(request, "Username or Password Incorrect")
            return redirect('login-writer')
    
    return render(request, 'users/login.html')


def loginUser(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User DOES not exist')
            return redirect('login-user')
           
        user = authenticate(request, username=username, password=password)

        if user != None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'User or Password DOES not Exist')
            return redirect('login-user')
    return render(request, 'users/login_user.html')

def logoutView(request):
    logout(request)
    return redirect('index')


def unauthorised(request):
    return render(request, '401.html')

def not_found(request):
    return render(request, '404.html')

