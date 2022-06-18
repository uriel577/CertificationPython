# Nombre: Pablo Uriel Rosas Vargas
# Fecha: 15 de Junio de 2022
# Descripcion: Uso de if-elif-else para años bisiestos

year = int(input("Introduce un año: "))

if year < 1582:
    print("No esta dentro del período del calendario Gregoriano")
elif year % 4 != 0:
    print("Es un año comun")
elif year % 100 != 0:
    print("El año es bisiesto")
elif year % 400 != 0:
    print("Es un año comun")
else:
    print("Es un año bisiesto")

'''Aqui se ingresa un año y a partir de ahi se llevaran a cabo una serie de 
condiciones para ver si es un año bisiesto o normal ademas de tener en cuenta 
que el Calendario Gregoriano(calendario actual) se enpezo a usar en el año 
1582 (dato de cital importancia)'''