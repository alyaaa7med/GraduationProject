
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import DoctorView , PatientView 

router = DefaultRouter()
router.register(r'Doctor', DoctorView)
router.register(r'Patient',PatientView)


urlpatterns = [
   
    path('', include(router.urls)),

]