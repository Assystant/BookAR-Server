from django.apps import AppConfig

class BooksConfig(AppConfig):
    """
    Django AppConfig for the book_api application.
    This configuration is used by Django to control the behavior of the application.
    """
    name = 'book_api'

    def ready(self):
        """
        Override the ready method to import the signals module.
        This ensures that the signal handlers are connected when the application starts.
        """
        import book_api.signals
        return super().ready()