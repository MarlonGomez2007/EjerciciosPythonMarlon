#De la linea 2 hasta la 4 le decimos al usuario que ingrese los datos
edad = float(input("Ingrese la edad en años: "))
sexo = input("Ingrese el sexo (mujer u hombre): ").lower()
nivel_hemoglobina = float(input("Ingrese el nivel de hemoglobina en g%: "))

tiene_anemia = False #De la linea 6 hasta la 31 decidimos que si el nivel de hemoglobina es mayor o menor que lo asignado, decida si tiene anemia o no con el atributo TRUE

if edad <= 1/12:
    if nivel_hemoglobina < 13 or nivel_hemoglobina > 26:
        tiene_anemia = True
elif 1/12 < edad <= 6/12:
    if nivel_hemoglobina < 10 or nivel_hemoglobina > 18:
        tiene_anemia = True
elif 6/12 < edad <= 12/12:
    if nivel_hemoglobina < 11 or nivel_hemoglobina > 15:
        tiene_anemia = True
elif 1 < edad <= 5:
    if nivel_hemoglobina < 11.5 or nivel_hemoglobina > 15:
        tiene_anemia = True
elif 5 < edad <= 10:
    if nivel_hemoglobina < 12.6 or nivel_hemoglobina > 15.5:
        tiene_anemia = True
elif 10 < edad <= 15:
    if nivel_hemoglobina < 13 or nivel_hemoglobina > 15.5:
        tiene_anemia = True
elif sexo == "mujer" and edad > 15:
    if nivel_hemoglobina < 12 or nivel_hemoglobina > 16:
        tiene_anemia = True
elif sexo == "hombre" and edad > 15:
    if nivel_hemoglobina < 14 or nivel_hemoglobina > 18:
        tiene_anemia = True
#Aca hacemos una desicion de que si tiene anemia imprima que es positivo y si no, lo contrario
if tiene_anemia:
    print("Resultado: Positivo para anemia.")
else:
    print("Resultado: Negativo para anemia.")
