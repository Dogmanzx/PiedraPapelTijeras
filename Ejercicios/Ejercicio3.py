#3.	Azua Air necesita transportar la cantidad de personas que usted indique por el tecladao a San Juan usando sus aviones DC9. Los mismos tienen capacidad para 110 personas, indique cuantos vuelos debe realizar Azua Air para transportar la cantidad de pasajeros que usted ingresó por el teclado.

#Asignamos la capacidad del avión a la variable capacidad_avion.

#Solicitamos al usuario que ingrese la cantidad de pasajeros que desean transportar mediante la función input(), la cual devuelve una cadena de caracteres que convertimos en un número entero usando int().

#Dividimos la cantidad de pasajeros entre la capacidad del avión usando el operador de división entera // para obtener la cantidad de vuelos completos necesarios. Esto lo asignamos a la variable cantidad_vuelos.

#Si queda un resto al dividir la cantidad de pasajeros entre la capacidad del avión, esto significa que se necesita un vuelo adicional para transportar a los pasajeros restantes. Por lo tanto, agregamos 1 a cantidad_vuelos usando el operador de suma +=.

#Usando la función print(), mostramos en pantalla la cantidad de vuelos necesarios para transportar la cantidad de pasajeros ingresada por el usuario.

capacidad_avion = 110

cantidad_pasajeros = int(input("Ingrese la cantidad de pasajeros que desea transportar: "))

cantidad_vuelos = cantidad_pasajeros // capacidad_avion
if cantidad_pasajeros % capacidad_avion != 0:
    cantidad_vuelos += 1

print(f"Azua Air debe realizar {cantidad_vuelos} vuelos para transportar a {cantidad_pasajeros} pasajeros.")