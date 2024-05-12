from django.db import models
from django.contrib.auth.models import AbstractUser


class CostumerUsers(AbstractUser):
    image = models.ImageField(upload_to='user_images/', blank=True, null=True, default='default_img/default.png')

    class Meta:
        db_table = 'costumuser'

    def __str__(self):
        return self.username