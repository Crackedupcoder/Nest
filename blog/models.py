from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.db.models.query import QuerySet
from django.utils import timezone
from django.urls import reverse
from taggit.managers import TaggableManager

class PublishedManager(models.Manager):
    def get_queryset(self) -> QuerySet:
        return super().get_queryset().filter(status=Post.Status.PUBLISHED)


class Post(models.Model):

    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'

    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    title = models.CharField(max_length=255, blank=True)
    slug = models.SlugField(max_length=255, unique_for_date='publish')
    description = models.CharField(max_length=255, blank=True)
    image = models.ImageField(upload_to='posts')
    content = RichTextField()
    tags = TaggableManager()
    publish = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=2,
                              choices=Status.choices,
                              default=Status.DRAFT)
    

    objects = models.Manager()
    published = PublishedManager()

    class Meta:
        ordering = ['-updated', '-created']
        indexes = [models.Index(fields=['-publish']),]

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post', args=[self.publish.year,
                                     self.publish.month,
                                     self.publish.day,
                                     self.slug])
    



class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['-updated', '-created']
        indexes = [models.Index(fields=['-updated'])]

    def __str__(self):
        return f"Comment by {self.user} on {self.post}"




class AboutTeam(models.Model):
    body = RichTextField()
    cover_image = models.ImageField(upload_to='covers', default='about-bg.jpg')

    def __str__(self):
        return self.body[:50]




class HomePageCoverImage(models.Model):
    image = models.ImageField(upload_to='covers')
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.image.url


class ScholarshipPageHomePage(models.Model):
    image =models.ImageField(upload_to='covers')
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.image.url
    