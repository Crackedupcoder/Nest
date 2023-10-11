from django.db import models
from django.contrib.auth.models import User
import uuid


class WriterProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    cover_image = models.ImageField(upload_to='writer_profile', default='about-bg.jpg', blank=True)
    avatar = models.ImageField(upload_to='avatar', default='forum-author1.png', blank=True)
    profession = models.CharField(max_length=255, blank=True)
    location = models.CharField(max_length=255, blank=True)
    social_media1 = models.CharField(max_length=1000, blank=True)
    social_media2 = models.CharField(max_length=1000, blank=True)
    social_media3 = models.CharField(max_length=1000, blank=True)
    social_media4 = models.CharField(max_length=1000, blank=True)
    bio = models.TextField(blank=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)

    def __str__(self):
        return self.name


