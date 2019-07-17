from main import cliente, FilaPreferencial, FilaGeneral
from random import randint,uniform
maxenfila= 10
filanueva=1
tol=0.5
tol_at_p=0.5
tol_at_g=0.2
tol_cb_g_p=0.8
tol_entrar=0.6
filapref1= FilaPreferencial()
filagen1= FilaGeneral()
clientespool= []
for i in range(1,10000):
    n=randint(1,44000000)
    clientespool.append(cliente(n))
    if uniform(0,1) < tol:
        clientespool[-1].modificarcategoria('Preferencial') 
    else:
        clientespool[-1].modificarcategoria('General') 
#    print(clientespool[-1].dni,clientespool[-1].categoria)
    if clientespool[-1].categoria == 'Preferencial':
        filapref1.insertar(clientespool[-1])
    else:
        filagen1.insertar(clientespool[-1])    
while filagen1.enfila!=0 or filapref1.enfila!=0:
    if uniform(0,1) < tol_cb_g_p and filapref1.enfila ==0: 
        clientespool[0].modificarcategoria('Preferencial') 
        filapref1.insertar(clientespool[0])
        filagen1.sacar()
    if uniform(0,1) < tol_entrar: 
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
    filapref1.abrircajanueva(maxenfila,filanueva)
    for i in range(1,filanueva+1):
        if uniform(0,1) < tol_at_p and filapref1.enfila !=0:
            filapref1.atender()
            clientespool.pop(0)
    if uniform(0,1) < tol_at_g and filagen1.enfila !=0: 
        filagen1.atender()
        clientespool.pop(0)
    print (filapref1.enfila,filagen1.enfila,len(clientespool))





