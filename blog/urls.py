from django.urls import path

# Trabajar vistas en el proyecto 
from . import views

urlpatterns = [
    path('', views.blog, name="blog"),
    # Especificar parametro de tabla "blog_post_categorias" que esta en la bd y despues viws
    path('categoria/<int:categoria_id>/', views.categoria, name="categoria"),
]
