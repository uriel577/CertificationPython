# Nombre: Pablo Uriel Rosas Vargas
# Fecha: 15 de Junio de 2022
# Descripcion: Creando una funcion para años bisiestos o comunes

def is_year_leap(year):
	if year % 4 != 0:
		return False
	elif year % 100 != 0:
		return True
	elif year % 400 != 0:
		return False
	else:
		return True

test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]
for i in range(len(test_data)):
	yr = test_data[i]
	print(yr,"-> ",end="")
	result = is_year_leap(yr)
	if result == test_results[i]:
		print("OK")
	else:
		print("Fallido")

'''Se crea una funcion para que regrese un True o False dependiendo si es un año
bisiesto o normal, despues se usan las cadenas para poder ver si cumple con otros 
parametros que se usan en la parte final del codigo'''