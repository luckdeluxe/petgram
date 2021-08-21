from django.contrib.auth import get_user_model
from django.db import models
from django.contrib.auth.models import User

# Makes email unique (User is class django default)
User._meta.get_field('email')._unique = True

class Profile(models.Model):
    """Profile model.
        Proxy model that extends the base data with
        other information.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    website = models.URLField(max_length=50, blank=True)
    biography = models.TextField(blank=True)
    phone_number = models.CharField(max_length=13)
    picture = models.ImageField(
        upload_to='users/pictures',
        blank=True,
        null=True)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    #Followers system
    followers = models.ManyToManyField(User, related_name='is_following', blank=True) #user.followers.all()
    #Status online-offline
    activated = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
    
