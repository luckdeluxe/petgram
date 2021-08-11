#Django
from django.urls import path

from comments.views import create_comment

urlpatterns = [
    path('<int:pk>', create_comment, name='create'),
]