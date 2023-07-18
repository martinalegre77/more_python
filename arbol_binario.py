"""
ARBOL BINARIO

# [9, 5, 35, 2, 7, 23]
"""

class Tree:
    def __init__(self) -> None:
        self.root = None

    def add_node(self, value):
        if self.root:
            self.root.add_node(value)
        else:
            self.root = Nodo_tree(value)

    def buscar_valor(self, value):
        print(f"Buscando valor {value}")
        if self.root:
            self.root.buscar_valor(value)
        else:
            print("El valor no existe en el árbol")

class Nodo_tree:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None

    def add_node(self, value):
        if value < self.value:
            # insertar en el nodo de la izquierda
            if self.left:
                self.left.add_node(value)
            else:
                self.left = Nodo_tree(value)
        elif value > self.value:
            # insertar en el nodo de la derecha
            if self.right:
                self.right.add_node(value)
            else:
                self.right = Nodo_tree(value)

    def buscar_valor(self, value):
        if value == self.value:
            print("Valor encontrado!")
        elif value < self.value:
            if self.left:
                self.left.buscar_valor(value)
            else:
                print("El valor no existe")
        elif value > self.value:
            if self.right:
                self.right.buscar_valor(value)
            else:
                print("El valor no existe")

arbolito = Tree()

arbolito.add_node(9)
arbolito.add_node(5)
arbolito.add_node(35)
arbolito.add_node(2)
arbolito.add_node(7)
arbolito.add_node(23)

arbolito.buscar_valor(8)