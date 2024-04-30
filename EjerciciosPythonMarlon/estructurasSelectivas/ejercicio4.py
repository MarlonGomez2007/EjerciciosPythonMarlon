from random import *
valorCompra=int(input("Ingrese el Valor de la Compra: "))
balotas=choice(["Verde","Roja","Color diferente"])

if balotas =="Rojo":
    print(f"Te toco el descuento del 15%")
    descuento=valorCompra*0.15
    valorPagar=valorCompra-descuento
    print(f"El valor de la compra fue: {valorCompra} El color de la balota fue: {balotas} El valor a Pagar es: {valorPagar}")

elif balotas=="Verde":
    print(f"Te toco el descuento del 20%")
    descuento=valorCompra*0.2
    valorPagar=valorCompra-descuento
    print(f"El valor de la compra fue: {valorCompra} El color de la balota fue: {balotas} El valor a Pagar es: {valorPagar}")
elif balotas=="Color diferente":
    print(f"No tiene descuento")
    valorPagar=valorCompra
    print(f"El valor de la compra fue: {valorCompra} El color de la balota fue: {balotas} El valor a Pagar es: {valorPagar}")
