# Nombre: Pablo Uriel Rosas Vargas
# Fecha: 15 de Junio de 2022
# Descripcion: Saber si un numero es primo o impar

# 1 milla (mile) = 1609.344 metros(metres)
# 1 galón (gallon) = 3.785411784 litros(litres)
    
def liters_100km_to_miles_gallon(litres):
    gallons = litres / 3.785411784
    miles = 100 * 1000 / 1609.344
    return miles / gallons

def miles_gallon_to_liters_100km(miles):
    km100 = miles * 1609.344 / 1000 / 100
    litres = 3.785411784
    return litres / km100

print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))

'''Se usan dos fucniones para convertir los listros por kilometos y los litros por millas 
despues se mandan a imprimir los valores dependiendo de los litros que le usario tenga
sera la cantidad de millas avanzadas por galon'''