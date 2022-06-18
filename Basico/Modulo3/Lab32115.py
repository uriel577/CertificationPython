# Nombre: Pablo Uriel Rosas Vargas
# Fecha: 15 de Junio de 2022
# Descripcion: Uso de while para evaluar un numero

c0 = int(input("Ingresa c0: "))

if c0 > 1:
	steps = 0
	while c0 != 1:
		if c0 %2 != 0:
			cnew = 3 * c0 + 1
		else:
			cnew = c0 // 2
		print(c0)
		c0 = cnew
		steps += 1
	print("pasos =",steps)
else:
	print("Valor de c0 incorrecto")

'''Se ingresa un numero y depues de eso vemos como dependiendi si es par o impar 
dividirlo o hacer una operacion aritmetica imprimir el valor del numero y crear un contador
para saber la cantidad de veces que modifico el numero hasta que su valor fuera 1'''