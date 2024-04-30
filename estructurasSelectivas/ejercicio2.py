CantidadDeZapatillas= int(input("ingrese la cantidad de zapatillas en Unidades, compradas: "))
ValorUnitario= int(input("ingrese el total a pagar por las zapatillas: "))

subTotal = (CantidadDeZapatillas) * (ValorUnitario)
print(f"El precio a pagar sin el descuento es del:  {subTotal}")


if CantidadDeZapatillas>=3:
    totalaPagar= subTotal-(subTotal*0.20)  
    formatearNumero = str(totalaPagar).split('.')[0]
    print(f"El total a pagar con el descuento del 20% es: {formatearNumero} " )
elif CantidadDeZapatillas<3:
   totalaPagar2 = subTotal-(subTotal*0.10)
   formatearNumero = str(totalaPagar2).split('.')[0]
   print(f"ELTotal a pagar con el descuento del 10% es: {formatearNumero} ")