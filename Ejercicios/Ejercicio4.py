#4.	Un profesor registra calificaciones de sus estudiantes, indicando que los estudiantes que saquen 89 puntos automáticamente tienen 90, los que saquen 79 puntos tienen 80, los que saquen 69 puntos tienen 70, 68 o menos son reprobados. Debe indicar en el registro de cada estudiante la nueva calificación, e indicar el promedio de calificaciones de todos los estudiantes registrados, y el literal que corresponde al mismo, 100-90, A, 89-80, B, 79-70, C, menos de 70 F.

calificaciones = [89, 95, 73, 81, 68, 90, 87, 79, 92, 76]

num_estudiantes = len(calificaciones)

suma_calificaciones = 0

for i in range(num_estudiantes):
    calificacion = calificaciones[i]
    
    # Ajuste de calificación según reglas del profesor
    if calificacion >= 89:
        calificacion = 90
    elif calificacion >= 79:
        calificacion = 80
    elif calificacion >= 69:
        calificacion = 70
    else:
        calificacion = "R"
    
    if isinstance(calificacion, int):  # Verificar si la calificación es entero
        suma_calificaciones += calificacion
    
    calificaciones[i] = calificacion

promedio_calificaciones = suma_calificaciones / num_estudiantes

# Asignamos el literal según el promedio de calificaciones
if promedio_calificaciones >= 90:
    literal = "A"
elif promedio_calificaciones >= 80:
    literal = "B"
elif promedio_calificaciones >= 70:
    literal = "C"
else:
    literal = "F"

# Imprimimos el registro de calificaciones
print("Registro de calificaciones:")
for i in range(num_estudiantes):
    print(f"Estudiante {i + 1}: {calificaciones[i]}")

# Imprimimos el promedio de calificaciones y el literal correspondiente
print(f"\nEl promedio de calificaciones es {promedio_calificaciones:.2f}.")
print(f"El literal correspondiente es {literal}.")