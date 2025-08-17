# api/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TowerViewSet

router = DefaultRouter()
router.register(r'towers', TowerViewSet, basename='tower')

urlpatterns = [
    path('', include(router.urls)),
]