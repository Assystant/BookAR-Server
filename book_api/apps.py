from django.apps import AppConfig
# from book_api import signal

class BooksConfig(AppConfig):
    name = 'book_api'
    def ready(self):
        import book_api.signals
        return super().ready()