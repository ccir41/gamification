from django.db import models

# 3rd party models
from ckeditor.fields import RichTextField

# user defined models
from core.models import TimeStampModel
from user.models import User


class ProductCategoryChoice(models.TextChoices):
    ELECTRONICS = 'ELECTRONICS', 'Electronics'
    FURNITURE = 'FURNITURE', 'Furniture'


class Product(TimeStampModel):
    product_category = models.CharField(
        max_length=64,
        choices=ProductCategoryChoice.choices,
        default=ProductCategoryChoice.ELECTRONICS
    )
    name = models.CharField(max_length=255)
    description = RichTextField()
    image = models.ImageField(upload_to='Product/')
    price = models.DecimalField(
        max_digits=9,
        decimal_places=2
    )
    min_price = models.DecimalField(
        max_digits=9,
        decimal_places=2
    )
    max_price = models.DecimalField(
        max_digits=9,
        decimal_places=2
    )

    def __str__(self):
        return self.name


class UserResponse(TimeStampModel):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='user_response'
    )
    response = models.JSONField(
        blank=True,
        default=dict
    )

    def __str__(self):
        return self.user.email
