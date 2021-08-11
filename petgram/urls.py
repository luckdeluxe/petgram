"""platzigram URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from users.views import ProfileSearchListView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [ 

    path('search', ProfileSearchListView.as_view(), name='search'),

    path('admin/', admin.site.urls),

    path('', include(('posts.urls', 'posts'), namespace='posts')),

    path('users/', include(('users.urls', 'users'), namespace='users')),

    path('comments', include(('comments.urls', 'comments'), namespace='comments')),


#Concatenate static with the values defined in settings.py
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
