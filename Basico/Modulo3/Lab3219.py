# Nombre: Pablo Uriel Rosas Vargas
# Fecha: 15 de Junio de 2022
# Descripcion: Usar el while con el break 

word = input("Ingresa una palabra o ingresa la palabra secreta: ")

while word != "chupacabra":
    word = input("Ingresa una palabra o ingresa la palabra secreta: ")
    if word == "chupacabra":
        break

print("¡Has dejado el bucle con éxito")

'''Se pide al usuario que ingresa palabra hasta que ingrese la palabra clave(chupacabra) 
una vez que ha ingresado la palabra clave el proceso(while) debe detenerse con un break 
y enviar un mensaje a pantalla diciendo que el bucle termino'''