
from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Doctor , Patient 
User = get_user_model()


class CreateUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id','name','email','password'] 

    def create(self, validated_data):
        password = validated_data.pop("password", None)
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user

    def update(self, instance, validated_data):
        password = validated_data.pop("password", None)
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user

    def delete(self, validated_data):
        password = validated_data.pop("password", None)
        user = User(**validated_data)
        user.set_password(password)
        user.delete()
        return user

    
class DoctorSerializer(serializers.ModelSerializer):

    # to handle the user data 

    user= CreateUserSerializer() 
    confirm_password = serializers.CharField(write_only=True, required=True)
    class Meta : 
        model = Doctor   
        fields = ['id','user','confirm_password','phone','syndicateNo','specialization','university','work_experience','gender','image']
        

    def validate(self, data):
        if data['user']['password'] != data['confirm_password']:
            raise serializers.ValidationError("The passwords do not match.")
        return data
    
    # during deserialization 
    def create(self, validated_data): # validated data = user + doctor 
        user_data = validated_data.pop('user') # This line extracts the nested user data from the validated data dictionary. Since user is a nested serializer field, it's removed from validated_data and stored separately in user_data.
        validated_data.pop('confirm_password') # Remove 'confirm_password' from the data
        user = User.objects.create(**user_data, role='doctor') # Here, a new User instance is created using the extracted user data (user_data). Additionally, the role attribute is set to 'doctor', indicating that this user instance represents a doctor.
        doctor = Doctor.objects.create(user=user,**validated_data)  # validated data does not have user 
        return doctor
    

   
    
class PatientSerializer(serializers.ModelSerializer):
 
    user= CreateUserSerializer() 
    confirm_password = serializers.CharField(write_only=True, required=True)
    class Meta : 
        model = Patient
        fields =['id','user','confirm_password','gender','birthdate']

    
    def validate(self, data):
        if data['user']['password'] != data['confirm_password']:
            raise serializers.ValidationError("The passwords do not match.")
        return data

    def create(self, validated_data): 
        user_data = validated_data.pop('user') 
        validated_data.pop('confirm_password') # Remove 'confirm_password' from the data
        user = User.objects.create(**user_data, role='patient')
        patient = Patient.objects.create(user=user,**validated_data) 
        return patient

   

   