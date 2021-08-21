"""Users URLs."""

# Django
from django.urls import path

# View
from users import views


urlpatterns = [

    # Management
    path(
        route='login/',
        view=views.LoginView.as_view(),
        name='login'
    ),
    path(
        route='logout/',
        view=views.LogoutView.as_view(),
        name='logout'
    ),
    path(
        route='register/',
        view=views.SignupView.as_view(),
        name='register'
    ),
    path(
        route='profile/',
        view=views.UpdateProfileView.as_view(),
        name='update'
    ),

    path(
        route='change/',
        view=views.ChangePasswordView.as_view(),
        name='change'
    ),

    # Posts
    path(
        route='<str:username>/',
        view=views.UserDetailView.as_view(),
        name='detail'
    ),
    #Follow
    path(
        route='',
        view=views.ProfileFollowToggle.as_view(),
        name="follow"
    ),

]