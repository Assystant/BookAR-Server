from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import BookModel, PhrasesModel

@receiver(post_save, sender=PhrasesModel)
def update_book_last_update(sender, instance, created, **kwargs):
    """
    Signal receiver that updates the 'modified' field of the associated book 
    when a PhrasesModel instance is updated.

    Args:
    sender: The model class. 
    instance: The actual instance being saved.
    created: Boolean; True if a new record was created.
    **kwargs: Arbitrary keyword arguments.
    """
    if not created:
        book = instance.book
        book.modified = instance.modified
        book.save()
