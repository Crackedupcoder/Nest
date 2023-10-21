from django.forms import ModelForm,Textarea
from django.utils.translation import gettext_lazy as _
from .models import Comment

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['body']
        widgets = {
            "body": Textarea(attrs={"cols":40, "rows":5,}),
        }
        labels = {
            "body": _("")
        }

