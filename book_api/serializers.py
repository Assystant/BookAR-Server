from django.contrib.auth.models import Group, User
from rest_framework import serializers

from .models import AuthorModel, BookModel, ContentModel, PhrasesModel, PublisherModel


class PublisherSerializer(serializers.ModelSerializer):
    """
    Serializer for the PublisherModel.
    
    The serializer defines the fields that get serialized/deserialized. 
    The 'id', 'name', and 'description' fields from the PublisherModel are included.
    """
    class Meta:
        model = PublisherModel
        fields = ['id', 'name', 'description']


class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializer for the AuthorModel.
    
    The serializer defines the fields that get serialized/deserialized. 
    The 'id', 'first_name', 'last_name', and 'author_image' fields from the AuthorModel are included.
    """
    class Meta:
        model = AuthorModel
        fields = ['id', 'first_name', 'last_name', 'author_image']


class ContentSerializer(serializers.ModelSerializer):
    """
    Serializer for the ContentModel.
    
    The serializer defines the fields that get serialized/deserialized. 
    The 'object' and 'phrase' fields from the ContentModel are included.
    """
    class Meta:
        model = ContentModel
        fields = ['object', 'phrase']


class PhraseSerializer(serializers.ModelSerializer):
    """
    Serializer for the PhrasesModel.
    
    The serializer defines the fields that get serialized/deserialized. 
    The 'id', 'phrase', 'book', 'trigger', 'status', and 'object' fields from the PhrasesModel are included.
    """
    class Meta:
        model = PhrasesModel
        fields = ['id', 'phrase', 'book', 'trigger', 'status', 'object']


class BookSerializer(serializers.ModelSerializer):
    """
    Serializer for the BookModel.
    
    The serializer defines the fields that get serialized/deserialized. 
    The 'id', 'name', 'published_date', 'book_cover', 'description', 'ISBN', 'author', 'status', 'publisher', 'phrases', and 'content' fields from the BookModel are included.
    
    The 'phrases', 'content', 'author', and 'publisher' fields use the PhraseSerializer, ContentSerializer, AuthorSerializer, and PublisherSerializer respectively to handle their serialization.
    """
    phrases = PhraseSerializer(many=True, read_only=True)
    content = ContentSerializer(many=True, read_only=True)
    author = AuthorSerializer(read_only=True)
    publisher = PublisherSerializer(read_only=True)

    class Meta:
        model = BookModel
        fields = ['id', 'name', 'published_date', 'book_cover', 'description',
                  'ISBN', 'author', 'status', 'publisher', 'phrases', 'content']


class BookListSerializer(serializers.ModelSerializer):
    """
    Serializer for a list of BookModel instances.
    
    The serializer defines the fields that get serialized/deserialized. 
    The 'id', 'name', 'published_date', 'book_cover', 'description', 'ISBN', 'author', 'publisher', and 'status' fields from the BookModel are included.
    
    The 'author' and 'publisher' fields use the AuthorSerializer and PublisherSerializer respectively to handle their serialization.
    """
    author = AuthorSerializer(read_only=True)
    publisher = PublisherSerializer(read_only=True)

    class Meta:
        model = BookModel
        fields = ['id', 'name', 'published_date', 'book_cover', 'description',
                  'ISBN', 'author', 'publisher', 'status']


class UserSerializers(serializers.ModelSerializer):
    """
    Serializer for the User model.
    
    The serializer defines the fields that get serialized/deserialized. 
    The 'id', 'email', 'username', 'is_active', 'password', and 'groups' fields from the User model are included.
    """
    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'is_active', 'password', 'groups')
        

class UserAuthenticationSerializer(serializers.ModelSerializer):
    """
    Serializer for the User model for authentication purposes.
    
    The serializer defines the fields that get serialized/deserialized. 
    The 'username' and 'password' fields from the User model are included.
    
    Both 'username' and 'password' fields are write-only, meaning they can be used to send data, but won't be included when reading data.
    """
    username = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'password')
