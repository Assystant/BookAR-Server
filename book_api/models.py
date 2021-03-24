import datetime
# from django.contrib.sites.models import Site
from django.db import models
from django.contrib.auth import get_user_model
from model_utils.models import TimeStampedModel
from django.core.validators import FileExtensionValidator

User = get_user_model()



class AuthorModel(TimeStampedModel):

    """
    Stores a single Author entry, Extednding fromTimeStampedModel.
    """

    name = models.CharField(max_length=100)
    about = models.TextField(null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    death_date = models.DateField(null=True, blank=True)
    author_image = models.ImageField(default="placeholder_author.png")

    def __str__(self):
        return self.name


class PublisherModel(TimeStampedModel):

    """
    Stores a single Publisher entry, Extednding fromTimeStampedModel.
    """

    name = models.CharField(max_length=100)
    descripton = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

class BookModel(TimeStampedModel):

    """
    Stores a single Book entry, Extednding fromTimeStampedModel.
    """
    STATUS_ACTIVE = 'active'
    STATUS_SUSPENDED = 'inactive'
    STATUS_CHOICES = (
        (STATUS_ACTIVE, 'Active'),
        (STATUS_SUSPENDED, 'Inactive'),

    )

    name = models.CharField(max_length=100)
    published_date = models.DateField(null=True, blank=True)
    book_cover = models.ImageField(default="placeholder_cover.png")
    description = models.TextField()
    ISBN = models.IntegerField(null=True, blank=True)
    author = models.ForeignKey(AuthorModel, on_delete=models.SET_NULL, null=True, blank=True)
    publisher = models.ForeignKey(PublisherModel, on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField(
        "Status Type", choices=STATUS_CHOICES, max_length=10,default=STATUS_ACTIVE)

    def __str__(self):
        return self.name

class PhrasesModel(TimeStampedModel):
    """
    Stores a Multiple Phrases entry related to particular book, Extednding fromTimeStampedModel.
    """
    STATUS_ACTIVE = 'active'
    STATUS_SUSPENDED = 'inactive'
    STATUS_CHOICES = (
        (STATUS_ACTIVE, 'Active'),
        (STATUS_SUSPENDED, 'Inactive'),

    )
    status = models.CharField(
        "Status Type", choices=STATUS_CHOICES, max_length=10,default=STATUS_ACTIVE)
    phrase = models.CharField(max_length=100)
    book = models.ForeignKey(BookModel, on_delete=models.CASCADE,related_name="phrases", null=True, blank=True)

    def __str__(self):
        return str(self.phrase)


class ContentModel(TimeStampedModel):
    object = models.FileField(upload_to = '3dObjects/',validators=[FileExtensionValidator(allowed_extensions=['obj','fbx'])])
    phrase = models.ForeignKey(PhrasesModel, on_delete=models.CASCADE,related_name="content_phrases", null=True, blank=True)

