from django.shortcuts import render, redirect

from .forms import FormularioContacto

from django.core.mail import EmailMessage 

# Create your views here.
def contacto(request):
    formulario_contacto = FormularioContacto()

# Si el meotod se POST
    if request.method == "POST":
        # Cargar la info que el usuario agrego en el formulario
        formulario_contacto = FormularioContacto(data=request.POST)
        if formulario_contacto.is_valid(): #si se rellenaron los campos bien
            # Guardar en variables los datos ingresados lo que tenemos en cada input
            nombre = request.POST.get("nombre") 
            email = request.POST.get("email")
            contenido = request.POST.get("contenido")

            # Crea un objeto EmailMessage para enviar el correo
            email= EmailMessage("Mensaje desde App Django", 
                                "Usuario con nombre {} con al dirrección {} escribe lo siguiente: \n\n {}"
                                    .format(nombre, email, contenido),
                                    "",["l20200195@pachuca.tecnm.mx"], reply_to=[email])
            
            try:
                # Intenta enviar el correo
                email.send()
                # Redirige a la página de contacto con un parámetro "?valido" en la URL
                return redirect("/contacto/?valido")
            except:
                return redirect("/contacto/?error")

    return render (request, "contacto/contacto.html", {"miFormulario":formulario_contacto})