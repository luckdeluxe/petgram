#Django
from django.urls import path

from comments.views import CommentDeleteView, create_comment

urlpatterns = [
    path('<int:pk>', create_comment, name='create'),
    path('comments/delete/<int:pk>', CommentDeleteView.as_view(), name='delete_comment'),
]