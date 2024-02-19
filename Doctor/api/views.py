from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from Doctor.models import Doctor, Nurse, DoctorAvailability
from .serializers import DoctorSerializer, NurseSerializer, DoctorAvailabilitySerializer
from .permissions import HasDynamicModelPermission  

class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, HasDynamicModelPermission]

class NurseViewSet(viewsets.ModelViewSet):
    queryset = Nurse.objects.all()
    serializer_class = NurseSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, HasDynamicModelPermission]

class DoctorAvailabilityViewSet(viewsets.ModelViewSet):
    queryset = DoctorAvailability.objects.all()
    serializer_class = DoctorAvailabilitySerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, HasDynamicModelPermission]
