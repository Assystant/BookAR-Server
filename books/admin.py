from django.contrib import admin

from django.contrib import admin
from .models import AuthorModel,  PublisherModel, BookModel, PhrasesModel


# @admin.site.register(AuthorModel, BookModel, CategoryModel, PublisherModel, BookRatingModel)
# Register your models here.
# admin.site.register(CategoryModel)
admin.site.register(BookModel)
admin.site.register(PublisherModel)

admin.site.register(AuthorModel)
admin.site.register(PhrasesModel)