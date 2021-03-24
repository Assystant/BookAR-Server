from django.urls import path, include, re_path
from rest_framework import routers
from . import views as views
app_name = 'book-ui'

urlpatterns = [
# path('demoform/',views.formcontrol,name='demoforms'),#DEMO
    #Book URLS
    path('bookform/',views.bookform,name='bookform'),#ADD A BOOK
    path('books-list/',views.lbooks,name='ui-book-list'),#LIST A BOOK
    path('books-list/<pk>/',views.lbooks,name='ui-book-delete'),#DELETE A BOOK
    path('book-edit/<pk>/',views.editbook,name='ui-book-list'),
    path('book-view/<pk>/',views.viewbook,name='ui-book-list'),

    #Phrases URL
    path('phraseform/',views.phraseform,name='phraseform'),#ADD A Phrase
    path('phrase-list/', views.listphrase, name='ui-phrase-list'),  # LIST Phrase
    path('phrase-list/<pk>/', views.listphrase, name='ui-phrase-delete'),  # DELETE A BOOK
    path('phrase-edit/<pk>/', views.editphrase, name='ui-phrase-edit'),
    # path('phrase-view/<pk>/', views.viewphrase, name='ui-phrase-list'),

]