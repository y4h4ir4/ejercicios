#edad de los niños

n1=int(input("ingrese la edad 1: "))
n2=int(input("ingrese la edad 2: "))
n3=int(input("ingrese la edad 3: "))
n4=int(input("ingrese la edad 4: "))
n5=int(input("ingrese la edad 5: "))
n6=int(input("ingrese la edad 6: "))
n7=int(input("ingrese la edad 7: "))
n8=int(input("ingrese la edad 8: "))

pre_kinder=0 #contador de edad 4
kinder=0 #contador de edad 5
prepa=0 #contador de edad 6

if (3<n1<=6) and (3<n2<=6) and (3<n3<=6) and (3<n4<=6)  and (3<n5<=6) and (3<n6<=6) and (3<n7<=6) and (3<n8<=6):
    if n1==4:
        pre_kinder=pre_kinder+1
    if n2==4:
        pre_kinder=pre_kinder+1
    if n3==4:
        pre_kinder=pre_kinder+1
    if n4==4:
        pre_kinder=pre_kinder+1
    if n5==4:
        pre_kinder=pre_kinder+1
    if n6==4:
        pre_kinder=pre_kinder+1
    if n7==4:
        pre_kinder=pre_kinder+1
    if n8==4:
        pre_kinder=pre_kinder+1
    print(pre_kinder, "Niños de pre_kinder") 

    if n1==5:
        kinder=kinder+1
    if n2==5:
        kinder=kinder+1
    if n3==5:
        kinder=kinder+1
    if n4==5:
        kinder=kinder+1
    if n5==5:
        kinder=kinder+1
    if n6==5:
        kinder=kinder+1
    if n7==5:
        kinder=kinder+1
    if n7==5:
        kinder=kinder+1
    if n8==5:
        kinder=kinder+1
    print(kinder,"Niños de kinder")

    if n1==6:
        prepa=prepa+1
    if n2==6:
        prepa=prepa+1
    if n3==6:
        prepa=prepa+1
    if n4==6:
        prepa=prepa+1
    if n5==6:
        prepa=prepa+1
    if n6==6:
        prepa=prepa+1
    if n7==6:
        prepa=prepa+1
    if n8==6:
        prepa=prepa+1
    print(prepa,"Niños de prepa")
else: 
    print("No valido")   

