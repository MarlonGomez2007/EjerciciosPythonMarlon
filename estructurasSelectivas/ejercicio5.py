genero=input("digite el genero( masculino o femenino): ")
edad=int(input("digite la edad que tiene: "))

if genero == " femenino":
    pulsaciones= (220 - edad)/10
    
if genero =="masculino":
    pulsaciones=  (210 - edad)/10
print(f"El promedio de las pulsaciones es de: {pulsaciones}")