from rest_framework import serializers
from .models import BookModel, PhrasesModel
class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = BookModel
        fields = ['name', 'published_date', 'book_cover','description',
                  'ISBN','author','publisher']

class PhraseSerializer(serializers.ModelSerializer):

    class Meta:
        model = PhrasesModel
        fields = ['phrase', 'book']