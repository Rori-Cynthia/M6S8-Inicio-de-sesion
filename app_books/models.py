from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class AccountUser(AbstractUser):
    email = models.EmailField(
        unique=True,
        error_messages={
            'unique': "El correo electrónico ya está registrado. Por favor, usa otro.",
        }
    )

    def __str__(self):
        return self.username


class Book(models.Model):
    title = models.CharField(
        max_length=150,
        verbose_name="Título"
    )
    author = models.CharField(
        max_length=150,
        verbose_name="Autor"
    )
    valuation = models.IntegerField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(10000),
        ],
        verbose_name="Valoración"
    )

    def __str__(self):
        return f"{self.title} - {self.author}"
