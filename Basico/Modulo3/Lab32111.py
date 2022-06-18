# Nombre: Pablo Uriel Rosas Vargas
# Fecha: 15 de Junio de 2022
# Descripcion: Uso de if-elif-else con for y continue

word_without_vowels = ""

user_word = input("Ingrese una palabra: ")# Indicar al usuario que ingrese una palabra
# y asignarla a la variable user_word.

user_word = user_word.upper()
for letter in user_word:
    if letter == "A":
        continue
    elif letter == "E":
        continue
    elif letter == "I":
        continue
    elif letter == "O":
        continue
    elif letter == "U":
        continue
    word_without_vowels = word_without_vowels + letter


print(word_without_vowels)# Imprimir la palabra asignada a word_without_vowels.

'''Aqui se hace uso del ciclo for del if-elif-else y la palabra continue haciendo que el 
usuario pueda ingresar una palabra y depsues de eso si la palabra tiene vocales estan seran 
omitidas y solo imprimira las consonantes agregando que ahora las imprimira en una sola linea
es decir no realizara saltos de linea''' 