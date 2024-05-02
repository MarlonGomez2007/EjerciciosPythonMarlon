nombEstudiante= input("Ingrese el Nombre del Estudiante: ")
#declaro la variable y le pido al usuario que me proporcione la informacion mediante el input

califi_1 = int(input("Ingrese la Primera Nota (0-100): "))
#declaro la variable y le pido al usuario que me proporcione la informacion mediante el input

califi_2 = int(input("Ingrese la Segunda Nota (0-100): "))
#declaro la variable y le pido al usuario que me proporcione la informacion mediante el input

califi_3 = int(input("Ingrese la Tercera Nota(0-100): "))
#declaro la variable y le pido al usuario que me proporcione la informacion mediante el input
if  califi_1 >= 101 or califi_2 >= 101 or califi_3 >= 101:
    print(f"En Alguna de las Notas Ingresadas un Numero es Mayor a 100 no se admite como una nota valida")
#si se coloca un numero mayo a 101 no dejara seguir con el proceso

else:
    caliCasi = (califi_1) + (califi_2) + (califi_3)
#sumo la 3 variables
    califiFinal = caliCasi/3
#saco la division para el promedio
    formatearNumero = str(califiFinal).split('.')[0]
#formateo el numero para que se vea mas bonitos
    if califiFinal >= 70:
        print(f"La Nota Final fue de: {formatearNumero} El/La Estudiante {nombEstudiante} Aprobó 🎉")
    #si es mayor o igual a 70 aprueba
    else:
        print(f"La Nota Final fue de: {formatearNumero} El/La Estudiante {nombEstudiante} Reprobó 😓")
#si es menor a 70 desaprueba

