from django.urls import path
from .import views




urlpatterns = [
    path('<int:page_id>/', views.page, name='page'), # ruta para la página
]
