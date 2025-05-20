from django.urls import path
from .import views




urlpatterns = [
    
    path('', views.blog, name='blog'),
    path('categori/<int:categori_id>/', views.categori, name='categori'), # ruta para la vista de categoria
]
