from django.contrib import admin
from .models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'name']
    search_fields = ['user','name','bio','profession','location']
    list_filter  = ['location','profession']


