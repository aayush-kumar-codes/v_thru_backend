from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from .managers import CustomUserManager


class CustomUser(AbstractUser):
    username = models.CharField(blank=True, null=True,max_length=100)
    email = models.EmailField(_('email address'), unique=True, blank=True, null=True)
    name = models.CharField(blank=True, null=True, max_length=100)


    # bio = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to=None, null=True, blank=True,
                              default='media/None/default.png')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    # spouse_name = models.CharField(blank=True, null=True, max_length=100)
    # date_of_birth = models.DateField(blank=True, null=True)
    # language = models.CharField(blank=True, null=True, max_length=100)
    phone_number = models.CharField(blank=True, null=True, max_length=100)
    # ip_addr = models.CharField(blank=True, null=True, max_length=40)
    verified = models.BooleanField(default=False)
    receive_updates_on_notifications = models.BooleanField(default=False)
    receive_updates_on_email = models.BooleanField(default=False)
    receive_updates_on_sms = models.BooleanField(default=False)
    receive_offers_on_notifications = models.BooleanField(default=False)
    receive_offers_on_email = models.BooleanField(default=False)
    receive_offers_on_sms = models.BooleanField(default=False)
    password = models.CharField(_('password'), max_length=128, null=True, blank=True)

    def __str__(self):
        if self.email:
            return self.email
        elif self.ip_addr:
            return self.ip_addr
        else:
            return ''