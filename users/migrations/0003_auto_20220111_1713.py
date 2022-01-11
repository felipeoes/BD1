# Generated by Django 3.2.9 on 2022-01-11 20:13

from django.db import migrations, models
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_usuario_profile_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='id',
        ),
        migrations.AlterField(
            model_name='usuario',
            name='funcional',
            field=models.CharField(max_length=7, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='profile_image',
            field=models.ImageField(default='posts/user_default.png', upload_to=users.models.upload_to, verbose_name='Image'),
        ),
    ]
