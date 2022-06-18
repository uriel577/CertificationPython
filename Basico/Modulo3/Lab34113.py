# Nombre: Pablo Uriel Rosas Vargas
# Fecha: 15 de Junio de 2022
# Descripcion: Manejo de listas

# paso 1:
Beatles = []
print("Paso 1:", Beatles)

# paso 2:

Beatles.append("John Lennon")
Beatles.append("Paul McCartney")
Beatles.append("George Harrison")
print("Paso 2:", Beatles)

# paso 3:
for members in range(2):
    Beatles.append(input("Nuevo miembro de la banda: "))
print("Paso 3:", Beatles)

# paso 4:
del Beatles[-1]
del Beatles[-1]
print("Paso 4:", Beatles)

# paso 5:
Beatles.insert(0, "RingoStarr")
print("Paso 5:", Beatles)
print("Los Fav:",len(Beatles))

'''Se usa una lista de los beatles para agregar, crear, eliminiar, e insertar a la lista de los 
beatles los diferentes integrantes'''