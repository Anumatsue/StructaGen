# api/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TowerViewSet, ReportViewSet

router = DefaultRouter()
router.register(r'towers', TowerViewSet, basename='tower')
router.register(r"reports", ReportViewSet, basename="reports")

urlpatterns = [
    path('', include(router.urls)),
]