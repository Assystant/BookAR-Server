import datetime
from django.db import models
from django.contrib.auth import get_user_model
from model_utils.models import TimeStampedModel
from django.core.validators import FileExtensionValidator

User = get_user_model()

class AuthorModel(TimeStampedModel):
    """
    Stores a single Publisher entry, extending from TimeStampedModel.
    
    Fields:
    name: A char field that stores the name of the publisher. It has a maximum length of 100 characters.
    description: A text field that stores the description of the publisher. This field can be left blank or null.

    Methods:
    __str__: Returns a string representation of the publisher, which is its name.
    """
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    author_image = models.ImageField(upload_to="Author_Image", null=True, blank=True)

    def natural_key(self):
        return self.name

class PublisherModel(TimeStampedModel):
    """
    Stores a single Publisher entry, extending from TimeStampedModel.
    
    Fields:
    name: A char field that stores the name of the publisher. It has a maximum length of 100 characters.
    description: A text field that stores the description of the publisher. This field can be left blank or null.

    Methods:
    __str__: Returns a string representation of the publisher, which is its name.
    """
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

class BookModel(TimeStampedModel):
    """
    Stores a single Content entry, extending from TimeStampedModel.
    
    Fields:
    content_object: A file field that stores the uploaded object files. The files are stored in the 'phrases_object/' directory.
                    Only 'obj' and 'fbx' file extensions are allowed. This field can be left blank or null.
    phrase: A foreign key that creates a many-to-one relationship with the PhrasesModel. 
            This means that each content can be associated with one phrase. 
            If the associated phrase is deleted, the content will also be deleted (models.CASCADE).
            This field can be left blank or null.
    """
    STATUS_ACTIVE = 'active'
    STATUS_SUSPENDED = 'inactive'
    STATUS_CHOICES = (
        (STATUS_ACTIVE, 'Active'),
        (STATUS_SUSPENDED, 'Inactive'),
    )

    name = models.CharField(max_length=100)
    published_date = models.DateField(null=True, blank=True)
    book_cover = models.ImageField(upload_to='Book_Cover', default="placeholder_cover.png", null=True)
    description = models.TextField()
    ISBN = models.IntegerField(null=True, blank=True)
    author = models.ForeignKey(AuthorModel, on_delete=models.SET_NULL, null=True, blank=True)
    publisher = models.ForeignKey(PublisherModel, on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField("Status Type", choices=STATUS_CHOICES, max_length=10, default=STATUS_ACTIVE)

    def __str__(self):
        return self.name

class PhrasesModel(TimeStampedModel):
    """
    Stores a single Content entry, extending from TimeStampedModel.
    
    Fields:
    content_object: A file field that stores the uploaded object files. The files are stored in the 'phrases_object/' directory.
                    Only 'obj' and 'fbx' file extensions are allowed. This field can be left blank or null.
    phrase: A foreign key that creates a many-to-one relationship with the PhrasesModel. 
            This means that each content can be associated with one phrase. 
            If the associated phrase is deleted, the content will also be deleted (models.CASCADE).
            This field can be left blank or null.
    """
    STATUS_ACTIVE = 'active'
    STATUS_SUSPENDED = 'inactive'
    STATUS_CHOICES = (
        (STATUS_ACTIVE, 'Active'),
        (STATUS_SUSPENDED, 'Inactive'),
    )
    trigger = models.ImageField(upload_to='trigger_image/')
    status = models.CharField("Status Type", choices=STATUS_CHOICES, max_length=10, default=STATUS_ACTIVE)
    phrase = models.CharField(max_length=100)
    book = models.ForeignKey(BookModel, on_delete=models.CASCADE, related_name="phrases", null=True, blank=True)
    content_object = models.FileField(upload_to='phrases_object/', null=True, blank=True,
                              validators=[FileExtensionValidator(allowed_extensions=['obj', 'fbx', 'mp3', 'wav', 'jpg', 'png', 'mp4', 'mkv', 'flv', 'avi', 'm4v', 'm4p '])])

    def __str__(self):
        return str(self.phrase)

class ContentModel(TimeStampedModel):
    """
    Stores a single Content entry, extending from TimeStampedModel.
    
    Fields:
    content_object: A file field that stores the uploaded object files. The files are stored in the 'phrases_object/' directory.
                    Only 'obj' and 'fbx' file extensions are allowed. This field can be left blank or null.
    phrase: A foreign key that creates a many-to-one relationship with the PhrasesModel. 
            This means that each content can be associated with one phrase. 
            If the associated phrase is deleted, the content will also be deleted (models.CASCADE).
            This field can be left blank or null.
    """
    content_object = models.FileField(upload_to='phrases_object/', null=True, blank=True, validators=[FileExtensionValidator(allowed_extensions=['obj', 'fbx'])])
    phrase = models.ForeignKey(PhrasesModel, on_delete=models.CASCADE, related_name="content_phrases", null=True, blank=True)

    def __str__(self):
        return str(self.phrase)
