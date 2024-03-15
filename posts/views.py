from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_http_methods

from .models import Post
from .forms import PostForm


@require_http_methods(['GET'])
def index(request):
    return render(request, 'posts/index.html')


@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'GET':
        form = PostForm()
        return render(request, 'posts/create-form.html', {'form': form})
    elif request.method == 'POST':
        form = PostForm(data=request.POST)
        if form.is_valid():
            post = form.save()
            return render(request, 'posts/post.html', {'post': post})
        return render(request, 'posts/create-form.html', {'form': form})
    

@require_http_methods(['POST'])
def post_list(request):
    exclude_ids = set(request.POST.keys()) - set(['csrfmiddlewaretoken'])
    posts = Post.objects.order_by('-created').exclude(pk__in=exclude_ids)
    return render(request, 'posts/post-list.html', {'posts': posts})


@require_http_methods('GET')
def get_post(request, pk):
    post= get_object_or_404(Post, pk=pk)
    return render(request, 'posts/post.html', {'post': post})


@require_http_methods(['GET', 'POST'])
def update(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'GET':
        form = PostForm(instance=post)
    elif request.method == 'POST':
        form = PostForm(instance=post, data=request.POST)
        if form.is_valid():
            post = form.save()
            return render(request, 'posts/post.html', {'post': post})
    return render(request, 'posts/update-form.html', {'form': form})
