"""
LISTA SIMPLEMENTE ENLAZADA
Nodos y recursividad
"""

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.next = None
        self.cont = 1

    def agregar(self, valor):
        if self.next:
            self.next.agregar(valor)
        else:
            self.next = Nodo(valor)

    # def listar(self):
    #     print(self.valor)
    #     if self.next:
    #         self.next.listar()

    def listar(self):
        if self.next:
            siguiente = self.next.listar()
        else:
            return self.valor

        return f"{self.valor} {siguiente}"

    def contar(self):
        ls = self.listar().split(" ")
        return len(ls)

lista = Nodo(5)
lista.agregar(3)
lista.agregar(9)
lista.agregar(11)
lista.agregar(6)


lista_completa = lista.listar()
print(lista_completa)

cant_nodos = lista.contar()
print(cant_nodos)

