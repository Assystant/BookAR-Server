from django.contrib import admin
from .models import DemoModel#, AuthorModel,  PublisherModel, BookModel, PhrasesModel, ContentModel


# @admin.site.register(AuthorModel, BookModel, CategoryModel, PublisherModel, BookRatingModel)
# Register your models here.
admin.site.register(DemoModel)

# admin.site.register(ContentModel)
# admin.site.register(BookModel)
# admin.site.register(PublisherModel)
#
# admin.site.register(AuthorModel)
# admin.site.register(PhrasesModel)