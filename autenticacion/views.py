from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm#crea formulario
from django.contrib.auth import login, authenticate , logout
from django.contrib import messages

class VRegistro(View):

    def get(self, request):
        form = UserCreationForm()
        return render(request, "registro/registro.html", {"form": form})

    def post(self, request):
        form = UserCreationForm(request.POST) #peticion con datos que enviamos con POST

        if form.is_valid():
            # Aquí puedes realizar acciones adicionales con los datos del formulario si es necesario
            usuario = form.save()  # Esto guardará el usuario en la base de datos
            login(request, usuario)
            # Luego puedes redirigir o hacer lo que necesites después de un registro exitoso
            return redirect("home")
        else:
            for msg in form.error_messages:  #por cada mensaje de error en form
                messages.error(request, form.error_messages[msg]) #manda mensaje de error

            return render(request, "registro/registro.html", {"form": form})

def cerrar_session(request):
    logout(request)
    return redirect('home')


def logear(request):
    if request.method=="POST": #si se envio el formulario (pulsando boton) 
        form=AuthenticationForm(request, data=request.POST) # instancia del formulario
        if form.is_valid(): #si form es valido 
            #obtienen los datos limpios del formulario
            nombre_usuario=form.cleaned_data.get("username") 
            contra=form.cleaned_data.get("password")
            #autenticar al usuario utilizando los datos proporcionados.
            usuario=authenticate(username=nombre_usuario, password=contra) 
            if usuario is not None: #Si la autenticación es exitosa
                login(request, usuario) # inicia la sesión del usuario
                return redirect("home")
            else:
                messages.error(request, "Usuario no valido") #no existe usuario
        else:
            messages.error(request, "Informacion incorrecta") 
    else:
        messages.error(request, "Informacion incorrecta")

    form=AuthenticationForm() 
    return render(request, "login/login.html", {"form": form})
    