from django.urls import path, include, re_path
from rest_framework import routers
from . import views as views
app_name = 'book-ui'

urlpatterns = [
# path('demoform/',views.formcontrol,name='demoforms'),#DEMO
    #Book URLS
    path('bookform/',views.bookform,name='bookform'),#ADD A BOOK
    path('books-list/',views.lbooks,name='ui-book-list'),#LIST A BOOK
    # path('books-detail/',views.lbooks,name='ui-book-list'),#Details of A BOOK
    path('books-list/<pk>/',views.lbooks,name='ui-book-delete'),#DELETE A BOOK
    path('book-edit/<pk>/',views.editbook,name='ui-book-list'),
    path('book-view/<pk>/',views.viewbook,name='ui-book-view'),

    #Phrases URL
    path('<bookid>/phraseform/',views.phraseform,name='phraseform'),#ADD A Phrase
    path('<bookid>/phrase-list/', views.listphrase, name='ui-phrase-list'),  # LIST Phrase
    path('phrase-list/<pk>/', views.listphrase, name='ui-phrase-delete'),  # DELETE A BOOK
    path('<bookid>/phrase-edit/<pk>/', views.editphrase, name='ui-phrase-edit'),
    path('3dObjects/<filename>/', views.download, name='ui-phrase-download'),#download


    #Publisher
    path('publisherform/',views.publisherform,name='publisherform'),#ADD A Phrase
    path('publisher-edit/<pk>/',views.editpublisher,name='ui-book-publisher-edit'),
    path('publisher-list/',views.listpublishers,name='ui-book-publisher-list'),#LIST A BOOK
    path('publisher-list/<pk>/',views.listpublishers,name='ui-book-publisher-delete'),#LIST A BOOK
    # path('phrase-view/<pk>/', views.viewphrase, name='ui-phrase-list'),


    #Author
    path('author-list/',views.listauthors,name='ui-book-author-list'),
    path('author-list/<pk>/',views.listauthors,name='ui-book-author-delete'),
    path('author-edit/<pk>/',views.editauthor,name='ui-book-author-edit'),
    path('author-add/',views.addauthor,name='ui-book-author-add'),


    #book download
    path('book-download/<pk>/',views.bookdownload,name='ui-book-book-download'),
]