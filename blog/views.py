from django.shortcuts import render
from blog.models import Post

# Create your views here.
def blog(request):
    # Obtener todos los Post que construimos en models.py
    posts = Post.objects.all()
    return render (request, "blog/blog.html", {"posts": posts})
  