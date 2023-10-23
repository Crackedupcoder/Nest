from django.shortcuts import render,redirect, get_object_or_404
from .models import Post,HomePageCoverImage,AboutTeam, ScholarshipPageHomePage
from users.models import TeamMember
from .forms import CommentForm
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from taggit.models import Tag
from django.db.models import Count
from django.core.mail import send_mail


def index(request, tag_slug=None):
    posts = Post.published.all()
    post_count = posts.count()
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        posts = posts.filter(tags__in=[tag])
    if_paginatable = False
    cover_image = HomePageCoverImage.objects.all().first()
    posts_per_page = 5
    if post_count > posts_per_page:
        if_paginatable = True
    paginator = Paginator(posts, posts_per_page)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    cxt = {'posts':posts, 'page_obj':page_obj, 'cover_image':cover_image, 'paginatable':if_paginatable, 'tag':tag}
    return render(request,'blog/index.html', cxt)



def post(request, year,month,day,post):
    post = get_object_or_404(Post,
                             slug = post,
                             publish__year = year,
                             publish__month = month,
                             publish__day = day,
                             status=Post.Status.PUBLISHED)
    comments = post.comments.filter(active=True)
    form = CommentForm()
    post_tags_ids = post.tags.values_list('id', flat=True)
    similar_posts = Post.published.filter(tags__in=post_tags_ids).exclude(id=post.id)
    similar_posts = similar_posts.annotate(same_tags=Count('tags'))\
                                            .order_by('-same_tags','-publish')[:4]
    cxt = {'post':post, 'form':form, 'comments':comments, 'similar_posts':similar_posts}
    return render(request, 'blog/post.html',cxt)




def contact(request):
    first_post = Post.objects.all().first()
    sent = False
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
    cxt = {'first_post':first_post}
    return render(request, 'contact.html', cxt)



@login_required(login_url='login-writer')
def createPost(request):
    if request.user.is_staff:
        if request.method == 'POST':
            try:
                category_name = request.POST.get('category')
 

                Post.objects.create(
                    author = request.user,
                    title = request.POST.get('title'),
      
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
 
                post.description = request.POST.get('description')
  
                post.content = request.POST.get('content')
                post.save()
                return redirect('post',pk=post.id)
            else:
                post.title = request.POST.get('title')
                post.image = request.FILES.get('image')
                category_name = request.POST.get('category')

 
                post.description = request.POST.get('description')
                post.content = request.POST.get('content')
                post.save()
            return redirect('post',pk=post.id)

    cxt = {'post':post}
    return render(request, 'blog/post_form.html', cxt)



@login_required(login_url='login-user')
@require_POST
def post_comment(request, pk):
    user = request.user
    post = get_object_or_404(Post, id=pk, status=Post.Status.PUBLISHED)
    comment = None

    form = CommentForm(data=request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.user = user
        comment.post = post
        comment.save()
    cxt = {'post':post, 'form':form, 'comment':comment}
    return render(request, 'blog/comments.html', cxt)



def teamAbout(request):
    members = TeamMember.objects.all()
    cxt = {'members': members}
    return render(request, 'blog/about.html', cxt)


def scholarship(request):
    tag_slug = 'scholarship'
    posts = Post.published.all()
    tag = get_object_or_404(Tag, slug=tag_slug)
    posts = posts.filter(tags__in=[tag])
    cover_image = ScholarshipPageHomePage.objects.get(id=1)
    return render(request, 'blog/scholarship.html', {'posts':posts, 'cover_image':cover_image})
