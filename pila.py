"""
PILA (Stack) - FIFO
"""

class Stack:
    def __init__(self) -> None:
        self.nodo = None

    def push(self, valor):
        if self.nodo:
            new = Nodo_pila(valor, self.nodo)
        else:
            self.nodo = Nodo_pila(valor, None)

    def pop(self):
        if self.nodo:
            valor = self.nodo.valor
            if self.nodo.next:
                self.nodo = self.nodo.next
            else:
                self.nodo = None
            return valor
        else:
            print("Pila vacía")


class Nodo_pila:
    def __init__(self, valor, next):
        self.valor = valor
        self.next = next

    
if __name__ == "__main__":
    from random import randint

    pila = Stack()

    for i in range(10):
        pila.push(randint(1, 50))

    print(pila)

    print(pila.pop())