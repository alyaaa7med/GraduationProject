from rest_framework import viewsets  , mixins
from .models import Doctor , Patient ,User ,otpcode 
from .serializers import DoctorSerializer , PatientSerializer , EmailSerializerr 
from rest_framework.parsers import MultiPartParser , FormParser
from rest_framework.decorators import api_view , renderer_classes
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.utils import timezone
import secrets
from django.core.mail import send_mail
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework_swagger import renderers
from rest_framework import generics


class DoctorView(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    parser_classes = [MultiPartParser,FormParser]



class PatientView(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    
 

# @swagger_auto_schema(
#     method='post',
#     request_body=EmailSerializerr,
#     responses={
#         200: openapi.Response('OTP sent successfully'),
#         400: openapi.Response('Bad request, validation errors'),
#         404: openapi.Response('User not found'),
#         405: openapi.Response('Method not allowed')
#     },
#     operation_description="Send OTP code to the user's email address"
# )

class SendOTP(viewsets.ModelViewSet):
    queryset = otpcode.objects.all()
    serializer_class = EmailSerializerr
    
    def create(self, request, *args, **kwargs):
        user = get_object_or_404(User, email=request.data['email'])
        user = User.objects.get(email=request.data['email'])
        otp = otpcode.objects.create(user=user, otp=secrets.token_hex(3)[:5])
        otp.otp_expires_at = timezone.now() + timezone.timedelta(minutes=5)
        otp.save()

        subject = "Email Code"
        message = f"Here is your OTP: {otp.otp}. It expires in 5 minutes."
        sender = "alyaa_ahmed@gmail.com"
        receiver = [user.email]

        # Send email
        send_mail(
                subject,
                message,
                sender,
                receiver,
                fail_silently=False,
            )

        return Response({'message': 'OTP sent successfully'}, status=200)

