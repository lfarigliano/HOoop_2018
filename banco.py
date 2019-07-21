from main import cliente, FilaPreferencial, FilaGeneral,printtofile
from random import randint,uniform
maxenfila= 100
filanueva=1
tol=0.8
tol_at_p=0.4
tol_at_g=0.1
tol_cb_g_p=0.5
tol_entrar=0.4
filapref1= FilaPreferencial()
filagen1= FilaGeneral()
archivo= printtofile()
clientespool= []
file = open("reultado.oop.dat","w")
for i in range(1,10000):
    n=randint(1,44000000)
    clientespool.append(cliente(n))
    if uniform(0,1) < tol:
        clientespool[-1].modificarcategoria('Preferencial') 
    else:
        clientespool[-1].modificarcategoria('General') 
    if clientespool[-1].categoria == 'Preferencial':
        filapref1.insertar(clientespool[-1])
    else:
        filagen1.insertar(clientespool[-1])    
cont=0
while filagen1.enfila!=0 or filapref1.enfila!=0:
    cont+=1
    if uniform(0,1) < tol_cb_g_p and filagen1.enfila !=0: 
        clientespool[0].modificarcategoria('Preferencial') 
        filapref1.insertar(clientespool[0])
        filagen1.sacar()
    if uniform(0,1) < tol_entrar: 
        n=randint(1,44000000)
        clientespool.append(cliente(n))
#        if uniform(0,1) < tol:
#            clientespool[-1].modificarcategoria('Preferencial') 
#        else:
        clientespool[-1].modificarcategoria('General') 
#        if clientespool[-1].categoria == 'Preferencial':
#            filapref1.insertar(clientespool[-1])
#        else:
        filagen1.insertar(clientespool[-1])    
    filanueva=filapref1.abrircajanueva(maxenfila)
    for i in range(1,filanueva+1):
        if uniform(0,1) < tol_at_p and filapref1.enfila !=0:
            filapref1.atender()
            clientespool.pop(0)
    if uniform(0,1) < tol_at_g and filagen1.enfila !=0: 
        filagen1.atender()
        clientespool.pop(0)
    npref=filapref1.contar()    
    ngen=filagen1.contar() 
    nclientes=len(clientespool)
    printtofile.imprimir(file,cont,npref,ngen,nclientes)





