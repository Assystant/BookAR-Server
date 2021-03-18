from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .serializers import BookSerializer, PhraseSerializer
# from . import serializers
from rest_framework import viewsets, filters
from .models import BookModel, PhrasesModel
from rest_framework.response import Response
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin
# Create your views here.
# class BookViewSet(viewsets.ModelViewSet):
class BookViewSet(viewsets.GenericViewSet,ListModelMixin,CreateModelMixin, RetrieveModelMixin, UpdateModelMixin):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = BookSerializer
    queryset = BookModel.objects.all()



class PhraseViewSet(viewsets.GenericViewSet,ListModelMixin,CreateModelMixin, RetrieveModelMixin, UpdateModelMixin):
    serializer_class = PhraseSerializer
    queryset = PhrasesModel.objects.all()
    
    filter_backends = [filters.SearchFilter]
    search_fields = ['phrase']
