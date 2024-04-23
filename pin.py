pin = int(input("ingrese su pin"))


if pin < 9999999999:
    print("ERROR")

n1 = pin // 10000000
n2 = pin % 10000000
n3 = n2 // 100000
n3 = pin % 100000
n4 = pin // 1000000
n5 = pin % 100000
n6 = pin // 10000
n7 = pin % 10000
n8 = pin // 1000


