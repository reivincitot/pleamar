from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=20, null=False, blank=False, verbose_name="Nombre")
    last_name = models.CharField(max_length=100, null=False, blank=False, verbose_name='Apellidos')
    birth_day = models.DateField(null=False, blank=False, verbose_name='Fecha de nacimiento')
    address = models.CharField(null=True, blank=True, verbose_name='Dirección')
    phone_number = models.CharField(max_length=12, blank=False, null=False, verbose_name='Número de teléfono')
    group = models.ForeignKey('auth.Group',verbose_name='Puesto', on_delete=models.SET_DEFAULT,default=1)
    email = models.EmailField(unique=True, null=False, blank=False, verbose_name='Correo electrónico')

    class Meta:
        verbose_name = 'Usuario personalizado'
        verbose_name_plural = 'Usuarios personalizados'

    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        related_name='customuser_set',
        related_query_name='customuser'
    )

    user_permissions= models.ManyToManyField(
        'auth.Permission',
        verbose_name= 'user permission',
        blank=True,
        related_name='customuser_set',
        related_query_name='customuser'
    )
