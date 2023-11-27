from .carro import Carro

def importe_total_carro(request):
    carro = Carro(request)
    total=0
    if request.user.is_authenticated: #saber si esta autenticado el usuario
        for key, value in request.session["carro"].items(): #recorrer el carro
            total=total+float(value["precio"])  #sumar el precio de cada producto
    else:
        for key, value in request.session["carro"].items(): #recorrer el carro
            total=total+float(value["precio"])  #sumar el precio de cada producto
    return {"importe_total_carro":total} #retornar el total del carro