from django.db import models
from django.contrib.auth.models import User
import uuid


class WriterProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    cover_image = models.ImageField(upload_to='writer_profile', default='about-bg.jpg', blank=True, null=True)
    avatar = models.ImageField(upload_to='avatar', default='forum-author1.png', blank=True)
    profession = models.CharField(max_length=255, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    social_media1 = models.CharField(max_length=1000, blank=True, null=True)
    social_media2 = models.CharField(max_length=1000, blank=True, null=True)
    social_media3 = models.CharField(max_length=1000, blank=True, null=True)
    social_media4 = models.CharField(max_length=1000, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)

    def __str__(self):
        return self.name
    

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255,blank=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    avatar = models.ImageField(upload_to='avatar', default='forum-author1.png', blank=True)

    def __str__(self):
        return self.name



