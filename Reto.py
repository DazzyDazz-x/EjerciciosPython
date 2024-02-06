#TRANSACCIONES DE TU CUENTA
""" Tx=input("Introduce tu primer transaccion, para terminar introduce 'F': ")
sum=0
while Tx!= 'F':
    sum=sum +int(Tx)
    Tx=input("Introduce tu siguiente transaccion, para terminar introduce 'F': ")
print("Tu saldo total es de: ", int(sum))   """  


Transacc= []
Tx=input("Introduce tu primer transaccion, para terminar introduce 'F': ")
while Tx!= 'F':
    Transacc.append(int(Tx))
    Tx=input("Introduce tu siguiente transaccion, para terminar introduce 'F': ")

suma= 0
for i in Transacc:   
    suma += i 
print("Tu saldo total es de: ", suma ) #sum(Tx[i])/i)
print("La media es: ", float(suma/Len(Transacc))
