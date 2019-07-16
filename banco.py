from main import cliente, FilaPreferencial, FilaGeneral
from random import randint,uniform
tol=0.1
filapref1= FilaPreferencial()
filagen1= FilaGeneral()
clientespool= []
for i in range(1,100):
    n=randint(1,44000000)
    clientespool.append(cliente(n))
    print(i)
    print(clientespool[-1].dni)
#    if uniform(0,1) < tol:
#        cliente1.modificarcategoria('Preferencial') 
#    else:
#        cliente1.modificarcategoria('General') 
#    cliente1.testcliente(n)
#    if cliente1.categoria == 'Preferencial':
#        filapref1.insertar(cliente1)
#    else:
#        filagen1.insertar(cliente1)    
#    print (filapref1.enfila,filagen1.enfila)
#
#while true:
    



