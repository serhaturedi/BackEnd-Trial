# Generated by Django 4.1.7 on 2023-03-24 11:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('appMy', '0003_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job', models.CharField(default='-', max_length=50, verbose_name='İş')),
                ('image', models.FileField(blank=True, upload_to=None, verbose_name='Profil Resmi')),
                ('tel', models.CharField(default='-', max_length=50, verbose_name='Telefon')),
                ('password', models.CharField(max_length=50, verbose_name='Şifre')),
                ('address', models.TextField(default='-', max_length=1500, verbose_name='Adres')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Kullanıcı')),
            ],
        ),
    ]
