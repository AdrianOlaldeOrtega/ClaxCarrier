# Generated by Django 4.0 on 2022-05-19 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tienda', '0003_delete_producto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150)),
                ('descripcion', models.TextField()),
                ('precio', models.FloatField()),
                ('categoria', models.CharField(max_length=50)),
                ('stock', models.IntegerField()),
            ],
        ),
    ]
