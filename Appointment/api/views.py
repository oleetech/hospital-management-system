from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from Appointment.models import Appointment, Visit
from .serializers import AppointmentSerializer, VisitSerializer
from .permissions import HasAppointmentPermission

class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, HasAppointmentPermission]

class VisitViewSet(viewsets.ModelViewSet):
    queryset = Visit.objects.all()
    serializer_class = VisitSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, HasAppointmentPermission]
