# Nombre: Pablo Uriel Rosas Vargas
# Fecha: 15 de Junio de 2022
# Descripcion: Uso de if para comparacion de cadenas

n = input("Ingresa la palabra: ")

if n == "ESPATIFILO":
    print("Si, ¡El ESPATIFILIO! es la mejor planta de todos los tiempos!")
else:
    if n == "espatifilo":
        print("No, ¡quiero un gran ESPATIFILIO!")
    else:
        print(f"¡ESPATIFILIO!, ¡No {n}!")

'''Se usa el if y el else para saber si una cadenas es como se esperaba 
usando los operadores de comparacion si la palabra es la esperada
lanzara un mensaje de exito y si no lanzara un mensaje de decepcion'''