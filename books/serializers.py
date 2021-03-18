from rest_framework import serializers
from .models import BookModel, PhrasesModel

#ARB-6
class PhraseSerializer(serializers.ModelSerializer):

    class Meta:
        model = PhrasesModel
        fields = ['phrase', 'book', 'modified']


class BookSerializer(serializers.ModelSerializer):
    phrases = PhraseSerializer(many=True, read_only=True)

    class Meta:
        model = BookModel
        fields = ['name', 'published_date', 'book_cover','description',
                  'ISBN','author','publisher','phrases','modified']

