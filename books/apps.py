from django.apps import AppConfig
# from books import signal

class BooksConfig(AppConfig):
    name = 'books'
    def ready(self):
        import books.signals
        return super().ready()
