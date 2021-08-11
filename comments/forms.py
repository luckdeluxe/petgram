from comments.models import Comment
from django import forms

class CommentForm(forms.ModelForm):
    pass

    class Meta:
        model = Comment
        fields = ['text']
        