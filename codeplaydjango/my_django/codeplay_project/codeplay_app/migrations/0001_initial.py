# Generated by Django 5.0.4 on 2024-11-14 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pendaftaran',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=100)),
                ('kelas', models.CharField(choices=[('kelas1', 'Usia anak 6-11 th'), ('kelas2', 'Usia anak 11-18 th')], max_length=50)),
            ],
        ),
    ]
