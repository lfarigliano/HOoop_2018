from main import cliente, FilaPreferencial, FilaGeneral
from random import randint,uniform
tol=0.1
filapref1= FilaPreferencial()
filagen1= FilaGeneral()
clientespool= []
for i in range(1,100):
    n=randint(1,44000000)
    clientespool.append(cliente(n))
    if uniform(0,1) < tol:
        clientespool[-1].modificarcategoria('Preferencial') 
    else:
        clientespool[-1].modificarcategoria('General') 
    print(clientespool[-1].dni,clientespool[-1].categoria)
    if clientespool[-1].categoria == 'Preferencial':
        filapref1.insertar(clientespool[-1])
    else:
        filagen1.insertar(clientespool[-1])    
    print (filapref1.enfila,filagen1.enfila)

#while true:
    



