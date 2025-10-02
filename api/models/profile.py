# profiles/models.py

import uuid
from django.db import models
from django.core.validators import (
    MinLengthValidator,
    RegexValidator,
    EmailValidator,
    URLValidator,
)
from django.utils import timezone


class Profile(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    full_name = models.CharField(
        max_length=255,
        validators=[MinLengthValidator(1)]
    )

    address = models.CharField(
        max_length=255,
        validators=[MinLengthValidator(5)]
    )

    mobile_number = models.CharField(
        max_length=20,
        validators=[
            RegexValidator(
                regex=r'^[0-9+\-\s()]{7,20}$',
                message="Enter a valid phone number."
            )
        ]
    )

    email = models.EmailField(
        validators=[EmailValidator()]
    )

    date_of_birth = models.DateField(
        validators=[],
        help_text="Must be a past date."
    )

    # Social platforms
    linkedin = models.URLField()
    whatsapp = models.CharField(max_length=255)
    instagram = models.CharField(max_length=255)
    snapchat = models.CharField(max_length=255)
    tiktok = models.CharField(max_length=255)

    # Extra info
    interests = models.TextField()
    notes = models.TextField()

    # Foreign key (assuming you have a Group model)
    groupsId = models.UUIDField()

    createdAt = models.DateTimeField(
        default=timezone.now
    )
    updatedAt = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        db_table = "profile"
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"

    def __str__(self):
        return self.full_name
