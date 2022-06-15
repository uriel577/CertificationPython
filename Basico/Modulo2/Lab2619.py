#Autor: Pablo Uriel Rosas Vargas
#Fecha: 14 de Junio de 2022
#Descripcion: Operaciones aritmeticas

a = input("Ingresa el primer valor: ")
a = float(a)# ingresa un valor flotante para la variable a aquí
b = input("Ingresa el segundo valor: ") 
b = float(b)# ingresa un valor flotante para la variable b aquí

suma = a + b
resta = a - b
multi = a * b
div = a / b

print("La suma es: " + str(suma))# muestra el resultado de la suma aquí 
print("La resta es: " + str(resta))# muestra el resultado de la resta aquí
print("La multi: " + str(multi))# muestra el resultado de la multiplicación aquí
print("La div: " + str(div))# muestra el resultado de la división aquí

print("\n¡Eso es todo, amigos!")

'''Se usa dos variables y con estas se covierten a flotantes deben ser ingresadas desde consola 
despues realizar las operaciones basicas sumar, restar, multiplicar y dividir por ultimo mostrar 
el resulado de las operaciones'''