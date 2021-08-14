"""Petgram URL Configuration"""

from users.views import ProfileSearchListView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [ 

    path('admin/', admin.site.urls),

    path('search/', ProfileSearchListView.as_view(), name='search'),

    path('', include(('posts.urls', 'posts'), namespace='posts')),

    path('users/', include(('users.urls', 'users'), namespace='users')),

    path('comments/', include(('comments.urls', 'comments'), namespace='comments')),

    path('', include(('likes.urls', 'likes'), namespace='likes')),

#Concatenate static with the values defined in settings.py
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
