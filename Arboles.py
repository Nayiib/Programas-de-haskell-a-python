class binario():
    def__init__(self,valor, izq=None,der = None)
    self.valor=valor
    self.izq=izq
    self.der=der

def buscar(arbol,valor):
    if arbol==None:
        return False
    elif arbol.valor==valor:
        return True
    elif arbol.valor>valor:
        return buscar(arbol.izq.valor)
    else:
        return buscar(arbol.der.valor)
