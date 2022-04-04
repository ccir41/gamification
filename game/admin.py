from django.contrib import admin

from .models import (
    Product,
    UserResponse
)

admin.site.register(Product)
admin.site.register(UserResponse)
