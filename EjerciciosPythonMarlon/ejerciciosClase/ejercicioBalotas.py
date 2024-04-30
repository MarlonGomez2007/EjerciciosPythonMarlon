#Realice un algoritmo que lea el valor de la compra y de acuerdo a
#las siguientes balotas : Verde, amarillo, verde, blanco
#si saco la balota verde el descuento es del 100%
#si saco la balota amarillo el descuento es del 75%
#si saco la balota rojo el descuento es del 50%
#si saco la balota blanco  no hay descuento
#imprimir valor de la compra, color de la balota y valor a pagar

from random import *
valorCompra=int(input("Ingrese el Valor de la Compra: "))
balotas=choice(["Verde","Amarilla","Roja","Blanca"])
if balotas =="Verde":
    print(f"Te toco el descuento del 100%")
    valorPagar=0
    print(f"El valor de la compra fue: {valorCompra} El color de la balota fue: {balotas} El valor a Pagar es: {valorPagar}")
elif balotas =="Amarilla":
    print(f"Te toco el descuento del 75%")
    descuento=valorCompra*0.75
    valorPagar=valorCompra-descuento
    print(f"El valor de la compra fue: {valorCompra} El color de la balota fue: {balotas} El valor a Pagar es: {valorPagar}")
elif balotas=="Roja":
    print(f"Te toco el descuento del 50%")
    descuento=valorCompra*0.5
    valorPagar=valorCompra-descuento
    print(f"El valor de la compra fue: {valorCompra} El color de la balota fue: {balotas} El valor a Pagar es: {valorPagar}")
elif balotas=="Blanca":
    print(f"No tiene descuento")
    valorPagar=valorCompra
    print(f"El valor de la compra fue: {valorCompra} El color de la balota fue: {balotas} El valor a Pagar es: {valorPagar}")

    