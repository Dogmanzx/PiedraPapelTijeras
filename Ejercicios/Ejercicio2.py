#2.	Don Sebastian vende limones en el mercado, por cada libra de limones a 50 pesos la libra gana 10 pesos, despliegue cuanto gana Don Sebastian si vende la cantidad de libras de limones que usted ingresa por el teclado.

#Asignamos el precio por libra de limones a la variable precio_por_libra y la ganancia por libra a la variable ganancia_por_libra.

#Solicitamos al usuario que ingrese la cantidad de libras de limones vendidas por Don Sebastian mediante la función input(), la cual devuelve una cadena de caracteres que convertimos en un número flotante usando float().

#Calculamos la ganancia total de Don Sebastian multiplicando la cantidad de libras vendidas por la ganancia por libra y lo asignamos a la variable ganancia_total.

#Calculamos el precio total de la venta de limones multiplicando la cantidad de libras vendidas por el precio por libra más la ganancia por libra, y lo asignamos a la variable precio_total.

#Usando la función print(), mostramos en pantalla la ganancia total de Don Sebastian y el precio total de la venta, ambos con un máximo de dos decimales, utilizando el modificador de formato :.2f.

precio_por_libra = 50
ganancia_por_libra = 10

libras_vendidas = float(input("Ingrese la cantidad de libras de limones que vendió Don Sebastian: "))

ganancia_total = ganancia_por_libra * libras_vendidas
precio_total = (precio_por_libra + ganancia_por_libra) * libras_vendidas

print(f"Don Sebastian ganó {ganancia_total:.2f} pesos por la venta de limones.")
print(f"El precio total de la venta fue de {precio_total:.2f} pesos.")