

dia = int(input("Ingresa el dia: "))
mes = int(input("Ingresa el mes: "))
año = int(input("ingresa el año: "))

if (año % 4 == 0 and año % 100 != 0) or (año % 100 == 0 and año % 400 == 0):
    
if dia<1 or dia>31:
    print("Día invalido")

if mes<1 or mes>12:
    print("Mes invalido")

else:
    print(f"La fecha es invalida, no es año bisiesto")
