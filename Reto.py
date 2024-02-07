#TRANSACCIONES DE TU CUENTA BANCARIA. MUESTRA TU SALDO TOTAL Y LA MEDIA

Transacc= []
Tx=input("Introduce tu primer transaccion. Para terminar introduce 'f': ")
while Tx!= 'f':
    Transacc.append(int(Tx))
    Tx=input("Introduce tu siguiente transaccion. Para terminar introduce 'f': ")

suma= 0
for i in Transacc:   
    suma += i 
print("Tu saldo total es de: ", suma, "euros" ) #sum(Tx[i])/i)
print("La media es: ", float(suma/len(Transacc)), "euros")
