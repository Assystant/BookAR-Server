from django.views.generic import TemplateView
from django.urls import path, include, re_path
# from .views import SettingsView
from rest_framework import routers

router = routers.SimpleRouter()

urlpatterns = [
    path('',include(router.urls)),
    # path('settings/', SettingsView, name="settings"),
]