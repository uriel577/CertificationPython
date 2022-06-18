# Nombre: Pablo Uriel Rosas Vargas
# Fecha: 15 de Junio de 2022
# Descripcion: Uso de una lista basica

hat_list = [1, 2, 3, 4, 5]  # Esta es una lista existente de números ocultos en el sombrero.

new = int(input("Ingresa el nuevo numero: "))
hat_list[2] = new 
print(hat_list)

del(hat_list[-1])
print("Lista con el ultimo elemento eliminado: ", hat_list)

print("La longitud de la lista es: "+  str(len(hat_list)))

'''Se tiene una lista con la cual trabajeremos a esta lista debemos cambiar el valor del numero de 
en medio, despues se elimina el ultimo elemento de la lista y se imprime y por ultimo se muestra la longitud 
de la lista con el elemento eliminado'''