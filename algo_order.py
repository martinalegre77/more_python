"""
Algoritmo de ordenamiento
"""

class Lista_se:
    def __init__(self) -> None:
        self.nodo = None

    def agregar(self, valor):
        if self.nodo:
            self.nodo.agregar(valor)
        else:
            self.nodo = Nodo_se(valor)

    def listar(self):
        return self.nodo.listar()

    def size(self):
        if self.nodo:
            return self.nodo.size()
        else:
            return 0

    def ordenar(self):
        if self.nodo:
            ordenando = True
            while ordenando:
                ordenando = self.nodo.ordenar()


class Nodo_se:
    def __init__(self, valor) -> None:
        self.valor = valor
        self.next = None

    def agregar(self, valor):
        if self.next:
            self.next.agregar(valor)
        else:
            self.next = Nodo_se(valor)

    def listar(self):
        if self.next:
            siguiente = self.next.listar()
        else:
            return self.valor

        return f"{self.valor} {siguiente}"

    def size(self):
        if self.next:
            elemento = 1
            return elemento + self.next.size()
        else:
            return 0

    def ordenar(self):
        if self.next:
            if self.valor > self.next.valor:
                change = self.valor
                self.valor = self.next.valor
                self.next.valor = change
                self.next.ordenar()
                return True
            else:
                return self.next.ordenar()
        else:
                return False

if __name__ == "__main__":
    from random import randint

    lista = Lista_se()

    for i in range(10):
        lista.agregar(randint(1, 50))
    
    print(lista.listar())

    lista.ordenar()

    print(lista.listar())