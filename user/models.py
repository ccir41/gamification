from django.db import models
from django.contrib.auth.models import AbstractUser


class UserCategoryChoice(models.TextChoices):
    STUDENT = 'STUDENT', 'Student'
    JOB_HOLDER = 'JOB_HOLDER', 'Job Holders'
    HOUSE_WIFE = 'HOUSE_WIFE', 'House Wife'



class User(AbstractUser):
    email = models.EmailField(unique=True)
    what_best_describe_you = models.CharField(
        max_length=10,
        choices=UserCategoryChoice.choices,
        default=UserCategoryChoice.STUDENT
    )

    def __str__(self):
        return self.email
    
    def save(self, *args, **kwargs):
        self.username = self.email
        super().save(*args, **kwargs)