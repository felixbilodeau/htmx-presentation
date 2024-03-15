from dependency_injector import containers, providers

from django.urls import reverse_lazy


class BaseContainer(containers.DeclarativeContainer):
    homepage_urls = providers.Dict({'Home': reverse_lazy('base:home')})


container = BaseContainer()
