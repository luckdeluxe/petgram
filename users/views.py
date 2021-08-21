"""Users views."""

# Django
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import views as auth_views
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, FormView, UpdateView, ListView, View
from django.db.models import Q
from django.shortcuts import redirect

# Models
from django.contrib.auth.models import User
from posts.models import Post
from users.models import Profile

# Forms
from users.forms import SignupForm


class ProfileFollowToggle(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        user_to_toggle = request.POST.get('username')
        profile_ = Profile.objects.get(user__username__iexact=user_to_toggle)
        user = request.user

        if user in profile_.followers.all():
            profile_.followers.remove(user)
        else:
            profile_.followers.add(user)
            
        return redirect(f'{profile_.user.username}/')


class ProfileSearchListView(ListView):
    template_name = 'search.html'
    model = User
    context_object_name = 'users'
    paginate_by = 12
    

    def get_queryset(self):
        filters = Q(username__icontains=self.query()) | Q(first_name__icontains=self.query()) | Q(last_name__icontains=self.query())
        return User.objects.filter(filters)

    def query(self):
        return self.request.GET.get('q')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.query()
        return context


class UserDetailView(LoginRequiredMixin, DetailView):
    """User detail view."""

    template_name = 'users/detail.html'
    slug_field = 'username'
    slug_url_kwarg = 'username'
    queryset = User.objects.all()
    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        """Add user's posts to context."""
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        is_following = False
        if user.profile in self.request.user.is_following.all():
            is_following = True
        context['is_following'] = is_following
        context['posts'] = Post.objects.filter(user=user).order_by('-created')
        return context


class SignupView(FormView):
    """Users sign up view."""

    template_name = 'users/register.html'
    form_class = SignupForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        """Save form data."""
        form.save()
        return super().form_valid(form)


class UpdateProfileView(LoginRequiredMixin, UpdateView):
    """Update profile view."""

    template_name = 'users/update_profile.html'
    model = Profile
    fields = ['website', 'biography', 'phone_number', 'picture']

    def get_object(self):
        """Return user's profile."""
        return self.request.user.profile

    def get_success_url(self):
        """Return to user's profile."""
        username = self.object.user.username
        return reverse('users:detail', kwargs={'username': username})


class LoginView(auth_views.LoginView):
    """Login view."""

    template_name = 'users/login.html'


class LogoutView(LoginRequiredMixin, auth_views.LogoutView):
    """Logout view."""

    template_name = 'users/logged_out.html'


class ChangePasswordView(LoginRequiredMixin, auth_views.PasswordChangeView):
    """Change password view."""

    template_name = 'users/change.html'
    success_url = reverse_lazy('users:login')