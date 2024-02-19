from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DoctorViewSet, NurseViewSet, DoctorAvailabilityViewSet

router = DefaultRouter()
router.register(r'doctors', DoctorViewSet)
router.register(r'nurses', NurseViewSet)
router.register(r'doctor-availabilities', DoctorAvailabilityViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
