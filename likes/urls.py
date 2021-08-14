"""Like URLs."""

#Django
from django.urls import path

#Views
from likes.views import like_post


urlpatterns = [
    
    path('like', like_post, name='like_post'),

]
