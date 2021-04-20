from rest_framework import serializers
from .models import BookModel, PhrasesModel, AuthorModel, PublisherModel, ContentModel
from django.contrib.auth.models import Group,User





class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = PublisherModel
        fields = ['id','name', 'descripton']

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthorModel
        fields = ['id','first_name', 'last_name',
                  'author_image']


class ContentSerializer(serializers.ModelSerializer):
    """
    A Phrase Serializer for Phrase and book Fields.
    """

    class Meta:
        model = ContentModel
        fields = ['object','phrase']

class PhraseSerializer(serializers.ModelSerializer):
    """
    A Phrase Serializer for Phrase and book Fields.
    """
    # content_phrases = ContentSerializer(many= True , read_only=True)
    class Meta:
        model = PhrasesModel
        fields = ['id','phrase', 'book','trigger','status','object']

class BookSerializer(serializers.ModelSerializer):

    """
    A BookSerializer  with 'name', 'published_date', 'book_cover','description',
                  'ISBN','author','publisher','phrases' .

    """
    phrases = PhraseSerializer(many=True, read_only=True)
    content = ContentSerializer(many=True, read_only=True)
    author = AuthorSerializer(many=False, read_only=True)
    publisher = PublisherSerializer(many=False, read_only=True)
    class Meta:
        model = BookModel
        fields = ['id','name', 'published_date', 'book_cover','description',
                  'ISBN','author','status','publisher','phrases','content']


class BookListSerializer(serializers.ModelSerializer):
    """
    A BookListSerializer  with 'name', 'published_date', 'book_cover','description',
                  'ISBN','author','publisher' .
    It lists all the AR available books.
    """
    # author = AuthorSerializer(many=False, read_only=True)
    # publisher = PublisherSerializer(many=False, read_only=True)
    author = AuthorSerializer(many=False, read_only=True)
    publisher = PublisherSerializer(many=False, read_only=True)
    class Meta:
        model = BookModel
        fields = ['id','name', 'published_date', 'book_cover','description',
                  'ISBN','author','publisher','status']


class UserSerializers(serializers.ModelSerializer):
# groups = GroupSerializer(many=True)

    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'is_active',
               'password', 'groups')

# class StudentSerializer(serializers.ModelSerializer):
#     user = UserSerializer(many=False, read_only=True)
#
#     class Meta:
#         model = Group
#         fields = ('id','user')


class UserAuthenticationSerializer(serializers.ModelSerializer):
    username = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'password')