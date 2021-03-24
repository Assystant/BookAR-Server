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
    books = BookModel.objects.get(pk=pk)
    form = BookForm(request.POST or None, instance=books)
    if request.method == 'GET':
        return render(request, "books/edit/index.html",{"form":form})
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return JsonResponse({"status":True,"message":"Book Successfully Edited"})
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
            return Response({'status':"Done"})
        return Response({'status':"Invalid"})
    else:
        authors = AuthorModel.objects.all().order_by('name')
        publishers = PublisherModel.objects.all().order_by('name')
        return  render(request,'books/add/index.html',{"authors":authors,"publishers":publishers,"form":form})


################################################ PHRASE ##########################################################

@renderer_classes([JSONRenderer])
# @api_view(['GET', 'POST', 'DELETE'])
@csrf_exempt
def listphrase(request,pk=None):
    if request.method == 'GET':
        phrases= PhrasesModel.objects.all()
        return render(request, "books/details/index.html",{"phrases":phrases})
    if request.method == 'DELETE':
        if PhrasesModel.objects.filter(pk=pk).delete():
            print("Object Found")
            return JsonResponse({"status":True,"message":"Book Successfully Deleted"})
    else:
        return JsonResponse({"status": False, "message": "Invalid Request"})


def editphrase(request,pk=None):
    phrase = PhrasesModel.objects.get(pk=pk)
    form = PhraseForm(request.POST or None, instance=phrase)
    if request.method == 'GET':
        return render(request, "books/details/edit/index.html",{"form":form})
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return JsonResponse({"status":True,"message":"Book Successfully Edited"})
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
def phraseform(request):
    form = PhraseForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            print('valid form')
            form.save()
            #return  render(request,'demoform.html')
            return redirect("/book-ui/phrase-list/")
        return Response({'status':"Invalid"})
    else:
        books = BookModel.objects.all().order_by('name')
        return  render(request,'books/details/add/index.html',{"books":books,"form":form})
