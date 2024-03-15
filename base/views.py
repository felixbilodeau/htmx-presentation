from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.http import HttpResponse

from .containers import container


@require_http_methods(['GET', 'POST'])
def empty(request):
    return HttpResponse()


@require_http_methods(['GET'])
def homepage(request):
    return render(
        request, 'homepage/home.html', {'homepage_urls': container.homepage_urls()}
    )
