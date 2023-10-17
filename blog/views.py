from django.shortcuts import render,redirect
from .models import Category, Post,HomePageCoverImage
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def index(request):
    posts = Post.objects.all()
    cover_image = HomePageCoverImage.objects.all().first()
    posts_per_page = 1
    paginator = Paginator(posts, posts_per_page)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    page_obj.adjusted_elided_pages = paginator.get_elided_page_range(page_number)
    cxt = {'posts':posts, 'page_obj':page_obj, 'cover_image':cover_image}
    return render(request,'blog/index.html', cxt)

def post(request, pk):
    post = Post.objects.get(id=pk)
    cxt = {'post':post}
    return render(request, 'blog/post.html',cxt)


def contact(request):
    first_post = Post.objects.all().first()
    cxt = {'first_post':first_post}
    return render(request, 'contact.html', cxt)

@login_required(login_url='login-writer')
def createPost(request):
    if request.user.is_staff:
        category = Category.objects.all()
        if request.method == 'POST':
            try:
                category_name = request.POST.get('category')
                category,created = Category.objects.get_or_create(name=category_name)

                Post.objects.create(
                    author = request.user,
                    title = request.POST.get('title'),
                    category = category,
                    image = request.FILES.get('image'),
                    description = request.POST.get('description'),
                    content = request.POST.get('content')
                )
                messages.success(request, "Post Succesfully Created")
                return redirect('dashboard')
            except:
                messages.error(request, "An error occured")
                return redirect('post-new')
        else:
            return render(request, 'blog/post_form.html')
    else:
        return redirect('401')


@login_required(login_url='login-writer')
def updatePost(request, pk):
    post = Post.objects.get(id=pk)
    if request.user != post.author:
        return redirect('401')
    elif post.author == request.user and request.user.is_staff:
        if request.method == 'POST':
            if request.FILES.get('image') == None:
                post.title = request.POST.get('title')
                post.image = post.image
                category_name = request.POST.get('category')
                category,created = Category.objects.get_or_create(name=category_name)
                post.description = request.POST.get('description')
                post.category = category
                post.content = request.POST.get('content')
                post.save()
                return redirect('post',pk=post.id)
            else:
                post.title = request.POST.get('title')
                post.image = request.FILES.get('image')
                category_name = request.POST.get('category')
                category,created = Category.objects.get_or_create(name=category_name)
                post.category = category
                post.description = request.POST.get('description')
                post.content = request.POST.get('content')
                post.save()
            return redirect('post',pk=post.id)

    cxt = {'post':post}
    return render(request, 'blog/post_form.html', cxt)


