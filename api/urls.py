# api/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TowerViewSet

router = DefaultRouter()
router.register(r'towers', TowerViewSet, basename='tower')
<<<<<<< Updated upstream
=======
router.register(r"antennas", AntennaViewSet, basename="antennas")
router.register(r"stress", StressResultViewSet, basename="stress")
router.register(r"reports", ReportViewSet, basename="reports")
>>>>>>> Stashed changes

urlpatterns = [
    path('', include(router.urls)),
]