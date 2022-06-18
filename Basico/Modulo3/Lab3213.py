# Nombre: Pablo Uriel Rosas Vargas
# Fecha: 15 de Junio de 2022
# Descripcion: Usar el While de forma basica

secret_number = 777
print(
"""
+==================================+
| ¡Bienvenido a mi juego, muggle!  |
| Introduce un número entero       |
| y adivina qué número he          |
| elegido para ti.                 |
| Entonces,                        |
| ¿Cuál es el número secreto?      |
+==================================+
""")
number = int(input("Ingresa el numero a adivinar: "))
while number != secret_number:
    print("¡Ja, ja! ¡Estás atrapado en mi bucle!")
    number = int(input("Ingresa el numero a adivinar: "))

if number == secret_number:
    print("¡Bien hecho, muggle! Eres libre ahora")
    