# Nombre: Pablo Uriel Rosas Vargas
# Fecha: 15 de Junio de 2022
# Descripcion: Uso de if-elif-else con for y continue

user_word = input("Ingresa una palabra: ")# Indicar al usuario que ingrese una palabra
# y asignarlo a la variable user_word.

user_word = user_word.upper()
for letter in user_word:
    if  letter == "A":
        continue
    elif letter == "E":
        continue
    elif letter == "I":
        continue
    elif letter == "O":
        continue
    elif letter == "U":
        continue
    print(letter)# Completa el cuerpo del bucle for.

'''Aqui se hace uso del ciclo for del if-elif-else y la palabra continue haciendo que el 
usuario pueda ingresar una palabra y depsues de eso si la palabra tiene vocales estan seran 
omitidas y solo imprimira las consonantes''' 