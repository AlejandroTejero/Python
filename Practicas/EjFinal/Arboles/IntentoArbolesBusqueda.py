from Stack import Stack
'''class Bt:
    def __init__(self,item=None,izquierda=None,derecha=None):
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

    def contiene(self,item):
        if self.esta_vacio():
            return False
        else:
            return (self.item == item
                    or (self.izquierda.contiene(item) if self.izquierda else False)
                    or (self.derecha.contiene(item) if self.derecha else False))

    def nodes(self):
        if self.esta_vacio():
            return False
        else:
            return 1 + (self.izquierda.nodes() if self.izquierda else 0) + (self.derecha.nodes() if self.derecha else 0)

    def depth(self):
        if self.esta_vacio():
            return False
        else:
            return 1 + max((self.izquierda.depth() if self.izquierda else 0),(self.derecha.depth() if self.derecha else 0))

    def print_inorder(self):
        if not self.esta_vacio():
            if self.izquierda:
                self.izquierda.print_inorder()
            print(self.item)
            if self.derecha:
                self.derecha.print_inorder()

    def print_preorder(self):
        if not self.esta_vacio():
            print(self.item)
            if self.izquierda:
                self.izquierda.print_preorder()
            if self.derecha:
                self.derecha.print_preorder()

    def print_posorder(self):
        if not self.esta_vacio():
            if self.izquierda:
                self.izquierda.print_posorder()
            if self.derecha:
                self.derecha.print_posorder()
            print(self.item)

    def print_menor_mayor(self):
        if not self.esta_vacio():
            if self.izquierda:
                self.izquierda.print_posorder()
            print(self.item)
            if self.derecha:
                self.derecha.print_posorder()

    def print_mayor_menor(self):
        if not self.esta_vacio():
            if self.derecha:
                self.derecha.print_posorder()
            print(self.item)
            if self.derecha:
                self.derecha.print_posorder()

    def preorder(self):
        if self.esta_vacio():
            return []
        else:
            return [self.item] + (self.izquierda.preorder() if self.izquierda else []) + (self.derecha.preorder() if self.derecha else [])

    def inorder(self):
        if self.esta_vacio():
            return []
        else:
            return (self.izquierda.inorder() if self.izquierda else []) + [self.item] +  (self.derecha.inorder() if self.derecha else [])

    def posorder(self):
        if self.esta_vacio():
            return []
        else:
            return (self.izquierda.posorder() if self.izquierda else []) +  (self.derecha.posorder() if self.derecha else []) + [self.item]


def evaluate(arbol:Bt):
    if arbol.esta_vacio():
        return 0
    else:
        if isinstance(arbol.get_item(),int):
            return arbol.get_item()

        resultado_izquierdo = evaluate(arbol.get_izquierda())
        resultado_derecha = evaluate(arbol.get_derecha())

        if arbol.get_item() == '+':
            return resultado_izquierdo + resultado_derecha
        elif arbol.get_item() == '-':
            return resultado_izquierdo - resultado_derecha
        elif arbol.get_item() == '*':
            return resultado_izquierdo * resultado_derecha
        elif arbol.get_item() == '/':
            return resultado_izquierdo / resultado_derecha


def evaluate_v2(arbol: Bt):
    if arbol.esta_vacio():
        return 0
    else:
        pila = Stack()
        expresion = arbol.posorder()
        for item in expresion:
            if isinstance(item,int):
                pila.push(item)
            else:
                derecha = pila.pop()
                izquierda = pila.pop()
                if item == '+':
                    pila.push(izquierda + derecha)
                elif item == '-':
                    pila.push(izquierda - derecha)
                elif item == '*':
                    pila.push(izquierda * derecha)
                elif item == '/':
                    pila.push(izquierda / derecha)

izq1 = Bt(7)
der1 = Bt(3)
izq2 = Bt(5)
der2 = Bt(2)

suma = Bt('+',izq1,der1)
resta = Bt('+',izq2,der2)

arbol = Bt('*',suma,resta)

print(f"El resultado es {evaluate(arbol)}")'''

class Bt:
    def __init__(self,item=None,izquierda=None,derecha=None):
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

    def contiene(self,item):
        if self.esta_vacio():
            return False
        else:
            return (item == self.item
                    or (self.izquierda.contiene(item) if self.izquierda else False)
                    or (self.derecha.contiene(item) if self.derecha else False))

    def nodes(self):
        if self.esta_vacio():
            return 0
        else:
            return 1 + (self.izquierda.nodes() if self.izquierda else 0) + (self.derecha.nodes() if self.derecha else 0)

    def depth(self):
        if self.esta_vacio():
            return 0
        else:
            return 1 + max((self.izquierda.nodes() if self.izquierda else 0),(self.derecha.nodes() if self.derecha else 0))

    def print_inorder(self):
        if not self.esta_vacio():
            if self.izquierda:
                self.izquierda.print_inorder()
            print(self.item)
            if self.derecha:
                self.derecha.print_inorder()

    def inorder(self):
        if self.esta_vacio():
            return []
        else:
            return (self.izquierda.inorder() if self.izquierda else []) + [self.item] + (self.derecha.inorder if self.derecha else [])

    def posorder(self):
        if self.esta_vacio():
            return []
        else:
            return (self.izquierda.inorder() if self.izquierda else []) + (self.derecha.inorder if self.derecha else [])+ [self.item]


def evaluate(arbol: Bt):
    if arbol.esta_vacio():
        return None
    else:
        if isinstance(arbol.get_item(),int):
            return arbol.get_item()

        resultado_izq = evaluate(arbol.get_izquierda())
        resultado_der = evaluate(arbol.get_derecha())
        if arbol.get_item() == '+':
            return resultado_izq + resultado_der
        elif arbol.get_item() == '-':
            return resultado_izq - resultado_der
        elif arbol.get_item() == '*':
            return resultado_izq * resultado_der
        elif arbol.get_item() == '/':
            return resultado_izq / resultado_der

def evaluate_v1(arbol:Bt):
    if arbol.esta_vacio():
        return None
    else:
        pila = Stack()
        numeros = arbol.posorder()
        for item in numeros:
            if isinstance(item(),int):
                pila.push(item)
            else:
                result_izq = pila.pop()
                result_der = pila.pop()
                if item == '+':
                    pila.push(result_der + result_izq)
                elif item == '-':
                    pila.push(result_der - result_izq)
                elif item == '*':
                    pila.push(result_der * result_izq)
                elif item == '/':
                    pila.push(result_der / result_izq)

        return pila.pop()

izq1 = Bt(7)
der1 = Bt(3)
izq2 = Bt(5)
der2 = Bt(2)

suma = Bt('+',izq1,der1)
resta = Bt('+',izq2,der2)

arbol = Bt('*',suma,resta)

print(f"El resultado es {evaluate(arbol)}")