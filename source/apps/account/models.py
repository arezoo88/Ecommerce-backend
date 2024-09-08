from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser
from apps.account.managers import CustomUserManager
from utils.validators import validate_image_extension, validate_image_size
from shortuuid.django_fields import ShortUUIDField


class User(AbstractUser):
    username = None
    email = models.EmailField(
        _("email address"),
        unique=True
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email


GENDER_CHOICES = (
    ("Male", "male"),
    ("Female", "female"),
    ("Unknown", "unknown")
)


class Profile(models.Model):
    user = models.OneToOneField(
        to=User,
        verbose_name=_('User'),
        on_delete=models.CASCADE,
        unique=True
    )

    image = models.ImageField(
        verbose_name=_('Image'),
        upload_to='images/',
        validators=[validate_image_extension, validate_image_size],
        default='default/default-user.jpg'
    )

    full_name = models.CharField(
        verbose_name=_('Full Name'),
        max_length=100,
        null=True,
        blank=True
    )
    address = models.CharField(
        verbose_name=_('Address'),
        max_length=200,
        null=True,
        blank=True
    )
    country = models.CharField(
        verbose_name=_('Country'),
        max_length=50,
        null=True,
        blank=True
    )
    city = models.CharField(
        verbose_name=_('City'),
        max_length=50,
        null=True,
        blank=True
    )
    state = models.CharField(
        verbose_name=_('State'),
        max_length=100,
        null=True,
        blank=True
    )
    about = models.TextField(
        verbose_name=_('About'),
        blank=True,
        null=True
    )
    gender = models.CharField(
        verbose_name=_('Gender'),
        max_length=20,
        choices=GENDER_CHOICES
    )
    pid = ShortUUIDField(
        verbose_name=_('Pid'),
        unique=True,
        length=10,
        max_length=20,
        alphabet="abcdefghijk"
    )

    def __str__(self):
        if self.full_name:
            return str(self.full_name)
        else:
            return str(self.user.email)

    class Meta:
        verbose_name = _("Profile")
        verbose_name_plural = _("Profiles")
