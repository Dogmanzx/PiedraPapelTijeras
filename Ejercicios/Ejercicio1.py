#1. El hijo mayor de Doña María le envía US$ 200.00 cada mes, despliegue cuanto dinero hace en pesos dominicanos, asumiendo la tasa por dólar del día, ingresada por usted por el teclado.

#Explicación de como hacerlo: 

#Solicitamos al usuario ingresar la tasa por dólar del día mediante la función input(), la cual devuelve una cadena de caracteres que convertimos en un número flotante usando float().

#Asignamos el valor de 200.00 a la variable dinero_en_dolares.

#Multiplicamos dinero_en_dolares por tasa_dolar para obtener dinero_en_pesos.

#Usando la función print(), mostramos en pantalla el resultado, con un máximo de dos decimales, utilizando el modificador de formato :.2f.

tasa_dolar = float(input("Ingrese la tasa por dólar del día: "))
dinero_en_dolares = 200.00
dinero_en_pesos = dinero_en_dolares * tasa_dolar

print(f"El dinero en pesos dominicanos que hace cada mes es: {dinero_en_pesos:.2f}")