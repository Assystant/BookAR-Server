from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import BookModel, PhrasesModel
#ARB-5
@receiver(post_save, sender=PhrasesModel)
def update_book_last_update(sender, instance,created, **kwargs):
    if not created:
        book = instance.book
        book.modified = instance.modified
        book.save()