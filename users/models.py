from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    public_address = models.CharField(
        _("Public address"), max_length=100, null=True, blank=True)
