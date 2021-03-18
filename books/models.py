import datetime
# from django.contrib.sites.models import Site
from django.db import models
from django.contrib.auth import get_user_model
from model_utils.models import TimeStampedModel
User = get_user_model()



class AuthorModel(TimeStampedModel):
    name = models.CharField(max_length=100)
    about = models.TextField(null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    death_date = models.DateField(null=True, blank=True)
    author_image = models.ImageField(default="placeholder_author.png")

    def __str__(self):
        return self.name


class PublisherModel(TimeStampedModel):
    name = models.CharField(max_length=100)
    descripton = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

class BookModel(TimeStampedModel):
    name = models.CharField(max_length=100)
    published_date = models.DateField(null=True, blank=True)
    book_cover = models.ImageField(default="placeholder_cover.png")
    description = models.TextField()
    ISBN = models.IntegerField(null=True, blank=True)
    author = models.ForeignKey(AuthorModel, on_delete=models.SET_NULL, null=True, blank=True)
    publisher = models.ForeignKey(PublisherModel, on_delete=models.SET_NULL, null=True, blank=True)
    # how many books that are currently in storage
    # store_amount = models.IntegerField(default=1)
    # page count of the book, no need to specify it
    # pages = models.IntegerField(null=True, blank=True)
    # ISBN doesn't exist for books that have been published before 1970

    # price = models.DecimalField(max_digits=10, decimal_places=2)

    # category = models.ForeignKey(CategoryModel, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name

class PhrasesModel(TimeStampedModel):
    phrase = models.CharField(max_length=100)
    book = models.ForeignKey(BookModel, on_delete=models.CASCADE,related_name="phrases", null=True, blank=True)

    def __str__(self):
        return str(self.book)


