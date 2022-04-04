import random

from django.shortcuts import render
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View

from user.models import UserCategoryChoice
from game.models import Product, ProductCategoryChoice



class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html', {})


class GameView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        if request.user.what_best_describe_you == UserCategoryChoice.STUDENT:
            queryset1 = Product.objects.filter(product_category=ProductCategoryChoice.FURNITURE)
            queryset2 = Product.objects.filter(product_category=ProductCategoryChoice.ELECTRONICS)
            queryset = queryset1 | queryset2
        elif request.user.what_best_describe_you == UserCategoryChoice.JOB_HOLDER:
            queryset1 = Product.objects.filter(product_category=ProductCategoryChoice.FURNITURE)
            queryset2 = Product.objects.filter(product_category=ProductCategoryChoice.ELECTRONICS)
            queryset = queryset1 | queryset2
        elif request.user.what_best_describe_you == UserCategoryChoice.HOUSE_WIFE:
            queryset1 = Product.objects.filter(product_category=ProductCategoryChoice.FURNITURE)
            queryset2 = Product.objects.filter(product_category=ProductCategoryChoice.ELECTRONICS)
            queryset = queryset1 | queryset2
        queryset = sorted(queryset, key=lambda L: random.random())[:10]
        return render(request, 'game.html', {'queryset': queryset})
    
    def post(self, request, *args, **kwargs):
        pass