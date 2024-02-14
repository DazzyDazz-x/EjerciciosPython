#Gestión de los correos electrónicos
emails=["jon.smith@microsoft.com", "maria.fernandez@microsoft.com", "david@microsoft.com", "isabel@microsoft.es","alfonso@gmail.com"]
Nombres=[]
Dominios=[]
for c in emails:
    x,y= c.split("@")
    Nombres.append(x)
    Dominios.append(y)

#Informe
sTexto="Informe de usuarios\n"        
for i in Nombres:
    sTexto= sTexto+ i+ "," 
sTexto= sTexto[:-1]    #quitamos el ultimo

sTexto = sTexto + "\n Aqui son los dominios: \n"
     

setDominios= set(Dominios)
for i in setDominios:

    sTexto= sTexto+","+i

#Guardamos informe en un archivo
print(sTexto)



with open("informe.txt", "w") as f:
    f.write(sTexto)
      
    


