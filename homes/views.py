from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response


from django.contrib.auth.models import Permission


# home model
from homes import models


# Authentication
from example_2.authentcation import Authentication


# Create your views here.

class HomeView(APIView):
    
    authentication_classes = [Authentication]
    
    def get(self, request, format=None):
        return Response({"data": "home_get"})
    
    def post(self, request, format=None):
        
        home_obj=models.Home(direccion=request.data['direccion'])
        home_obj.save()
        
        return Response({"data": "home_post"})
    
    def put(self, request, format=None):
        """se asignará un permiso a un usuario en específico"""
        
        perm = Permission.objects.get(codename='add_groupobjectpermission')
        
        request.user.user_permissions.add(perm)
        
        return Response({"data": "ok"})
        
        
        