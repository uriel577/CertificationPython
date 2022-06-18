# Nombre: Pablo Uriel Rosas Vargas
# Fecha: 15 de Junio de 2022
# Descripcion: Manejo de listas sin repeticiones

my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
new_list = []
for number in my_list:  
	if number not in new_list:  
		new_list.append(number)  
my_list = new_list[:]  

print("La lista con elementos únicos:")
print(my_list)

'''Se crea una lista donde no deben existir valores repetidos s psrtir de una 
lista ya creada verificara si el elemento ya esta y si no esta se agrega a una
nueva lista que tendra los elementos sin repetir'''