from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.db import models

from apps.utils.hash import hash_generator


class User(AbstractUser):
    slug = models.SlugField(max_length=100, blank=True, unique=True, null=True)
    is_active = models.BooleanField(_("Active"), default=False)

    class Meta(AbstractUser.Meta):
        swappable = "AUTH_USER_MODEL"
        db_table = "auth_user"
        ordering = ["pk"]

    def __str__(self):
        return f"User: {self.username}"

    def save(self, *args, **kwargs):
        self.slug = self.slug or hash_generator()
        super(User, self).save(*args, **kwargs)
