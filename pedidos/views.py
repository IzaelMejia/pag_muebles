from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from carro.carro import Carro
from django.shortcuts import redirect  #para redicreccionar 
from pedidos.models import LineaPedido, Pedido
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

# Create your views here.

@login_required(login_url='/autentication/logear') #requiere estar logeado 
def procesar_pedido(request):
    pedido=Pedido.objects.create(user=request.user)    #dar de alta pedido
    carro= Carro(request)
    lineas_pedido=list()
    for key, value in carro.carro.items(): #por cada calve calor que hay en items de carro
        lineas_pedido.append(LineaPedido(
            producto_id=key,
            cantidad=value['cantidad'],
            user=request.user,
            pedido=pedido
        ))
        LineaPedido.objects.bulk_create(lineas_pedido) #dar de alta lineas pedido a bd
        enviar_mail(
            pedido=pedido, 
            lineas_pedido=lineas_pedido, 
            nombreusuario=request.user.username,
            emailusuario=request.user.email
            )
        messages.success(request, 'El pedido se ha realizado correctamente')
        return redirect("../tienda")


def enviar_mail(**kwargs):
    asunto = 'Gracias por comprar'
    mensaje = render_to_string("emails/pedido.html", {
        'pedido': kwargs.get('pedido'),
        'lineas_pedido': kwargs.get('lineas_pedido'),
        'nombreusuario': kwargs.get('nombreusuario'),
    })
    mensaje_texto = strip_tags(mensaje)
    from_email = "l20200195@pachuca.tecnm.mx"
    # to = kwargs.get('emailusuario')
    to = "izaelmejiaa@gmail.com"
    send_mail(asunto, mensaje_texto, from_email, [to], html_message=mensaje)

