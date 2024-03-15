from base.containers import container

from django.urls import reverse_lazy


def inject():
    container.homepage_urls.add_kwargs({'Posts': reverse_lazy('posts:index')})
