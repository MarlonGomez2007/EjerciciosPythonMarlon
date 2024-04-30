monto_Total = float(input("ingrese el monto total de la compra:")) # Asignamos el monto total para empezar y como vamos a trabajar con decimales ponemos float
if monto_Total > 500000:
    propio = monto_Total * 0.55
    prestamo_Banco = monto_Total * 0.30
    credito_Fabricante = monto_Total        # Ingresamos las variables y asignamos el porcentaje que nos indican en el ejercicio
else:
    propio = monto_Total * 0.70
    credito_Fabricante = monto_Total - propio
    prestamo_Banco = 0                        # Si el monto no excede los 500.000 entonces entonces ingresamos el monto total por el porcentaje de la empresa

print("La empresa invirtió: ",propio, "Le solicitó prestado al banco:",prestamo_Banco,"y el valor del credito solicitado al fabricante fué de:",credito_Fabricante)
