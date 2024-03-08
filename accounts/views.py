from rest_framework import viewsets
from .models import Doctor , Patient ,User ,otpcode 
from .serializers import DoctorSerializer , PatientSerializer , EmailSerializerr 
from rest_framework.parsers import MultiPartParser , FormParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.utils import timezone
import secrets
from django.core.mail import send_mail



class DoctorView(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    parser_classes = [MultiPartParser,FormParser]



class PatientView(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    
 


@api_view(['POST'])
def SendOTP(request):
    if request.method == 'POST':
        serializer = EmailSerializerr(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            user = get_object_or_404(User, email=email)
            otp = otpcode.objects.create(user=user, otp=secrets.token_hex(3)[:5]) #  Fields that have default values or are nullable (blank=True, null=True) can be omitted if you're satisfied with the defaults or if they can be left empty.
            otp.otp_expires_at = timezone.now() + timezone.timedelta(minutes=5)  # Set OTP expiration time
            otp.save()
            
            subject="Email Code"
            message = f"""
                                here is your OTP {otp.otp} 
                                it expires in 5 minuteuse 
                                
                                """
            sender = "alyaa_ahmed@gmail.com"
            receiver = [user.email, ]
       
        
        
            # send email
            send_mail(
                subject,
                message,
                sender,
                receiver,
                fail_silently=False,
            )
  
            return Response({'message': 'OTP sent successfully'}, status=200)
    
        else:
            errors = serializer.errors
            return Response(errors, status=400)
    return Response({'message': 'Not allowed http method'}, status=405)
