#Pedimos los número uno a uno
numero1= int(input("ingrese 3 número diferentes: "))
numero2= int(input("ingrese 3 número diferentes: "))
numero3= int(input("ingrese 3 número diferentes: "))

        #Hacemos todas las comparaciones posibles entre los 3 números
if numero1 > numero2:
    if numero2>numero3:
        print("Los números en orden creciente son: ",numero3, numero2, numero1)
elif numero1>numero3:
    print("Los números en orden creciente son: ",numero2, numero3, numero1)
else:
    print("Los números en orden creciente son: ",numero2, numero1, numero3)    
else:
    if numero1>numero3:
        print("Los números en orden creciente son: ",numero3, numero1, numero2)

elif numero2>numero3:
    print("Los números en orden creciente son: ",numero1, numero3, numero2)       
else:
    print("Los números en orden creciente son: ",numero1, numero2, numero3)
        exit()                    
    except ValueError:
        print("Debe ingresar un número de tipo entero")