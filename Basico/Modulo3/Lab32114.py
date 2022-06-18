# Nombre: Pablo Uriel Rosas Vargas
# Fecha: 15 de Junio de 2022
# Descripcion: Uso de while para la creacion de una piramide

blocks = int(input("Ingresa el número de bloques: "))

level = 1
height = 0
while blocks > 0:
    level += 1
    blocks = blocks - level
    height += 1
    
print("La altura de la pirámide:", height)

'''Se necesita crear un piramide a partir del numero que ingrese el usuario despues 
se deben ver cuantos niveles tiene la piramide para eso hay que hacer una variable 
descuente la cantidad de bloques a la cantidad original tomando en cuenta que cada 
nivel de la piramide es un bloque mas grande que el anterior y se empieza en 1 '''