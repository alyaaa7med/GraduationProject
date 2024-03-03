from rest_framework import viewsets
from .models import Doctor , Patient 
from .serializers import DoctorSerializer , PatientSerializer
from rest_framework.parsers import MultiPartParser , FormParser



class DoctorView(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    parser_classes = [MultiPartParser,FormParser]



class PatientView(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

