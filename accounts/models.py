from django.db import models
from django.contrib.auth.models import AbstractBaseUser  ,PermissionsMixin 
from django.utils.translation import gettext_lazy as _ 
from .managers import CustomUserManger 
import secrets 

class User(AbstractBaseUser,PermissionsMixin) :
    #Limit the values the 1st is the actual will stored in the database , but the 2nd is the readable in the admin 
    ROLE_CHOICES =[
        ('doctor','Doctor'),
        ('patient','Patient'),
        ('guest','Guest')
    ] 
    name = models.CharField(max_length=200)
    email=models.EmailField(max_length=250,unique=True,blank=False,null = False) # should be unique 
    password = models.CharField(max_length=150)  # Increase the maximum length to 128 characters
    is_staff = models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)  
    role =models.CharField(max_length = 10, choices = ROLE_CHOICES ,default='guest' )


    USERNAME_FIELD= "email"
    REQUIRED_FIELDS= ["name","password"]  # required fields you need to create an account

    objects = CustomUserManger()

    # class Meta : 
    #     verbose_name = _("User")
    #     verbose_name_plural = _("Users")

    def __str__(self) :
        return self.email
    
   

class otpcode(models.Model): 
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    otp=models.CharField(max_length=6, default = secrets.token_hex(3)[:5])
    otp_created_at = models.DateTimeField(auto_now_add = True )
    otp_expires_at = models.DateTimeField(blank= True , null = True) # why ? 


# not all relations have been added ^_^    
class Doctor(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    phone= models.CharField(max_length=15)
    syndicateNo = models.CharField(max_length=15)
    university = models.CharField(max_length=30)
    specialization = models.CharField(max_length=255)
    work_experience= models.CharField(max_length=255)
    gender= models.CharField(max_length=7)
    image = models.ImageField(upload_to="accounts/images/%Y/%m/%d/%H/%M/%S/", null=True, default="accounts/images/carton.png")

    REQUIRED_FIELDS= ["phone","syndicateNo","university","specialization"]  # null = False + blank = False 



class Patient(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    phone= models.CharField(max_length=15)
    birthdate = models.DateField()
    gender= models.CharField(max_length=7,default='unknown')

    REQUIRED_FIELDS= ["phone"]  # null = False + blank = False 


