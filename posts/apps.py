from django.apps import AppConfig


class PostsConfig(AppConfig):
    name = 'posts'
    label = 'posts'

    def ready(self):
        from .injector import inject
        inject()
