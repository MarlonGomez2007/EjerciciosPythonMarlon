vendedor = input("ingrese el nombre del vendedor:" )
sueldo = float(input("ingrese el sueldo"))
venta1 = float(input("ingrese la venta 1: "))
venta2 = float(input("ingrese la venta 2: "))
venta3 = float(input("ingrese la venta 3: "))
#declaro las variables para ingresar y le pido al usuario por el comando input que me proporcione la informacion de las ventas
comision = (venta1+venta2+venta3) * .10 #
#sumo las ventas  y multiplico .10
print("El nombre del vendedor es: " , vendedor)
print("El sueldo del vendedor es: ",sueldo)
print("La comision del mes por las 3 ventas es: ", comision)
print("El sueldo total con la comision es: ", sueldo+comision )
#imprimo con el comando print