# Nombre: Pablo Uriel Rosas Vargas
# Fecha: 15 de Junio de 2022
# Descripcion: Saber si un numero es primo o impar

def is_prime(num):
    for i in range(2, int(1 + num ** 0.5)):
        if num % i == 0:
            return False
    return True

for i in range(1, 20):
    if is_prime(i + 1):
        print(i + 1, end=" ")
print()

'''Se uda un for para tomar el numero '''
