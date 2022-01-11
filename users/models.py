from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils.translation import gettext_lazy as _


def upload_to(instance, filename):
    return 'posts/{filename}'.format(filename=filename)


class UsuarioGerente(BaseUserManager):
    def create_user(self, email, username, first_name, last_name, funcional, profile_image, password=None):
        user = self.model(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name,
            funcional=funcional,
            profile_image=profile_image
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password, first_name, last_name, funcional, profile_image):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
            funcional=funcional,
            profile_image=profile_image
        )

        user.is_staff = True
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Usuario(AbstractBaseUser):
    email = models.EmailField(verbose_name='email', max_length=60, unique=True)
    funcional = models.CharField(max_length=7, primary_key=True)
    profile_image = models.ImageField(
        _("Image"), upload_to=upload_to, default='posts/user_default.png')
    first_name = models.CharField(verbose_name='first_name', max_length=30)
    last_name = models.CharField(verbose_name='last_name', max_length=30)
    username = models.CharField(max_length=30, unique=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    

    USERNAME_FIELD = 'funcional'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name', 'email']

    objects = UsuarioGerente()

    def __str__(self):
        return self.first_name + ' - ' + self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True


# class Usuario(AbstractUser):

#     def __str__(self):
#         return self.email
