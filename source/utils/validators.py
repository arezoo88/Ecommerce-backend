import datetime
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
import os


def validate_image_size(value):
    # 5MB
    MAX_FILE_SIZE = 5000000
    if value.size > MAX_FILE_SIZE:
        raise ValidationError("Image size must be less than 5MB!")


def validate_image_extension(value):
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.png', '.jpg', '.jpeg']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension.')
