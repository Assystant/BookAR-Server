from django.shortcuts import render
from rest_framework.response import Response
# Create your views here.
from .forms import Demoform, BookForm, PhraseForm
from book_api.models import AuthorModel, PublisherModel, BookModel,PhrasesModel
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect
from django.urls import reverse


def handle_uploaded_file(f):
    with open('3dObjects/'+f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


@renderer_classes([JSONRenderer])
# @api_view(['GET', 'POST', 'DELETE'])
@csrf_exempt
def lbooks(request,pk=None):
    if request.method == 'GET':
        books= BookModel.objects.all()
        return render(request, "books/index.html",{"books":books})
    if request.method == 'DELETE':
        if BookModel.objects.filter(pk=pk).delete():
            print("Object Found")
            return JsonResponse({"status":True,"message":"Book Successfully Deleted"})
    else:
        return JsonResponse({"status": False, "message": "Invalid Request"})


def editbook(request,pk=None):
    book = BookModel.objects.get(pk=pk)
    form = BookForm(request.POST or None, instance=book)
    if request.method == 'GET':
        return render(request, "books/edit/index.html",{"form":form,"book":book})
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect("/book-ui/books-list/")
    else:
        return JsonResponse({"status": False, "message": "Invalid Request"})


def viewbook(request,pk=None):
    print("Viewbook called")
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


@api_view(('GET','POST'))
@renderer_classes([JSONRenderer])
def bookform(request):
    form = BookForm(request.POST or None)
    if request.method == 'POST':
        print(request.POST.get('name'))
        print("CALLING YOU")
        if form.is_valid():
            print('valid form')
            form.save()
            #return  render(request,'demoform.html')
            return redirect("/book-ui/books-list/")
        return Response({'status':"Invalid"})
    else:
        authors = AuthorModel.objects.all().order_by('name')
        publishers = PublisherModel.objects.all().order_by('name')
        return  render(request,'books/add/index.html',{"authors":authors,"publishers":publishers,"form":form})


################################################ PHRASE ##########################################################

@renderer_classes([JSONRenderer])
# @api_view(['GET', 'POST', 'DELETE'])
@csrf_exempt
def listphrase(request,pk=None,bookid=None):
    if request.method == 'GET':
        print("bookid",bookid)
        phrases= PhrasesModel.objects.filter(book__pk=bookid)
        return render(request, "books/details/index.html",{"phrases":phrases,"bookid":bookid})
    if request.method == 'DELETE':
        if PhrasesModel.objects.filter(pk=pk).delete():
            print("Object Found")
            return JsonResponse({"status":True,"message":"Book Successfully Deleted"})

    else:
        try :
            form = PhraseForm(request.POST or None, request.FILES)
            print("clear Form", form.is_valid())
            if form.is_valid():
                print("equest.FILES",request.FILES)
                print("request.FILES", request.POST)
                if request.FILES['object']:
                    handle_uploaded_file(request.FILES['object'])
                form.save()
                return redirect("/book-ui/{}/phrase-list/".format(bookid))
        except:
            return JsonResponse({"status": False, "message": "Invalid Request"})


def editphrase(request,pk=None,bookid=None):
    phrase = PhrasesModel.objects.get(pk=pk)
    if request.method == 'GET':
        form = PhraseForm(instance=phrase)
        return render(request, "books/details/edit/index.html",{"form":form,"phrase":phrase,"bookid":bookid})
    if request.method == 'POST':
        form = PhraseForm(request.POST or None, request.FILES, instance=phrase)
        if form.is_valid():
            if request.FILES['object']:
                handle_uploaded_file(request.FILES['object'])
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
@renderer_classes([JSONRenderer])
def phraseform(request,bookid=None):
    book = BookModel.objects.get(pk=bookid)
    form = PhraseForm(request.POST or None,request.FILES)
    print("book",book)
    if request.method == 'POST':
        print("clear Form",form)
        if form.is_valid():
            if request.FILES['object']:
                handle_uploaded_file(request.FILES['object'])
            form.save()
            #return  render(request,'demoform.html')
            return redirect("/book-ui/{}/phrase-list/".format(bookid))
        return Response({'status':"Invalid"})
    else:
        print(vars(book))
        return  render(request,'books/details/add/index.html',{"book":book,"form":form})
