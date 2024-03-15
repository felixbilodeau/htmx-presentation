from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from .models import Post


@require_http_methods(['GET'])
def index(request):
    posts = Post.objects.order_by('-created').all()
    return render(request, 'posts/index.html', {'posts': posts})
