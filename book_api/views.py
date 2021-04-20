from django.shortcuts import render
# from django.shortcuts import get_object_or_404
from .serializers import BookSerializer, PhraseSerializer, BookListSerializer,PublisherSerializer,AuthorSerializer
from rest_framework.decorators import action
from django.http import JsonResponse
# from rest_framework import status
from rest_framework import viewsets, filters
from .models import BookModel, PhrasesModel, AuthorModel, PublisherModel
from .serializers import UserSerializers
from rest_framework.response import Response
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin
# from rest_framework.views import View
from django.contrib.auth.models import Group,User
from django.shortcuts import get_object_or_404
# from rest_framework.renderers import TemplateHTMLRenderer
# from rest_framework.views import APIView
# from django.shortcuts import redirect

# from .forms import BookForm
# from django.forms import forms
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from rest_framework_extensions.mixins import NestedViewSetMixin

from rest_framework.permissions import IsAuthenticated,IsAdminUser
# Create your views here.
# class BookViewSet(viewsets.ModelViewSet):
# class BookViewSet(viewsets.GenericViewSet,ListModelMixin,CreateModelMixin, RetrieveModelMixin, UpdateModelMixin):
#     """
#     A viewset for viewing and editing BOOK instances.
#     """
#     serializer_class = BookSerializer
#     queryset = BookModel.objects.all()
#     permission_classes = [IsAuthenticated]
#     def get_serializer_class(self):
#         if self.action == 'list':
#             return BookListSerializer
#         return BookSerializer
#
#
#
#
# class PhraseViewSet(viewsets.GenericViewSet,ListModelMixin,CreateModelMixin, RetrieveModelMixin, UpdateModelMixin):
#     """
#     A viewset for viewing and editing Phrase instances.
#     """
#     serializer_class = PhraseSerializer
#     queryset = PhrasesModel.objects.all()
#     permission_classes = [IsAuthenticated]
#     #ARB -4
#     filter_backends = [filters.SearchFilter]
#     search_fields = ['phrase']

def test(request):
    print("Working")
    return render(request,'books/index.html')



#########################################       BOOK        #####################################################
#To list all books
# class BooksViews(View):
#     permission_classes = [IsAuthenticated]
#     def get(self,request):
#         books = BookModel.objects.all()
#         bookserializeobj = BookSerializer(books,many=True)
#         return render(request,"books/index.html",context = {"data":bookserializeobj.data })
#
#
#
# @api_view(('GET','POST'))
# @renderer_classes([JSONRenderer])
# def add_book(request):
#     if request.method == 'POST':
#         # print("Request",)
#         data={}
#         data["name"] = request.POST.get('name')
#         data["description"] =request.POST.get('description')
#         data["status"] =request.POST.get('status')
#         data["publisher"] =request.POST.get('publisher')
#         # data["author"] =request.POST.get('author')
#         print("Author Value",request.POST.get('author'))
#         data["author"] = get_object_or_404(BookModel, pk=request.POST.get('author'))
#         # return render(request, "books/add/index.html")
#         print("data",data)
#         serializer = BookSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return redirect("booklist")
#         return Response(serializer.errors,
#                         status=status.HTTP_400_BAD_REQUEST)
#     else:
#         authors = AuthorModel.objects.all().order_by('name')
#         publishers = PublisherModel.objects.all().order_by('name')
#         return render(request,"books/add/index.html",{"authors":authors,"publishers":publishers})
#
#
# class BookEdit(APIView):
#     renderer_classes = [TemplateHTMLRenderer]
#     template_name = "books/edit/index.html"
#     permission_classes = [IsAuthenticated]
#     def get(self, request, pk):
#         book = get_object_or_404(BookModel, pk=pk)
#         serializer = BookSerializer(book)
#         return Response({'serializer': serializer, 'book': book})
#
#     def post(self, request, pk):
#         book = get_object_or_404(BookModel, pk=pk)
#         serializer = BookSerializer(book, data=request.data)
#         if not serializer.is_valid():
#             return Response({'serializer': serializer, 'book': book})
#         serializer.save()
#         return redirect('booklist')
#
# class BookView(APIView):
#     renderer_classes = [TemplateHTMLRenderer]
#     template_name = "books/view/index.html"
#     permission_classes = [IsAuthenticated]
#     def get(self, request, pk):
#         book = get_object_or_404(BookModel, pk=pk)
#         serializer = BookSerializer(book)
#         return Response({'serializer': serializer, 'book': book})
#
# class BookDelete(APIView):
#     permission_classes = [IsAuthenticated]
#     def get(self, request, pk, format=None):
#         book = get_object_or_404(BookModel, pk=pk)
#         book.delete()
#         return redirect('booklist')
#
#
# #########################################       PUBLISHER        ##############################################
# #To list all books
# class listPublishersViews(View):
#     permission_classes = [IsAuthenticated]
#     def get(self,request):
#         books = PublisherModel.objects.all()
#         bookserializeobj = PublisherSerializer(books,many=True)
#         return render(request,"publishers/index.html",context = {"data":bookserializeobj.data })
#
#
# class EditPublishersViews(APIView):
#     renderer_classes = [TemplateHTMLRenderer]
#     template_name = "publishers/edit/index.html"
#     permission_classes = [IsAuthenticated]
#     def get(self, request, pk):
#         publishers = get_object_or_404(PublisherModel, pk=pk)
#         serializer = PublisherSerializer(publishers)
#         return Response({'serializer': serializer, 'publishers': publishers})
#
#     def post(self, request, pk):
#         publishers = get_object_or_404(PublisherModel, pk=pk)
#         serializer = PublisherSerializer(publishers, data=request.data)
#         if not serializer.is_valid():
#             return Response({'serializer': serializer, 'publishers': publishers})
#         serializer.save()
#         return redirect('publisherlist')
#
# class PublisherDelete(APIView):
#     permission_classes = [IsAuthenticated]
#     def get(self, request, pk, format=None):
#         publisher = get_object_or_404(PublisherModel, pk=pk)
#         publisher.delete()
#         return redirect('publisherlist')
#
# @api_view(('GET','POST'))
# @renderer_classes([JSONRenderer])
# def add_publisher(request):
#     permission_classes = [IsAuthenticated]
#     if request.method == 'POST':
#         data={}
#         data["name"] = request.POST.get('name')
#         data["description"] =request.POST.get('description')
#         print("Data",data)
#         serializer = PublisherSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return redirect("publisherlist")
#         return Response(serializer.errors,
#                         status=status.HTTP_400_BAD_REQUEST)
#     else:
#         return render(request,"publishers/add/index.html")
#
#
#
# #####################################################   Authors #############################################
#
# class listAuthorsViews(View):
#     permission_classes = [IsAuthenticated]
#     def get(self,request):
#         authors = AuthorModel.objects.all()
#         authorsserializeobj = AuthorSerializer(authors,many=True)
#         return render(request,"authors/index.html",context = {"data":authorsserializeobj.data })
#
#
#
# class EditAuthorssViews(APIView):
#     renderer_classes = [TemplateHTMLRenderer]
#     template_name = "authors/edit/index.html"
#     permission_classes = [IsAuthenticated]
#     def get(self, request, pk):
#         authors = get_object_or_404(AuthorModel, pk=pk)
#         serializer = AuthorSerializer(authors)
#         return Response({'serializer': serializer, 'authors': authors})
#
#     def post(self, request, pk):
#         authors = get_object_or_404(AuthorModel, pk=pk)
#         serializer = AuthorSerializer(authors, data=request.data)
#         if not serializer.is_valid():
#             return Response({'serializer': serializer, 'authors': authors})
#         serializer.save()
#         return redirect('authorlist')
#
# class AuthorDelete(APIView):
#     permission_classes = [IsAuthenticated]
#     def get(self, request, pk, format=None):
#         authors = get_object_or_404(AuthorModel, pk=pk)
#         authors.delete()
#         return redirect('authorlist')
#
# @api_view(('GET','POST'))
# @renderer_classes([JSONRenderer])
# def add_author(request):
#     if request.method == 'POST':
#         print("request.FILES",request.POST.get('author_image', False))
#         data={}
#         data["name"] = request.POST.get('name')
#         data["about"] =request.POST.get('about')
#         data["birth_date"] =request.POST.get('birth_date')
#         data["death_date"] =request.POST.get('death_date')
#         data["author_image"] =request.POST.get('author_image', False)
#
#
#         print("Data",data)
#         serializer = AuthorSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return redirect("authorlist")
#         return Response(serializer.errors,
#                         status=status.HTTP_400_BAD_REQUEST)
#     else:
#         return render(request,"authors/add/index.html")

#################################################View SETS######################################################
class StudentAPIViewset(viewsets.GenericViewSet, ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin):
    """
    retrieve:
        Return the given Student whose studentid is Provided.

    list:
        Return a list of all Student.

    create:
        Create a new Student.

    destroy:
        Delete a Student.

    update:
        Update a Student.

    partial_update:
        Update a Student.
    """
    serializer_class = UserSerializers
    queryset = User.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['is_active']
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        group_obj = Group.objects.get(name='user')
        return User.objects.filter(groups=group_obj.id)

    def destroy(self, request, pk=None):
        user = get_object_or_404(User, pk=pk)
        user.delete()
        return JsonResponse({"status": "Student Successfully Deleted"})

class AuthorAPIViewset(viewsets.GenericViewSet, ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin):
    """
    retrieve:
        Return the given Author whose authorid is Provided.

    list:
        Return a list of all Authors.

    create:
        Create a new Author.

    destroy:
        Delete a Author.

    update:
        Update a Author.

    partial_update:
        Update a Author.
    """
    serializer_class = AuthorSerializer
    queryset = AuthorModel.objects.all()
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        # qs = super().get_queryset()
        return super().get_queryset()

    def destroy(self, request, pk=None):
        author = get_object_or_404(AuthorModel, pk=pk)
        author.delete()
        return JsonResponse({"status":"Author Successfully Deleted"})

class BookAPIViewSet(NestedViewSetMixin,viewsets.GenericViewSet,ListModelMixin,CreateModelMixin, RetrieveModelMixin, UpdateModelMixin):
    """
    retrieve:
        Return the given Book whose Bookid is Provided.

    list:
        Return a list of all Books.

    create:
        Create a new Book.

    destroy:
        Delete a Book.

    update:
        Update a Book.

    partial_update:
        Update a Book.
    """
    serializer_class = BookSerializer
    queryset = BookModel.objects.all()

    def get_serializer_class(self):
        """
        Returns a List of book or full details of book whose bookid is provided
        """
        if self.action == 'list':
            return BookListSerializer
        return BookSerializer
    def destroy(self, request, pk=None):
        book = get_object_or_404(BookModel, pk=pk)
        book.delete()
        return JsonResponse({"status":"Book Successfully Deleted"})

    @action(detail=True, methods=['get'])
    def phrases(self, request,pk=None):
        book_Phrases = PhrasesModel.objects.filter(book=pk)
        serializer = PhraseSerializer(book_Phrases,many=True)
        return Response(serializer.data)
    # @action(detail=True, methods=['get'])
    # def get_book_phrases(self, request,pk=None):
    #     book_Phrases = PhrasesModel.objects.filter(book=pk)
    #     serializer = PhraseSerializer(book_Phrases,many=True)
    #     return Response(serializer.data)

class PhraseAPIViewSet(NestedViewSetMixin,viewsets.GenericViewSet,ListModelMixin,CreateModelMixin, RetrieveModelMixin, UpdateModelMixin):
    """
    retrieve:
        Return the given phrase whose phraseid is Provided.

    list:
        Return a list of all pharases of book whose bookid is provided.

    create:
        Create a new phrase for a particular book.

    destroy:
        Delete a phrase belonging to particular book.

    update:
        Update a phrase belonging to particular book.

    partial_update:
        Update a phrase belonging to particular book.
    """
    serializer_class = PhraseSerializer
    queryset = PhrasesModel.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['phrase']
    permission_classes = [IsAuthenticated]
    def destroy(self, request, pk=None):
        parent = self.kwargs['parent']
        phrase = get_object_or_404(PhrasesModel, pk=pk,book=parent)
        phrase.delete()
        return JsonResponse({"status":"Phrase Successfully Deleted"})


class PublisherAPIViewset(viewsets.GenericViewSet, ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin):
    """
    retrieve:
        Return the given Publisher.

    list:
        Return a list of all Publishers.

    create:
        Create a new Publisher.

    destroy:
        Delete a Publisher.

    update:
        Update a Publisher.

    partial_update:
        Update a Publisher.
    """
    serializer_class = PublisherSerializer
    queryset = PublisherModel.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # qs = super().get_queryset()
        return super().get_queryset()

    def destroy(self, request, pk=None):
        publisher = get_object_or_404(PublisherModel, pk=pk)
        publisher.delete()
        return JsonResponse({"status":"Publisher Successfully Deleted"})

