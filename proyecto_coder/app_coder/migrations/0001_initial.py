from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hoteles',
            fields=[
                ('hotel_reserva', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('hotel_nombre', models.CharField(max_length=30)),
                ('hotel_direccion', models.CharField(max_length=30)),
                ('hotel_pasajero_id', models.CharField(max_length=10)),
                ('hotel_ciudad', models.CharField(max_length=30)),
                ('hotel_fecha_ini', models.DateField()),
                ('hotel_cant_noches', models.IntegerField()),
                ('hotel_contacto', models.EmailField(blank=True, max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Pasajero',
            fields=[
                ('pasajero_nombre', models.CharField(max_length=20)),
                ('pasajero_apellido', models.CharField(max_length=30)),
                ('pasajero_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('pasajero_mail', models.EmailField(max_length=254)),
                ('pasajero_fecha_nac', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='viajes',
            fields=[
                ('viajes_reserva', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('viajes_origen', models.CharField(max_length=40)),
                ('viajes_destino', models.CharField(max_length=40)),
                ('viajes_fecha_ini', models.DateField()),
                ('viajes_pasajero_id', models.CharField(max_length=10)),
                ('viajes_cant_pasajeros', models.IntegerField()),
                ('viajes_comentarios', models.CharField(blank=True, max_length=300)),
            ],
        ),
    ]