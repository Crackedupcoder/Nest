from django.shortcuts import render
from .models import Category, Post
from django.core.paginator import Paginator

def index(request):
    posts = Post.objects.all()
    first_post = Post.objects.all().first()
    posts_per_page = 4
    paginator = Paginator(posts, posts_per_page)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    page_obj.adjusted_elided_pages = paginator.get_elided_page_range(page_number)
    cxt = {'posts':posts, 'page_obj':page_obj, 'first_post':first_post}
    return render(request,'blog/index.html', cxt)

def post(request, pk):
    post = Post.objects.get(id=pk)
    cxt = {'post':post}
    return render(request, 'blog/post.html',cxt)


def contact(request):
    first_post = Post.objects.all().first()
    cxt = {'first_post':first_post}
    return render(request, 'contact.html', cxt)
