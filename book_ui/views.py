from django.shortcuts import render
from rest_framework.response import Response
# Create your views here.
from .forms import Demoform, BookForm, PhraseForm, PublisherForm, AuthorForm
from book_api.models import AuthorModel, PublisherModel, BookModel,PhrasesModel
from book_api.serializers import BookSerializer
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect
from django.views.static import serve
from config import settings
from django.contrib.auth.decorators import login_required
from django.urls import reverse


# def handle_uploaded_file(f):
#     with open(f, 'wb+') as destination:
#         for chunk in f.chunks():
#             destination.write(chunk)


@renderer_classes([JSONRenderer])
# @api_view(['GET', 'POST', 'DELETE'])
@csrf_exempt
@login_required
def lbooks(request,pk=None):
    """
    :param request:
    :param pk:
    Used to list and delete the BOoks
    """
    print("Request",request.user)
    if request.method == 'GET':
        if pk==None:
            books= BookModel.objects.all()
            return render(request, "books/index.html",{"books":books})
        else:
            book = BookModel.objects.get(pk=pk)
            # author=AuthorModel.objects.select_related().filter(bookmodel = pk)
            # publisher = PublisherModel.objects.select_related().filter(bookmodel = pk)
            print("Books",book.author.name)
            # print("author",author)
            # print("publisher",publisher)
            return JsonResponse({"status":True,"message":"Book Successfully Viewed"})
    if request.method == 'DELETE':
        if BookModel.objects.filter(pk=pk).delete():
            return JsonResponse({"status":True,"message":"Book Successfully Deleted"})
    else:
        return JsonResponse({"status": False, "message": "Invalid Request"})

@api_view(["GET","POST"])
@permission_classes([IsAdminUser])
def editbook(request,pk=None):
    """

    :param request:
    :param pk:
    Used to change the book details
    """
    book = BookModel.objects.get(pk=pk)
    form = BookForm(request.POST or None, instance=book)
    if request.method == 'GET':
        return render(request, "books/edit/index.html",{"form":form,"book":book})
    if request.method == 'POST':
        form = BookForm(request.POST or None,request.FILES, instance=book)
        if form.is_valid():
            form.save()
            return redirect("/book-ui/books-list/")
    else:
        return JsonResponse({"status": False, "message": "Invalid Request"})

@login_required
def viewbook(request,pk=None):
    """
    :param request:
    :param pk:
    Used to view the details of a particular book
    """
    books = BookModel.objects.get(pk=pk)
    form = BookForm(request.POST or None, instance=books)
    if request.method == 'GET':
        return render(request, "books/View/index.html",{"form":form})


@api_view(('GET','POST'))
@renderer_classes([JSONRenderer])
def formcontrol(request):
    form = Demoform(request.POST or None)
    if request.method == 'POST':
        print("CALLING YOU")
        if form.is_valid():
            print('valid form')
            form.save()
            return  render(request,'demoform.html')
            #return Response({'status':"Done"})
        return Response({'status':"Invalid"})
    return  render(request,'demoform.html',{'form':form})


@api_view(["GET","POST"])
@permission_classes([IsAdminUser])
@renderer_classes([JSONRenderer])
def bookform(request):
    """

    :param request:
    Used to create a Book using A BOOKForm
    """
    form = BookForm(request.POST or None)
    if request.method == 'POST':
        print("*****************************************************************************")
        print(request.POST.get('name'))
        form = BookForm(request.POST or None,request.FILES)
        print("CALLING YOU",request.POST)
        if form.is_valid():
            print('valid form')
            form.save()
            #return  render(request,'demoform.html')
            return redirect("/book-ui/books-list/")
        return Response({'status':"Invalid"})
    else:
        authors = AuthorModel.objects.all().order_by('first_name','last_name')
        publishers = PublisherModel.objects.all().order_by('name')
        return  render(request,'books/add/index.html',{"authors":authors,"publishers":publishers,"form":form})


################################################ PHRASE ##########################################################

@renderer_classes([JSONRenderer])
# @api_view(['GET', 'POST', 'DELETE'])
@csrf_exempt
@login_required
def listphrase(request,pk=None,bookid=None):
    """

    :param request:
    :param pk:
    :param bookid:
    This view is used to list Create and delete a phrase on GET,POST, DELETE method respectively
    """
    if request.method == 'GET':
        book = BookModel.objects.get(pk=bookid)
        print("bookdata",book.description)
        import os
        from config import settings
        print("directory",settings.MEDIA_ROOT)
        phrases= PhrasesModel.objects.filter(book__pk=bookid)
        # phras = PhrasesModel.objects.get(pk=35)
        return render(request, "books/details/index.html",{"phrases":phrases,"bookid":bookid,"book":book,"download":settings.MEDIA_ROOT})
    if request.method == 'DELETE':
        if PhrasesModel.objects.filter(pk=pk).delete():
            print("Object Found")
            return JsonResponse({"status":True,"message":"Phrase Successfully Deleted"})

    else:
        try :
            form = PhraseForm(request.POST or None, request.FILES)
            print("clear Form", form.is_valid())
            if form.is_valid():
                # if request.FILES['object']:
                #     handle_uploaded_file(request.FILES['object'])
                form.save()
                return redirect("/book-ui/{}/phrase-list/".format(bookid))
        except:
            return JsonResponse({"status": False, "message": "Invalid Request"})

@api_view(["GET","POST"])
@permission_classes([IsAdminUser])
def editphrase(request,pk=None,bookid=None):
    """

    :param request:
    :param pk:
    :param bookid:
    This view allows admin to ediit a phrase of a particular book
    """
    phrase = PhrasesModel.objects.get(pk=pk)
    if request.method == 'GET':
        form = PhraseForm(instance=phrase)
        return render(request, "books/details/edit/index.html",{"form":form,"phrase":phrase,"bookid":bookid})
    if request.method == 'POST':
        form = PhraseForm(request.POST or None, request.FILES, instance=phrase)
        print("post phrase", phrase.object)
        if form.is_valid():
            # if  request.FILES.get('object', False):
            # # if request.FILES['object']:
            #     handle_uploaded_file(request.FILES['object'])
            form.save()
            return redirect("/book-ui/{}/phrase-list/".format(bookid))
    else:
        return JsonResponse({"status": False, "message": "Invalid Request"})


# def viewphrase(request,pk=None):
#     print("Viewbook called")
#     books = PhrasesModel.objects.get(pk=pk)
#     form = PhraseForm(request.POST or None, instance=books)
#     if request.method == 'GET':
#         return render(request, "books/View/index.html",{"form":form})




@api_view(('GET','POST'))
@permission_classes([IsAdminUser])
@renderer_classes([JSONRenderer])
def phraseform(request,bookid=None):
    """

    :param request:
    :param bookid:
    This view is used to create a phrase for a particular book
    """
    book = BookModel.objects.get(pk=bookid)
    form = PhraseForm(request.POST or None,request.FILES)
    if request.method == 'POST':
        print("clear Form",form)
        if form.is_valid():
            if request.FILES['object']:
                handle_uploaded_file('media/phrases_object/'+request.FILES['object'].name)
            form.save()
            #return  render(request,'demoform.html')
            return redirect("/book-ui/{}/phrase-list/".format(bookid))
        return Response({'status':"Invalid"})
    else:
        return  render(request,'books/details/add/index.html',{"book":book,"form":form})


###############################################    publisher     ####################################################

@api_view(('GET','POST'))
@permission_classes([IsAdminUser])
@renderer_classes([JSONRenderer])
def publisherform(request):
    """
    :param request:
    This views is used to render Publisher form to create a publisher
    """
    form = PublisherForm(request.POST or None)
    if request.method == 'POST':
        print("clear Form",form)
        if form.is_valid():
            form.save()
            #return  render(request,'demoform.html')
            return redirect("book-ui:ui-book-publisher-list")
            # return Response({'status': "Done"})
        return Response({'status':"Invalid"})
    else:
        return  render(request,'publishers/add/index.html',{"form":form})

@api_view(('GET','POST'))
@permission_classes([IsAdminUser])
def editpublisher(request,pk=None):
    """

    :param request:
    :param pk:
    Allows a publisher to be edited
    """
    publisher = PublisherModel.objects.get(pk=pk)
    form = PublisherForm(instance=publisher)
    if request.method == 'GET':

        return render(request, "publishers/edit/index.html",{"form":form})
    if request.method == 'POST':
        form = PublisherForm(request.POST or None,instance=publisher)
        if form.is_valid():
            form.save()
            return redirect("book-ui:ui-book-publisher-list")
        return Response({'status': "invalid Form"})
            # return redirect("/book-ui/books-list/")
    else:
        return JsonResponse({"status": False, "message": "Invalid Request"})


def download(request,filename):
    """

    :param request:
    :param filename:
    this is used to download the 3d contents of phrase
    """
    return serve(request, filename,settings.MEDIA_ROOT)


@renderer_classes([JSONRenderer])
# @api_view(['GET', 'POST', 'DELETE'])
@csrf_exempt
@login_required
def listpublishers(request,pk=None):
    """

    :param request:
    :param pk:
    lists all the publisher on GET method and particular publisher can be deleted using DELETE method
    """
    if request.method == 'GET':
        publisher= PublisherModel.objects.all()
        return render(request, "publishers/index.html",{"publisher":publisher})
    if request.method == 'DELETE':
        print("Object Found", PublisherModel.objects.filter(pk=pk))
        if PublisherModel.objects.filter(pk=pk).delete():
            return JsonResponse({"status":True,"message":"Publisher Successfully Deleted"})
    else:
        return JsonResponse({"status": False, "message": "Invalid Request"})


@renderer_classes([JSONRenderer])
# @api_view(['GET', 'POST', 'DELETE'])
@csrf_exempt
@login_required
def listauthors(request,pk=None):
    """
    :param request:
    :param pk:
    lists all the author on GET method and particular author can be deleted using DELETE method
    """
    if request.method == 'GET':
        authors= AuthorModel.objects.all()
        return render(request, "authors/index.html",{"authors":authors})
    if request.method == 'DELETE':
        if AuthorModel.objects.filter(pk=pk).delete():
            print("Object Found")
            return JsonResponse({"status":True,"message":"Author Successfully Deleted"})
    else:
        return JsonResponse({"status": False, "message": "Invalid Request"})



@api_view(('GET','POST'))
@permission_classes([IsAdminUser])
def editauthor(request,pk=None):
    """

    :param request:
    :param pk:
    :return: Redirects to author list

    Allows author information to be edited like first name,last name and Author Image
    """
    author = AuthorModel.objects.get(pk=pk)
    form = AuthorForm(instance=author)
    if request.method == 'GET':
        print("Form",form["last_name"])
        return render(request, "authors/edit/index.html",{"form":form})
    if request.method == 'POST':
        form = AuthorForm(request.POST or None,instance=author)
        if form.is_valid():
            form.save()
            return redirect("book-ui:ui-book-author-list")
        return Response({'status': "invalid Form"})
            # return redirect("/book-ui/books-list/")
    else:
        return JsonResponse({"status": False, "message": "Invalid Request"})



@api_view(('GET','POST'))
@permission_classes([IsAdminUser])
@renderer_classes([JSONRenderer])
def addauthor(request):
    """

    :param request:
    :return: USed to Render a Author Form on Get Request which is used to create an author on POST request
    :redirect: To book list
    """
    form = AuthorForm(request.POST or None)
    if request.method == 'POST':
        form = AuthorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            #return  render(request,'demoform.html')
            return redirect("book-ui:ui-book-author-list")
            # return Response({'status': "Done"})
        return Response({'status':"Invalid"})
    else:
        return  render(request,'authors/add/index.html',{"form":form})


@api_view(('GET','POST'))
@renderer_classes([JSONRenderer])
def bookdownload(request,pk):
    """
    :param request:
    :param pk:
    :return: A Json file which contains a detailed info about the particular Book
    """
    book = BookModel.objects.filter(pk=pk)
    bookserializeobj = BookSerializer(book, many=True)
    print("bookserializeobj",bookserializeobj)
    return Response({"Book":bookserializeobj.data})

# @renderer_classes([JSONRenderer])
# # @api_view(['GET', 'POST', 'DELETE'])
# @csrf_exempt
# def BookDetails(request,pk=bookid):
#     if request.method == 'GET':
#         book= BookModel.objects.get(pk=bookid)
#         author=AuthorModel.object.get(pk=book.author)
#         publisher = PublisherModel.object.get(pk=book.publisher)
#         print("BOOK",book)
#         print("Author",author)
#         print("Publisher",publisher)
#
#         return JsonResponse({"status":True,"message":"Book Successfully Viewed"})

# def error_404_view(request,exception):
#     return render(request,"404.html")