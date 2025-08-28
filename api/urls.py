# api/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
<<<<<<< HEAD
from .views import TowerViewSet, AntennaViewSet, StressResultViewSet, ReportViewSet
=======
from .views import TowerViewSet, ReportViewSet
>>>>>>> feature/reports-api

router = DefaultRouter()

router.register(r'towers', TowerViewSet, basename='tower')
<<<<<<< HEAD
router.register(r"antennas", AntennaViewSet, basename="antennas")
router.register(r"stress", StressResultViewSet, basename="stress")
=======
>>>>>>> feature/reports-api
router.register(r"reports", ReportViewSet, basename="reports")

urlpatterns = [
    path('', include(router.urls)),
]