from rest_framework import permissions
from django.contrib.auth.decorators import user_passes_test, permission_required

class BlocklistPermission(permissions.BasePermission):
    """
    Global permission check for blocked IPs.
    """

    
    def has_permission(self, request, view):
        user=request.user


        print(f'method:  *{request.method}')
        
        print(user.is_authenticated)
        print(f'** desde permissions: {request.user}')
        print(user.has_perms(''))
        return False
    
def check_perms(data_type, perms):
    def display_arguments(func):
        def display_and_call(*args, **kwargs):  
            print(perms)
            args = list(args)
            print('must-have arguments are:')
            for i in args:
                print(i)
            print('optional arguments are:')
            for kw in kwargs.keys():
                print( kw+'='+str( kwargs[kw] ))
            return Response({"data":"El usuario no tiene permisos"})          
            return func(*args, **kwargs)
        return display_and_call
    return display_arguments