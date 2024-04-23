CREAR UN PROGRAMA QUE PERMITA REALIZAR 20 RETIROS DE UN CAJERO AUTOMATICO TENIENDO EN CUENTA LAS DENOMINACIONES EN BILLETES DE 50000, 20000, 10000, 5000, 2000 Y 1000, SE DEBE VALIDAR CONSTANTEMENTE
DINERO DISPONIBLE EN EL CAJERO
caja [ 10, 10, 10, 10, 10, 10] 6 valores [50000, 20000, 10000, 5000, 2000, 1000]

b2-8
b3e
b48
b50
b60
for i in range(1, 21):

b1 retiro / 50000

retiro int(input("\nFavor ingresar valor de retiro: "))
rt retiro
if(retiro (bi valores[0]) >=0): retiro retiro (bl valores[0]) b2 retiro / 20000
if(retiro (b2"valores[1]) >=0): retiro retiro (b2"valores[1]) b3 retiro / 10000
if(retiro (b3*valores [2]) >=0) retiro retiro (b3 valores [2]) b4 retiro / 5000
if(retiro (b4"valores [3]) >=0): retiro retiro (b4"valores[3]) b5 retiro / 2000
if(retiro (b5°valores [4]) >=0): retiro retiro (b5 valores[4]) b6 retiro / 1000
if(retiro (b6"valores[5]) >= 0); retiro retiro (bé valores [5])
if(int(rt % 1000)--0):
cajero caja[0]"valores[0]+caja [1]"valores[1]+caja[2]"valores[2]+caja[3]"valores[3]+caja[4]"valores [4]+
caja[5]*valores [5]
if(cajero > retiro):
caja[0] = caja[0] - bl
caja[1]= caja [1] - b2
caja [2] caja [2] - b3
caja [3] caja [3]
caja [4]

else:
0
b4
caja[4]- b5
caja [5] caja [5] - b6
print("Retiro exitoso") else:
print("\nsin efectivo en el cajero para esta transaccion")
print("\nfavor ingresar una cantidad redondeada en billetes de 50000, 20000, 10000, 5000, 2000, 1000" )
61 print("\n\nBilletes en cajero: Vn58009: +str(caja[@])+ "\n20000: "+str(caja[1])+"\n10000: "+str(caja[2])+
62 "\n5000: "+str(caja[3])+"\n2000: "+str(caja[4])+"\1000; +str(caja[5]))