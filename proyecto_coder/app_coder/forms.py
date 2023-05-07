from django import forms

class pasajeroformulario(forms.Form):
    Nombre=forms.CharField(max_length=20)
    Apellido=forms.CharField(max_length=30)
    Identificación=forms.CharField(max_length=10)
    Email=forms.EmailField()
    Fecha_de_nacimiento=forms.DateField(input_formats=['%d/%m/%Y'])
    
        
        
class hotelesformulario(forms.Form):
    Codigo_de_reserva=forms.CharField(max_length=30)
    Nombre_del_hotel=forms.CharField(max_length=30)
    Dirección=forms.CharField(max_length=30)
    Identificación_del_pasajero=forms.CharField(max_length=10)
    Ciudad=forms.CharField(max_length=30)
    Fecha_de_ingreso=forms.DateField(input_formats=['%d/%m/%Y'])
    Cantidad_de_noches=forms.IntegerField()
    Contacto_email=forms.EmailField()

    
class viajesformulario(forms.Form):
    Codigo_de_reserva=forms.CharField(max_length=10)
    Origen=forms.CharField(max_length=40)
    Destino=forms.CharField(max_length=40)
    Fecha_de_partida=forms.DateField(input_formats=['%d/%m/%Y'])
    Pasajero_ID=forms.CharField(max_length=10)
    Cantidad_de_pasajeros=forms.IntegerField()
    Comentarios=forms.CharField(max_length=300)