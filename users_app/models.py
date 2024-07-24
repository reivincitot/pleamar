from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(
        max_length=20, null=False, blank=False, verbose_name="Nombre"
    )
    last_name = models.CharField(
        max_length=100, null=False, blank=False, verbose_name="Apellidos"
    )
    birth_day = models.DateField(
        null=True, blank=True
        )
    address = models.CharField(null=True, blank=True, verbose_name="Dirección")
    phone_number = models.CharField(
        max_length=12, blank=False, null=False, verbose_name="Número de teléfono"
    )
    group = models.ForeignKey(
        "auth.Group",
        verbose_name="Puesto",
        on_delete=models.SET_DEFAULT,
        default=1,
        related_name="custom_users",
    )
    email = models.EmailField(
        unique=True, null=False, blank=False, verbose_name="Correo electrónico"
    )

    class Meta:
        verbose_name = "Usuario personalizado"
        verbose_name_plural = "Usuarios personalizados"

    groups = models.ManyToManyField(
        "auth.Group",
        verbose_name="groups",
        blank=True,
        related_name="custom_user",
        related_query_name="custom_user",
    )

    user_permissions = models.ManyToManyField(
        "auth.Permission",
        verbose_name="User permission",
        blank=True,
        related_name="custom_user_permissions",
        related_query_name="custom_user_permissions",
    )
