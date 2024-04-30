nombEstudiante = input("Ingrese el nombre del estudiante: ")
#Con el comando input le estamos pidiendo al estudiante que digite su nombre en teclado
califiActividades = float(input("Ingrese la calificación promedio de las actividades en clase en decimales (0-5): "))
califiProyecto = float(input("Ingrese la calificación del proyecto final en decimales (0-5): "))
califiEvaluaciones = float(input("Ingrese la calificación promedio de las evaluaciones parciales en decimales (0-5): "))
#De la linea 3 hasta la 5, se le pide al usuario que digite su calificacion en teclado
notaFinal = (califiActividades * 0.3) + (califiProyecto * 0.5) + (califiEvaluaciones * 0.2)
print(f"La nota final de {nombEstudiante} en algoritmia es: {notaFinal}")
#Con el comando "print" se imprime las calificaciones de actividades, proyecto, evaluaciones y con "," concateno las variables