class Bt:
    def __init__(self, item: object = None, izquierda: object = None, derecha: object = None) -> object:
        self.item = item
        self.izquierda = izquierda
        self.derecha = derecha

    def get_item(self):
        return self.item

    def get_izquierda(self):
        return self.izquierda

    def get_derecha(self):
        return self.derecha

    def esta_vacio(self):
        return not self.item

    def contains(self,item):
        if self.esta_vacio():
            return 0
        else:
            return (self.item == item or (self.izquierda.contains(item) if self.izquierda else False)
                    or (self.derecha.contains(item) if self.derecha else False))

    def nodes(self):
        if self.esta_vacio():
            return 0
        else:
            return 1 + (self.izquierda.nodes() if self.izquierda else 0) + (self.derecha.nodes() if self.derecha else 0)

    def depth(self):
        if self.esta_vacio():
            return 0
        else:
            return 1 + max((self.izquierda.depth() if self.izquierda else 0),(self.derecha.depth() if self.derecha else 0))

    def print_menor_mayor(self):
        if not self.esta_vacio():
            if self.izquierda:
                self.izquierda.print_menor_mayor()
            print(self.item)
            if self.derecha:
                self.derecha.print_menor_mayor()

    def print_mayor_menor(self):
        if not self.esta_vacio():
            if self.derecha:
                self.derecha.print_mayor_menor()
            print(self.item)
            if self.izquierda:
                self.izquierda.print_mayor_menor()


    def print_preorder(self):
        if not self.esta_vacio():
            print(self.item)
            if self.izquierda:
                self.izquierda.print_preorder()
            if self.derecha:
                self.derecha.print_preorder()

    def print_inorder(self):
        if not self.esta_vacio():
            if self.izquierda:
                self.izquierda.print_inorder()
            print(self.item)
            if self.derecha:
                self.derecha.print_inorder()

    def print_posorder(self):
        if not self.esta_vacio():
            if self.izquierda:
                self.izquierda.print_posorder()
            if self.derecha:
                self.derecha.print_posorder()
            print(self.item)

    def posorder(self):
        if self.esta_vacio():
            return []
        else:
            return (self.izquierda.posorder if self.izquierda else []) + (self.derecha.posorder if self.derecha else []) + [self.item]

    def inorder(self):
        if self.esta_vacio():
            return []
        else:
            return (self.izquierda.posorder if self.izquierda else []) + [self.item] + (self.derecha.posorder if self.derecha else [])

    def preorder(self):
        if self.esta_vacio():
            return []
        else:
            return [self.item] + (self.izquierda.posorder if self.izquierda else []) + (self.derecha.posorder if self.derecha else [])


def evaluate(arbol: Bt):
    if arbol.esta_vacio():
        return 0
    else:
        if isinstance(arbol.get_item(),int):
            return arbol.get_item()

        resultado_izquierdo = evaluate(arbol.get_izquierda())
        resultado_derecho = evaluate(arbol.get_derecha())
        if arbol.get_item() == '+':
            return resultado_izquierdo + resultado_derecho
        elif arbol.get_item() == '-':
            return resultado_izquierdo - resultado_derecho
        elif arbol.get_item() == '*':
            return resultado_izquierdo * resultado_derecho
        elif arbol.get_item() == '/':
            return resultado_izquierdo / resultado_derecho

izq1 = Bt(7)
der1 = Bt(3)
izq2 = Bt(5)
der2 = Bt(2)

suma = Bt('+',izq1,der1)
resta = Bt('+',izq2,der2)

arbol = Bt('*',suma,resta)

print(f"EL resultado es {evaluate(arbol)}")

