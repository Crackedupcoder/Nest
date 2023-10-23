from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import Profile
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm



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
                new_profile = Profile.objects.create(user=user_model, id=user_model.id)
                new_profile.save()
                login(request, user)
                return redirect('setting')
        else:
            messages.error(request, "Passwords Don't Match")
            return redirect('register')
    return render(request, 'users/register.html')



def about(request,pk):
    user= User.objects.get(username=pk)
    profile = Profile.objects.get(user=user)
    posts = user.blog_posts.all()
    cxt = {'user':user, 'profile':profile, 'posts':posts}
    return render(request, 'users/about.html', cxt)



@login_required(login_url='login-user')
def setting(request):
    profile = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        if request.FILES.get('avatar') == None:
            profile.avatar = profile.avatar
            profile.name = request.POST.get('name')
            request.user.email = request.POST.get('email')
            profile.bio = request.POST.get('bio')
            profile.location = request.POST.get('location')
            profile.profession = request.POST.get('profession')
            profile.twitter = request.POST.get('twitter')
            profile.facebook = request.POST.get('facebook')
            profile.instagram = request.POST.get('instagram')
            profile.linkedIn= request.POST.get('linkedIn')
            request.user.save()
            profile.save()
            messages.success(request, 'User Successfully Updated')
            if request.user.is_staff:
                return redirect('about', pk=request.user)
            else:
                return redirect('index')
            
        elif request.FILES.get('avatar') != None:
            profile.avatar = request.FILES.get('avatar')
            profile.name = request.POST.get('name')
            request.user.email = request.POST.get('email')
            profile.bio = request.POST.get('bio')
            profile.location = request.POST.get('location')
            profile.profession = request.POST.get('profession')
            profile.twitter = request.POST.get('twitter')
            profile.facebook = request.POST.get('facebook')
            profile.instagram = request.POST.get('instagram')
            profile.linkedIn= request.POST.get('linkedIn')
            request.user.save()
            profile.save()
            messages.success(request, 'User Successfully Updated')
            if request.user.is_staff:
                return redirect('about', pk=request.user)
            else:
                return redirect('index')
    cxt = {'profile':profile}
    return render(request, 'users/setting.html', cxt)



def loginUser(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        #trick to get round round changing the user model
        try:
            user = User.objects.get(email=email)
        except:
            messages.error(request, 'User with email DOES not exist')
            return redirect('login-user')


        user = authenticate(request, username=user.username, password=password)

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



@login_required(login_url='login-user')
def changePassword(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, "Password Successfully Updated")
            return redirect('about', pk=request.user)
        else:
            messages.error(request, "Current Password Incorrect or Passwords Didn't Match")
            return redirect('password-change')
       
    else:
        form = PasswordChangeForm(request.user) 
    return render(request, 'users/password_change.html', {'form':form})



def unauthorised(request):
    return render(request, '401.html')


def not_found(request):
    return render(request, '404.html')




