from django.db import models

# 3rd party models
from ckeditor.fields import RichTextField

# user defined models
from core.models import TimeStampModel
from user.models import User


class ProductCategory(TimeStampModel):
    name = models.CharField(
        max_length=128,
        unique=True
    )

    def __str__(self):
        return self.name


class Product(TimeStampModel):
    product_category = models.ForeignKey(
        ProductCategory,
        on_delete=models.CASCADE,
        related_name='products'
    )
    name = models.CharField(max_length=255)
    description = RichTextField()
    image = models.ImageField(upload_to='Product/')
    price = models.DecimalField(
        max_digits=5,
        decimal_places=2
    )
    min_price = models.DecimalField(
        max_digits=5,
        decimal_places=2
    )
    max_price = models.DecimalField(
        max_digits=5,
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
