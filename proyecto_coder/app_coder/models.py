from django.db import models

# Create your models here.

class Pasajero(models.Model):
    pasajero_nombre=models.CharField(max_length=20)
    pasajero_apellido=models.CharField(max_length=30)
    pasajero_id=models.CharField(max_length=10, primary_key=True)
    pasajero_mail=models.EmailField()
    pasajero_fecha_nac=models.DateField()  
    
class viajes(models.Model):
    viajes_reserva= models.CharField(max_length=10, primary_key=True)
    viajes_origen=models.CharField(max_length=40)
    viajes_destino= models.CharField(max_length=40)
    viajes_fecha_ini=models.DateField()  
    viajes_pasajero_id=models.CharField(max_length=10)
    viajes_cant_pasajeros=models.IntegerField()
    viajes_comentarios= models.CharField(max_length=300, blank=True)
    

class Hoteles(models.Model):
    hotel_reserva=models.CharField(max_length=30, primary_key=True)
    hotel_nombre=models.CharField(max_length=30)
    hotel_direccion=models.CharField(max_length=30)
    hotel_pasajero_id=models.CharField(max_length=10)
    hotel_ciudad=models.CharField(max_length=30)
    hotel_fecha_ini= models.DateField()
    hotel_cant_noches=models.IntegerField()
    hotel_contacto=models.EmailField(blank=True)