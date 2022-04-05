from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractUser

from core.models import TimeStampModel


class UserCategoryChoice(models.TextChoices):
    STUDENT = 'STUDENT', 'Student'
    JOB_HOLDER = 'JOB_HOLDER', 'Job Holders'
    HOUSE_WIFE = 'HOUSE_WIFE', 'House Wife'

class User(AbstractUser, TimeStampModel):
    email = models.EmailField(unique=True)
    what_best_describe_you = models.CharField(
        max_length=10,
        choices=UserCategoryChoice.choices,
        default=UserCategoryChoice.STUDENT
    )

    def __str__(self):
        return self.email
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.username = self.email
        super().save(*args, **kwargs)


class UserProfile(TimeStampModel):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='user_profile'
    )
    points = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.user.email


def create_user_profile(sender, instance, created, *args, **kwargs):
    if created:
        UserProfile.objects.create(
            user=instance
        )

post_save.connect(
    create_user_profile,
    sender=User
)