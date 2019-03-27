from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import routers
from .api import views as api_views

router = routers.DefaultRouter()
router.register(r'accounts', api_views.AccountViewSet)
router.register(r'groups', api_views.GroupViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
