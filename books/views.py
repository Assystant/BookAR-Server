from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .serializers import BookSerializer, PhraseSerializer
# from . import serializers
from rest_framework import viewsets
from .models import BookModel, PhrasesModel
from rest_framework.response import Response
from rest_framework.mixins import ListModelMixin, CreateModelMixin
# Create your views here.
# class BookViewSet(viewsets.ModelViewSet):
class BookViewSet(viewsets.GenericViewSet,ListModelMixin,CreateModelMixin):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = BookSerializer
    queryset = BookModel.objects.all()



class PhraseViewSet(viewsets.ModelViewSet):
    serializer_class = PhraseSerializer
    queryset = PhrasesModel.objects.all()

