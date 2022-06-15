#Autor: Pablo Uriel Rosas Vargas
#Fecha: 14 de Junio de 2022
#Descripcion: Evento hora de inicio y termino

hour = int(input("Hora de inicio (horas): "))
mins = int(input("Minuto de inicio (minutos): "))
dura = int(input("Duración del evento (minutos): "))

# calcula los minutos y los convierte a una cadena
minutos=str((mins+dura) %60)
# calcula los minutos totales y luego lo convierte a horas y despues a una cadena
horas = str( ((hour*60 + mins + dura)//60) % 24)
 
 
print("Hora: " +horas +":" +minutos)

'''Como se ve se usa tres varables para poder convertir las horas
depues de dar la hora y la duracion del eventos se toman estos datos para 
dar como resultado la hora en que comienza en levento y la hora en que termina'''