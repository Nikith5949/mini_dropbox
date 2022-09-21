
from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager


class UserManagerf(BaseUserManager):
    def create_user(self,email,username,password=None):
        if not email:
            raise ValueError('user Must have email address')
        print('1111111111111111111111')
        email=self.normalize_email(email)
        user=self.model(email=email,username=username,)
        user.set_password(password)
        print(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,email,username,password):
        user=self.create_user(email,username,password)
        user.is_admin=True
        user.is_staff=True
        user.is_superuser=True

        user.save(using=self._db)
        return user


class User(AbstractBaseUser):

    email = models.EmailField(verbose_name='email',primary_key=True)
    username=models.CharField(max_length=30,null=False,blank=False)
    is_active = models.BooleanField(default=True)
    is_admin=models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser=models.BooleanField(default=False)
    date_joined=models.DateField(verbose_name='date',auto_now=True)

    objects=UserManagerf()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']


    def __str__(self):
        return f'{self.email} '

    def has_perm(self,perm,obj=None):
        return self.is_admin

    def has_module(self,app_label):
        return True
