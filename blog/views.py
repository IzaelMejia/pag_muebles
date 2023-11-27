from django.shortcuts import render
from blog.models import Post, Categoria 

# Create your views here.
def blog(request):
    # Obtener todos los Post que construimos en models.py
    posts = Post.objects.all()
    return render (request, "blog/blog.html", {"posts": posts})
  
#   Con filtro 
def categoria(request, categoria_id):
    # Mostrar el id de cada categoria  " id = categoria_id  ""
    categoria = Categoria.objects.get(id=categoria_id)  #cuando hace clik en enlace obtiene categoria
    #  Filtrar los post por la categoria 
    posts = Post.objects.filter(categorias = categoria)  #otiene posts de esa categoria filtrada
    return render (request, "blog/categorias.html", {"categoria": categoria, "posts":posts}) #muestra categoria filtrada y sus posts
  