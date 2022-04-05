from django.urls import path

from . import views

app_name = 'core'


urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('game/<int:quiz_id>/', views.take_quiz, name='game')
]