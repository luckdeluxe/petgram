#Django
from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic.list import ListView

#Models
from comments.models import Comment

#Forms
from comments.forms import CommentForm


class CommentListView(ListView):
    template_name = 'posts/feed.html'
    model = Comment
    ordering = ('-created_date',)
    paginate_by = 3
    context_object_name = 'comments'


def create_comment(request, pk):
    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES)
    
        if form.is_valid():
            form.instance.post_id = pk
            form.instance.user = request.user
            form.instance.profile = request.user.profile
            form.save()
            return redirect('posts:feed')
    else:
        form = CommentForm()
    
    return render(request, 'posts/feed.html', {
        'form': form,
        'user': request.user,
        'profile': request.user.profile
        })