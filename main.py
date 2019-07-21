class Fila(object):
    """Clase base de fila"""
    def __init__(self):
        """constructor de la clase Fila """
        self.enfila = 0
        self.fila = []
  


class FilaPreferencial(Fila):
    """Clase de la fila de los clientes preferenciales"""        

    def insertar(self, cliente):
        """Inserta un nuevo cliente en la fila preferencial"""
        self.fila.append(cliente)
        self.enfila+=1

    def atender(self):
        """Atiende al proximo cliente prederencial"""
        self.enfila-=1
        self.fila.pop(0)
    
    def abrircajanueva(self,maxenfila):
        """Si maxenfila es menor que la cantidad de clientes actualmente en espera, abro nueva caja"""
        filanueva= self.enfila // maxenfila
        filanueva+=1
        return filanueva
    def contar(self):
        """Atiende al proximo cliente prederencial"""
        return self.enfila
    
    
class FilaGeneral(Fila):
    """Clase que mantiene una fila de clientes no preferenciales"""

    def insertar(self, cliente):
        """Inserta un nuevo cliente en la fila no preferencial"""
        self.fila.append(cliente)
        self.enfila+=1

    def atender(self):
        """Atiende al proximo cliente General"""
        self.enfila-=1
        self.fila.pop(0)

    def sacar(self):
        """Inserta un nuevo cliente en la fila no preferencial"""
        self.enfila-=1
        self.fila.pop(0)
    def contar(self):
        """Atiende al proximo cliente prederencial"""
        return self.enfila
    

class cliente(object):
    """clase cliente """
    def __init__(self,dni):
        """ constructor de la clase cliente """
        self.dni=dni
        self.categoria=None
    def modificarcategoria(self, categoria):
        """modifica el atributo categoria del cliente """
        self.categoria= categoria 

class printtofile(object):
    def imprimir(file,cont,npref,ngen,nclientes):
        L = [str(cont)," ",str(npref)," ",str(ngen)," ",str(nclientes),"\n"]   
        file.writelines(L)

    
if __name__ == "__main__":
    """ simular una fila en una entidad bancaria"""
