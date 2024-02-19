from rest_framework import serializers
from Doctor.models import Doctor, Nurse, DoctorAvailability,WeekDay

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'

class NurseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nurse
        fields = '__all__'

class DoctorAvailabilitySerializer(serializers.ModelSerializer):
    day_of_week = serializers.PrimaryKeyRelatedField(
        many=True, 
        queryset=WeekDay.objects.all()
    )

    class Meta:
        model = DoctorAvailability
        fields = '__all__'
