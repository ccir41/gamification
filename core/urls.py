from django.urls import path

from . import views

app_name = 'core'


urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('analytics/', views.analytics, name='analytics'),
    path('product-chart/', views.product_chart, name='product-chart'),
    path('game/<int:quiz_id>/', views.take_quiz, name='game'),
    path('result/<int:quiz_id>/', views.result_page, name='result'),
]