CantidadDeZapatillas= int(input("ingrese la cantidad de zapatillas en Unidades, compradas: "))
ValorUnitario= int(input("ingrese el total a pagar por las zapatillas: "))
#declaro las variables y le pido por teclado al usuario
subTotal = (CantidadDeZapatillas) * (ValorUnitario)
print(f"El precio a pagar sin el descuento es del:  {subTotal}")
#declaro las variables y le pido por teclado al usuario

if CantidadDeZapatillas>=3:
    totalaPagar= subTotal-(subTotal*0.20)  
    formatearNumero = str(totalaPagar).split('.')[0]
    print(f"El total a pagar con el descuento del 20% es: {formatearNumero} " )
    #si es mayor a 3 imprime con el descuento del 20%
elif CantidadDeZapatillas<3:
   totalaPagar2 = subTotal-(subTotal*0.10)
   formatearNumero = str(totalaPagar2).split('.')[0]
   print(f"ELTotal a pagar con el descuento del 10% es: {formatearNumero} ")
      #si es menor a 3 imprime con el descuento del 10%
