from cloudinary import models as cloudinary_models
from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator
from django.db import models
from django.db.models import RESTRICT
from petstagram.pets.models import Pet
from petstagram.photos.validators import validate_file_less_than_5mb

UserModel = get_user_model()


class Photo(models.Model):
    MIN_DESCRIPTION_LENGTH = 10
    MAX_DESCRIPTION_LENGTH = 300

    MAX_LOCATION_LENGTH = 30

    photo = cloudinary_models.CloudinaryField(
        null=False,
        blank=False,
        # validators=(validate_file_less_than_5mb,),
    )

    description = models.CharField(
        max_length=MAX_DESCRIPTION_LENGTH,
        validators=(MinLengthValidator(MIN_DESCRIPTION_LENGTH),),
        null=True,
        blank=True
    )

    location = models.CharField(max_length=MAX_LOCATION_LENGTH, null=True, blank=True)

    publication_date = models.DateField(auto_now=True, null=False, blank=True)

    tagged_pets = models.ManyToManyField(
        Pet,
        blank=True,
    )

    user = models.ForeignKey(UserModel, on_delete=RESTRICT)

    def __str__(self):
        return f'PK: {self.pk} PHOTO:{self.photo} LOCATION:{self.location}'
