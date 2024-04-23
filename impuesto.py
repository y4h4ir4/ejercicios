ingreso = float(input("Introduce el ingreso anual:"))

if ingreso<=85528: 
    print("El impuesto a pagar: ", round((ingreso*18/100)-556.02,1))
elif ingreso>85528:

   tax=14839.02+((ingreso-85528)*32/100)

tax = round(tax, 0)

print("El impuesto es:", tax, "pesos")