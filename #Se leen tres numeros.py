#Se leen tres numeros

#¿Comó identificar el mayor de los tres numeros?
number1 = int(input("ingresa el primer numero: "))
number2 = int(input("ingresa el segundo numero: "))
number3 = int(input("ingrese el tercer numero: "))

#Elige el numero más grande

if number1 > number2 and number1 > number3:  #si el numero uno es mayor a dos y si uno es mayor a tres
    print("El numero mayor es: ",number1)
elif number2 > number1 and number2 > number3:
    print("El numero mayor es: ", number2)
elif number3 > number1 and number3 > number2:
    print("El numero mayor es:", number3)


#Elige el numero menor 
    
if number1 < number2 and number1 < number3:  #si el numero uno es menor a dos y si uno es menor a tres
    print("El numero menor es: ",number1)
elif number2 < number1 and number2 < number3:
    print("El numero menor es: ", number2)
elif number3 < number1 and number3 < number2:
    print("El numero menor es:", number3)

     