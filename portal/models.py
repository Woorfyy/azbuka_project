from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from cloudinary.models import CloudinaryField


class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,verbose_name='Пользователь')
    full_name = models.CharField(max_length=150)
    phone =models.CharField(max_length=20)

    def __str__(self):
        return self.full_name

class Mebel(models.Model):
    TITLE_CHOICES = [
        ('Д', 'Диваны'),
        ('КХ', 'Кухонные гарнитуры'),
        ('Ш', 'Шкафы'),
        ('КР', 'Кровати'),
        ('С', 'Столы'),
    ]
    AVAILABILITY_CHOICES = [
        ('Е', 'Есть'),
        ('Н', 'Нет'),
    ]
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    image = CloudinaryField('image', folder='mebel/', blank=True, null=True)
    category = models.CharField(max_length=2, choices=TITLE_CHOICES)
    availability = models.CharField(max_length=1, choices=AVAILABILITY_CHOICES)

    def __str__(self):
        return self.title