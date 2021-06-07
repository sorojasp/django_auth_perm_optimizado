from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

# models of user
from profile_user import models


# hasher 
from example_2.hasher.EncriptadorBcrypt import EncriptadorBcrypt

#Token
from rest_framework.authtoken.models import Token


class UserView(APIView):
    
    
    __encript_obj=EncriptadorBcrypt()
    
    
    
    def get(self, request, *args, **kwargs):
        return Response({'recibido':{
            "name":"Stiven Rojas"
        }})
        
    def post(self, request, *args, **kwargs):
        
        encrypted_password = self.__encript_obj.encriptar(request.data['password']) 
        user_obj=models.UserProfile.objects.create(email=request.data['email'],password=encrypted_password)
        user_obj.save()
        
        token, created=Token.objects.get_or_create(user=user_obj) # con este se obtiene el Token
        
        return Response({
            "ok":True,
            "data": {  
            'recibido_post':request.data,
            'token':token.key,
            'id':user_obj.id
            }
            
            })
        
    def delete(self, request, *args, **kwargs):
        pass
        
        
        
    