from django.contrib import admin
from .models import AuthorModel, PublisherModel, BookModel, PhrasesModel, ContentModel

# Registering the models in the admin site for easy management

# ContentModel represents the content of a book
admin.site.register(ContentModel)

# BookModel represents a book
admin.site.register(BookModel)

# PublisherModel represents a publisher
admin.site.register(PublisherModel)

# AuthorModel represents an author
admin.site.register(AuthorModel)

# PhrasesModel represents a phrase for detection
admin.site.register(PhrasesModel)