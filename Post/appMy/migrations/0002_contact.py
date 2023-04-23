# Generated by Django 4.1.7 on 2023-03-24 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appMy', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='İsim')),
                ('email', models.EmailField(max_length=254, verbose_name='e-mail')),
                ('title', models.CharField(max_length=50, verbose_name='Başlık')),
                ('text', models.TextField(max_length=1500, verbose_name='Mesaj')),
            ],
        ),
    ]