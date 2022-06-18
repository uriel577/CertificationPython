# Nombre: Pablo Uriel Rosas Vargas
# Fecha: 15 de Junio de 2022
# Descripcion: Uso de ciclo for anidado

income = float(input("Introduce el ingreso anual: "))

if income <= 0.0:
    tax = income * 0.0
else:
    if income <= 85529 and income>0:
        tax = (income * 0.18) - 556.2
    else:
        tax = 14839.2 + (income-85528)*0.32

tax = round(tax, 0)
print("El impuesto es:", tax, "pesos")

'''Usamos el if para saber cunto se debe descontar de taxas(impuestos)
por ganar cierta cantidad de dinero tomando en cuenta que cuando la ganancia es
por debajo de cero(negativa) las taxas se reducen a cero tambien'''