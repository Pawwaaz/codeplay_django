from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Pendaftaran(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    kelas = models.CharField(max_length=50, choices=[('kelas1', 'Usia anak 6-11 th'), ('kelas2', 'Usia anak 11-18 th')])

    def __str__(self):
        return self.name

# class UserProfileInfo(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)

#     portofolio_site = models.URLField(blank=True)
#     profile_pic = models.ImageField(upload_to='profile_pics', blank=True)

#     def __str__(self):
#         return self.user.username
