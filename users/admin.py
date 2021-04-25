#Django Default
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

#Models
from django.contrib.auth.models import User
from users.models import Profile

# Register your models here. // Decorated class
@admin.register(Profile)
#By convention the class that we create must end in Admin.
class ProfileAdmin(admin.ModelAdmin): 
    """Profile admin"""

    list_display = ('user', 'phone_number', 'website', 'created', 'modified')
    search_fields = (
        'user__email',
        'user__first_name',
        'user__last_name',
        'phone_number',
    )

    list_filter = ('created', 'modified')

    # We will move the data we want. It is important that the information is in tuples.
    fieldsets= (
        ('Profile', { # Name of the section.
        'fields': ( # The fields that we will visualize.
        # When we put several fields in the same position within 
        # the tuple of field we are going to display the data in the same row.
        ('user', 'picture'), 
      ),
    }),
        ('Extra info', {
        'fields': ( 
        # In this case the information will be displayed 
        # in 2 rows since the fields tuple has 2 positions.
        ('website', 'phone_number'),
        ('biography',),
      ),
    }),
        ('Metadata', {
        'fields': (
        # This data cannot be modified, 
        # so we will make use of readonly_fields.
        ('created', 'modified'),
      ),
    }),
    )

  # Here we will declare the fields that can only be read but not modified.
    readonly_fields = ('created', 'modified',)



class ProfileInline(admin.StackedInline):
    """Profile in-line admin for users."""

    model = Profile
    can_delete = False
    verbose_name_plural = 'profiles'

class UserAdmin(BaseUserAdmin):
    """Add profile admin to base user admin."""

    inlines = (ProfileInline,)
    list_display = (
        'username',
        'email',
        'first_name',
        'last_name',
        'is_active',
    )

admin.site.unregister(User)
admin.site.register(User, UserAdmin)