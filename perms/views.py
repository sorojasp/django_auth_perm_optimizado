from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

# group
from django.contrib.auth.models import Group

# Content type
from django.contrib.contenttypes.models import ContentType

# Permission
from django.contrib.auth.models import Permission

# Create your views here.

from homes import models


# Authentication
from example_2.authentcation import Authentication


#login required decorator
from django.contrib.auth.decorators import login_required, permission_required

#method decorator
from django.utils.decorators import method_decorator



def search_perms_group(groups, request, wanted_perm)-> bool:
    """function that """
    permiso_encontrado:bool=False
    for group in request.user.groups.all():
    
        print(group)
        permissions = group.permissions.all()
        for perm in permissions:
                    
            print(f'from group perms - codename: {perm.codename}')
            print(f'from group perms - perm over: {perm.content_type}')
            print(f'{perm.content_type}.{perm.codename}')
            
            if f'{perm.content_type}.{perm.codename}' == wanted_perm:
                permiso_encontrado=True
                return permiso_encontrado
                
    return permiso_encontrado        

def search_perms_user(request, wanted_perm)-> bool:
    permiso_encontrado:bool=False
    for perm in request.user.user_permissions.all():
        print(f'from group perms - codename: {perm.codename}')
        print(f'from group perms - perm over: {perm.content_type}')
        print(f'{perm.content_type}.{perm.codename}')
        if f'{perm.content_type}.{perm.codename}' == wanted_perm:
                permiso_encontrado=True
                return permiso_encontrado
    return permiso_encontrado     
    


def my_login_required(method):#get the method like a argument of wrapper
    def wrapper(ref, request=None):
           
        if request.user.is_authenticated:
            return method(ref, request)# execute the method wrapped with arguments
                                       #so, the method like return
        else:
            return Response({"resp":"the user is not authenticated"}, status=403)   
    return wrapper




def my_perms_required(data_type, perms):
    def wrapper_arguments(method):
        def wrapper(ref, request=None):
           
            if (search_perms_group(request.user.user_permissions.all(),request,perms[0]) or search_perms_user(request,perms[0])) is True:
                return method(ref, request)
            return Response({"resp": "El usuario no tiene permisos"})
        
        return wrapper

    return wrapper_arguments





class PermsView(APIView):

    authentication_classes = [Authentication]

    #@my_login_required
    #@my_perms_required(list, ["home.can_create_home"])
    def get(self,request,name={"name":"Stiven"}, format=None):
        """asignación de grupos a los usuarios"""
                
        print(f"from get method: {request.user.__str__()}")
        
        print(request.data['name_perm'])

        perm = Permission.objects.get(codename=request.data['name_perm'])# ** get a perm **
        
        request.user.user_permissions.add(perm)#  ** add permsissions to a user **
        
        request.user.save()

        print(Permission.objects.filter(user=request.user))
        
        for group in request.user.groups.all():
            print(f'group: {group}, perm: {Permission.objects.filter(group=group)}')
        
        print(f"groups of {request.user}: ", list(request.user.groups.all()))
        print(f"individual permissions{request.user.user_permissions.all()}")
        print(request.user)
        
        return Response({"data": None,
                         "permissions": None,
                         "auth":request.user.is_authenticated
                         },)
        
        
    
    def post(self, request, format=None, *args, **kwargs):
        """se crea un grupo de permisos y guarda en base de datos"""

        group = Group(name=request.data['name_group'])
        group.save()
        return Response({"data": request.data})

    def patch(self, request, format=None, *args, **kwargs):
        """método para crear el permiso"""

        content_type = ContentType.objects.get_for_model(models.Home)
        permission = Permission.objects.create(
            codename=request.data['codename'],
            name=request.data['name'],
            content_type=content_type,
        )
        permission.save()
        return Response({"data": "OK"})
    
    
    #@method_decorator(check_perms(list, ["2", "45"]))
    @my_login_required
    def put(self, request, format=None):
        """método para crear el grupo"""
        

        group = Group.objects.get(name=request.data['name_group'])
        perm = Permission.objects.get(codename='can_add_home')
        print(perm)
        print(group)
        group.permissions.add(perm)
        group.save()
        Permission.save
        return Response({"data": "group"})

    def delete(self, request, format=None,):
        """asignación de permisos a los grupos"""

        my_group = Group.objects.get(name=request.data['name_group']) #get group

        perm = Permission.objects.get(codename=request.data['name_perm'])#get permission

        my_group.permissions.add(perm) # asign permission to a group

        return Response({"data": "delete"})
    def getName(self, request, format=None):
        return "su puta madre"
