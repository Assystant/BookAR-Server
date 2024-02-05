from django.views.generic import TemplateView
from django.urls import path, include, re_path
from rest_framework import routers
from . import views

from rest_framework_extensions.routers import NestedRouterMixin


class NestedSimpleRouter(NestedRouterMixin, routers.SimpleRouter):
    """
    A router class that extends both NestedRouterMixin and SimpleRouter.
    This allows for nested routing, where child routes can be nested under parent routes.
    """
    pass
router = NestedSimpleRouter()
(
    router.register(r'book', views.BookAPIViewSet, basename='book')
          .register(r'phrases',
                    views.PhraseAPIViewSet,
                    basename='phrases',
                    parents_query_lookups=['book_id'])
#
)
# router = routers.SimpleRouter()
# router = DefaultRouter()
# router.register(r'book', views.BookViewSet)
# router.register(r'phrase', views.PhraseViewSet)
# router.register(r'books', views.BookAPIViewSet)
# router.register(r'phrases', views.PhraseAPIViewSet)

#working
router.register(r'student', views.StudentAPIViewset)
router.register(r'author', views.AuthorAPIViewset)
router.register(r'publishers', views.PublisherAPIViewset)

urlpatterns = [

    path('',include(router.urls)),
    path('test/',views.test,name='test'),
    # path('publishers/',views.listPublishersViews.as_view(),name="publisherlist"),
    # path('publishers-add/',views.add_publisher,name="publishers-add"),
    # path('publishers-edit/<pk>/',views.EditPublishersViews.as_view(),name="publisheredit"),
    # path('publishers-delete/<pk>/',views.PublisherDelete.as_view(),name="publishers-delete"),

    # path('book-list/',views.BooksViews.as_view(),name="booklist"),
    # path('edit/<pk>/',views.BookEdit.as_view(),name="book-edit"),
    # path('view/<pk>/',views.BookView.as_view(),name="book-view"),
    # path('delete/<pk>/',views.BookDelete.as_view(),name="book-delete"),

    # path('author-list/', views.listAuthorsViews.as_view(), name="authorlist"),
    # path('authors-add/',views.add_author,name="authors-add"),
    # path('authors-edit/<pk>/', views.EditAuthorssViews.as_view(), name="authoredit"),
    # path('authors-delete/<pk>/', views.AuthorDelete.as_view(), name="authors-delete"),
    # path('/book-list/edit/',views.edit_book),
    # path('phrase-list/',views.BooksViews.as_view()),
    # path('publisher-list/',views.BooksViews.as_view()),
    # path('add/',views.add_book,name="book-add")

    # path('settings/', SettingsView, name="settings"),
]