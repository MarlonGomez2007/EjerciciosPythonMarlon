base=int(input("Ingrese el valor de la altura del rectangulo en cm: "))
altura=int(input("Ingrese el valor de la base del rectangulo en cm: "))
#primero declaro las 2 variables y le pido al usuario que me proporcione  la informacion
perimetro=(base*2) + (altura*2)
#segundo para hallar el perimetro  con los datos ya proporcionados  multiplico la base x 2 y sumo la altura ya previamente multiplicada x 2
area= base * altura
#tercero para hallar el area multiplico la base x la altura
print("El perímetro del rectángulo es: ",perimetro,"cm" " el area del rectangulo es: ",area,"cm")
#cuarto imprimo con el comando print el enunciado  y concateno las variables