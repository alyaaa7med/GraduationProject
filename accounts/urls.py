
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import DoctorView , PatientView , SendOTP
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register(r'Doctor', DoctorView)
router.register(r'Patient',PatientView)
router.register(r'SendOTP',SendOTP)


urlpatterns = [
   
    path('', include(router.urls)),
    path('Login/', TokenObtainPairView.as_view(), name='token_obtain_pair'), # return access + refresh
    # path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'), # return new access
]