from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .serializers import BookSerializer, PhraseSerializer, BookListSerializer,PublisherSerializer,AuthorSerializer
# from . import serializers
from rest_framework import status
from rest_framework import viewsets, filters
from .models import BookModel, PhrasesModel, AuthorModel, PublisherModel
# from .serializers import BookModel, PhrasesModel, AuthorModel, PublisherModel, ContentModel
from rest_framework.response import Response
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.views import View

from django.shortcuts import get_object_or_404
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from django.shortcuts import redirect

# from .forms import BookForm
# from django.forms import forms
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer


# Create your views here.
# class BookViewSet(viewsets.ModelViewSet):
class BookViewSet(viewsets.GenericViewSet,ListModelMixin,CreateModelMixin, RetrieveModelMixin, UpdateModelMixin):
    """
    A viewset for viewing and editing BOOK instances.
    """
    serializer_class = BookSerializer
    queryset = BookModel.objects.all()
    print("CAlled")
    def get_serializer_class(self):
        if self.action == 'list':
            return BookListSerializer
        return BookSerializer




class PhraseViewSet(viewsets.GenericViewSet,ListModelMixin,CreateModelMixin, RetrieveModelMixin, UpdateModelMixin):
    """
    A viewset for viewing and editing Phrase instances.
    """
    serializer_class = PhraseSerializer
    queryset = PhrasesModel.objects.all()
    #ARB -4
    filter_backends = [filters.SearchFilter]
    search_fields = ['phrase']

def test(request):
    print("Working")
    return render(request,'books/index.html')



#########################################       BOOK        #####################################################
#To list all books
class BooksViews(View):
    def get(self,request):
        books = BookModel.objects.all()
        bookserializeobj = BookSerializer(books,many=True)
        return render(request,"books/index.html",context = {"data":bookserializeobj.data })



@api_view(('GET','POST'))
@renderer_classes([JSONRenderer])
def add_book(request):
    if request.method == 'POST':
        # print("Request",)
        data={}
        data["name"] = request.POST.get('name')
        data["description"] =request.POST.get('description')
        data["status"] =request.POST.get('status')
        data["publisher"] =request.POST.get('publisher')
        # data["author"] =request.POST.get('author')
        print("Author Value",request.POST.get('author'))
        data["author"] = get_object_or_404(BookModel, pk=request.POST.get('author'))
        # return render(request, "books/add/index.html")
        print("data",data)
        serializer = BookSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return redirect("booklist")
        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)
    else:
        authors = AuthorModel.objects.all().order_by('name')
        publishers = PublisherModel.objects.all().order_by('name')
        return render(request,"books/add/index.html",{"authors":authors,"publishers":publishers})


class BookEdit(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "books/edit/index.html"

    def get(self, request, pk):
        book = get_object_or_404(BookModel, pk=pk)
        serializer = BookSerializer(book)
        return Response({'serializer': serializer, 'book': book})

    def post(self, request, pk):
        book = get_object_or_404(BookModel, pk=pk)
        serializer = BookSerializer(book, data=request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer, 'book': book})
        serializer.save()
        return redirect('booklist')

class BookView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "books/view/index.html"

    def get(self, request, pk):
        book = get_object_or_404(BookModel, pk=pk)
        serializer = BookSerializer(book)
        return Response({'serializer': serializer, 'book': book})

class BookDelete(APIView):
    def get(self, request, pk, format=None):
        book = get_object_or_404(BookModel, pk=pk)
        book.delete()
        return redirect('booklist')


#########################################       PUBLISHER        ##############################################
#To list all books
class listPublishersViews(View):
    def get(self,request):
        books = PublisherModel.objects.all()
        bookserializeobj = PublisherSerializer(books,many=True)
        return render(request,"publishers/index.html",context = {"data":bookserializeobj.data })


class EditPublishersViews(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "publishers/edit/index.html"

    def get(self, request, pk):
        publishers = get_object_or_404(PublisherModel, pk=pk)
        serializer = PublisherSerializer(publishers)
        return Response({'serializer': serializer, 'publishers': publishers})

    def post(self, request, pk):
        publishers = get_object_or_404(PublisherModel, pk=pk)
        serializer = PublisherSerializer(publishers, data=request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer, 'publishers': publishers})
        serializer.save()
        return redirect('publisherlist')

class PublisherDelete(APIView):
    def get(self, request, pk, format=None):
        publisher = get_object_or_404(PublisherModel, pk=pk)
        publisher.delete()
        return redirect('publisherlist')

@api_view(('GET','POST'))
@renderer_classes([JSONRenderer])
def add_publisher(request):
    if request.method == 'POST':
        data={}
        data["name"] = request.POST.get('name')
        data["description"] =request.POST.get('description')
        print("Data",data)
        serializer = PublisherSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return redirect("publisherlist")
        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)
    else:
        return render(request,"publishers/add/index.html")



#####################################################   Authors #############################################

class listAuthorsViews(View):
    def get(self,request):
        authors = AuthorModel.objects.all()
        authorsserializeobj = AuthorSerializer(authors,many=True)
        return render(request,"authors/index.html",context = {"data":authorsserializeobj.data })



class EditAuthorssViews(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "authors/edit/index.html"

    def get(self, request, pk):
        authors = get_object_or_404(AuthorModel, pk=pk)
        serializer = AuthorSerializer(authors)
        return Response({'serializer': serializer, 'authors': authors})

    def post(self, request, pk):
        authors = get_object_or_404(AuthorModel, pk=pk)
        serializer = AuthorSerializer(authors, data=request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer, 'authors': authors})
        serializer.save()
        return redirect('authorlist')

class AuthorDelete(APIView):
    def get(self, request, pk, format=None):
        authors = get_object_or_404(AuthorModel, pk=pk)
        authors.delete()
        return redirect('authorlist')

@api_view(('GET','POST'))
@renderer_classes([JSONRenderer])
def add_author(request):
    if request.method == 'POST':
        print("request.FILES",request.POST.get('author_image', False))
        data={}
        data["name"] = request.POST.get('name')
        data["about"] =request.POST.get('about')
        data["birth_date"] =request.POST.get('birth_date')
        data["death_date"] =request.POST.get('death_date')
        data["author_image"] =request.POST.get('author_image', False)


        print("Data",data)
        serializer = AuthorSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return redirect("authorlist")
        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)
    else:
        return render(request,"authors/add/index.html")
