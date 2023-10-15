# from django import forms
# from django.contrib.auth.models import User
# from .models import WriterProfile

# class UserUpdateForm(forms.ModelForm):
#     email = forms.EmailField

#     class Meta:
#         model = User
#         fields = ['email']


# class WriterProfileUpdateForm(forms.ModelForm):
#     class Meta:
#         model = WriterProfile
#         fields = ['name','profession','location','avatar','bio','id']
#         exclude = ['user','id','cover_image']