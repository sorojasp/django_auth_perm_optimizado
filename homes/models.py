from django.db import models

# Create your models here.

from django.db import models


class Home(models.Model):
    id=models.AutoField(primary_key=True)
    direccion=models.CharField(max_length=255)
    
    class Meta:
        permissions = (
            ('update_home', 'Update Home'),
        )
    

    

