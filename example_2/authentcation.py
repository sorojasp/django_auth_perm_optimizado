
from rest_framework.response import Response
from rest_framework import authentication
from rest_framework.authtoken.models import Token
from profile_user.models import UserProfile
import json

from django.contrib.auth.models import AnonymousUser

class Authentication(authentication.BaseAuthentication):
 
    def authenticate(self, request):
  
        user_obj=AnonymousUser()
     
        
        if request.query_params.get('Authorization'):
            token_key=request.query_params.get('Authorization').split(' ')[1]
            token = Token.objects.get(key=token_key)
            user_obj=token.user
            token.user.is_authenticated=True
        
        print(user_obj)
        return (user_obj, None)
    

        
        




