from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Card(models.Model):
    title=models.CharField(("Başlık"), max_length=50)
    text=models.TextField(("İçerik"), max_length=1500)
    image=models.FileField((""), upload_to=None, max_length=100)
    active=models.BooleanField(("Göster"))
    category=models.CharField(("Kategori"), max_length=50)

    def __str__(self):
        return self.title


class Contact(models.Model):
    name=models.CharField(("İsim"), max_length=50)
    email=models.EmailField(("e-mail"), max_length=254)
    title=models.CharField(("Başlık"), max_length=50)
    text=models.TextField(("Mesaj"),max_length=1500)

    def __str__(self):
        return self.name


class Comment(models.Model):
    name=models.CharField(("İsim"), max_length=50)
    email=models.EmailField(("e-mail"), max_length=254)
    text=models.TextField(("Mesaj"),max_length=1500)
    product=models.ForeignKey(Card, verbose_name=("Ürün"), on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class UserInfo(models.Model):
    user=models.ForeignKey(User, verbose_name=("Kullanıcı"), on_delete=models.CASCADE)
    job=models.CharField(("İş"), max_length=50,default="-")
    image=models.FileField(("Profil Resmi"), upload_to=None, max_length=100, blank=True)
    tel=models.CharField(("Telefon"), max_length=50, default="-")
    password=models.CharField(("Şifre"), max_length=50)
    address=models.TextField(("Adres"),max_length=1500, default="-")