from django.contrib import admin
from .models import Profile, TeamMember

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'name']
    search_fields = ['user','name','bio','profession','location']
    list_filter  = ['location','profession']


@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ['name', 'position']


