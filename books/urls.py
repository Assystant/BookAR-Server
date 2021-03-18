from django.views.generic import TemplateView
from django.urls import path, include, re_path
from rest_framework import routers
from . import views as views


router = routers.SimpleRouter()
# router = DefaultRouter()
router.register(r'book', views.BookViewSet)
router.register(r'phrase', views.PhraseViewSet)

urlpatterns = [
    path('',include(router.urls)),
    # path('settings/', SettingsView, name="settings"),
]