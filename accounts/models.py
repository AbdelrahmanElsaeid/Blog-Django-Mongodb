from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext as _
# Create your models here.



##################____________ Using ORM ______________################


class User(AbstractUser):
    username = models.CharField(max_length = 50, blank = True, null = True, unique = True,verbose_name=_('Username'))
    email = models.EmailField(unique = True, verbose_name=_('Email'))
    otp = models.CharField(max_length=100, null=True, blank=True, verbose_name=_('OTP'))

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']


    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')

    def __str__(self):
        return self.username  
    




 