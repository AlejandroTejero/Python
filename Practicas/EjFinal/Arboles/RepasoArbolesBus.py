'Buenardo'
'''class BST:
    def __init__(self):
        self.item = None
        self.left = None
        self.right = None

    def is_empty(self):
        return not self.item  # return self.item is None

    def create_leave(self, item):
        self.item = item
        self.left = BST()
        self.right = BST()

    def add(self, item):
        if self.is_empty():
            self.create_leave(item)
        else:
            if item < self.item:
                self.left.add(item)
            elif item > self.item:
                self.right.add(item)
            else:
                self.item = item  # Comment

    def print_preorder(self):
        if not self.is_empty():
            print(self.item)
            self.left.print_preorder()
            self.right.print_preorder()

    def print_inorder(self):
        if not self.is_empty():
            self.left.print_inorder()
            print(self.item)
            self.right.print_inorder()

    def print_posorder(self):
        if not self.is_empty():
            self.left.print_posorder()
            self.right.print_posorder()
            print(self.item)

    def nodes(self):
        if self.is_empty():
            return 0
        else:
            return 1 + self.left.nodes() + self.right.nodes()

    def depth(self):
        if self.is_empty():
            return 0
        else:
            return 1 + max(self.left.depth(), self.right.depth())

    def contains(self, item):
        if self.is_empty():
            return False
        else:
            if self.item == item:
                return True
            elif item < self.item:
                return self.left.contains(item)
            else:
                return self.right.contains(item)

    def to_list(self):
        if self.is_empty():
            return []
        else:
            return self.left.to_list() + [self.item] + self.right.to_list()

    def remove(self, item):
        if self.is_empty():
            return False
        return self.remove_aux(item, None)

    def remove_aux(self, item, parent):
        if item < self.item:
            if not self.left.is_empty():
                return self.left.remove_aux(item, self)
        elif item > self.item:
            if not self.right.is_empty():
                return self.right.remove_aux(item, self)
        else:
            if not self.left.is_empty() and not self.right.is_empty():
                self.item = self.right.min()
                self.right.remove_aux(self.item, self)
            elif parent is None:  # delete root
                if not self.left.is_empty():
                    self.become(self.left)
                else:
                    self.become(self.right)
            elif parent.left == self:
                parent.left = self.left if not self.left.is_empty() else self.right
            elif parent.right == self:
                parent.right = self.left if not self.left.is_empty() else self.right
            return True
        return False

    def become(self, other):
        self.item = other.item
        self.left = other.left
        self.right = other.right

    def min(self):
        if not self.is_empty():
            if self.left.is_empty():
                return self.item
            else:
                return self.left.min()
        else:
            return None

    def remove_alt(self, item):
        if not self.is_empty():
            if item == self.item:
                items = self.left.to_list() + self.right.to_list()
                if items:
                    self.item = items.pop()
                else:
                    self.item = None
                self.left = BST()
                self.right = BST()
                if items:
                    for item in items:
                        self.add(item)
                return True
            elif item < self.item:
                return self.left.remove_alt(item)
            else:
                return self.right.remove_alt(item)
        return False

'Ejecucion'
bst = BST()
bst.add(7)
bst.add(3)
bst.add(5)
bst.add(10)
print("Preorder:")
bst.print_preorder()
print()
print("Inorder:")
bst.print_inorder()
print()
print("Posorder:")
bst.print_posorder()
print()
print(f"Nodes: {bst.nodes()}")
print(f"Depth: {bst.depth()}")
print(f"Contains 7? {bst.contains(7)}")
print(f"Contains 5? {bst.contains(5)}")
print(f"Contains 10? {bst.contains(10)}")
print(f"Contains 3? {bst.contains(3)}")
print(f"Contains 4? {bst.contains(4)}")
print(f"To list: {bst.to_list()}")
print("Remove 3:")
bst.remove(3)
bst.print_inorder()
print()
print("Remove 7:")
bst.remove(7)
bst.print_inorder()
print()
print("Remove 10:")
bst.remove(10)
bst.print_inorder()
print()
print("Remove 5:")
bst.remove(5)
bst.print_inorder()
print()
bst.add(1)
bst.add(2)
bst.add(3)
bst.add(4)
bst.add(5)
bst.print_inorder()'''

'Intento 1'
'''class Bts:
    def __init__(self):
        self.item = None
        self.izquierda = None
        self.derecha = None

    def esta_vacio(self):
        return self.item is None
        #return not self.item

    def crear_hoja(self,item):
        self.item = item
        self.izquierda = Bts()
        self.derecha = Bts()

    def add(self,item):
        if self.esta_vacio():
            self.crear_hoja(item)
        else:
            if item < self.item:
                self.izquierda.add(item)
            elif item > self.item:
                self.derecha.add(item)
            else:
                self.item = item

    def nodes(self):
        if self.esta_vacio():
            return 0
        else:
            return 1 + self.izquierda.nodes() + self.derecha.nodes()

    def depth(self):
        if self.esta_vacio():
            return 0
        else:
            return 1 + max(self.izquierda.depth(),self.derecha.depth())

    def contiene(self,item):
        if self.esta_vacio():
            return False
        else:
            if item == self.item:
                return True
            elif item < self.item:
                return self.izquierda.contiene(item)
            else:
                return self.derecha.contiene(item)

    def to_list(self):
        if self.esta_vacio():
            return []
        else:
            return self.izquierda.to_list() + [self.item] + self.derecha.to_list()

    def print_preorder(self):
        if not self.esta_vacio():
            print(self.item)
            self.izquierda.print_preorder()
            self.derecha.print_preorder()

    def print_inorder(self):
        if not self.esta_vacio():
            self.izquierda.print_inorder()
            print(self.item)
            self.derecha.print_inorder()

    def print_postorder(self):
        if not self.esta_vacio():
            self.izquierda.print_postorder()
            self.derecha.print_postorder()
            print(self.item)'''

'Intento 2'
'''class Bts:
    def __init__(self):
        self.item = None
        self.izquierda = None
        self.derecha = None

    def esta_vacio(self):
        return self.item is None

    def crear_hoja(self,item):
        self.item = item
        self.izquierda = Bts()
        self.derecha = Bts()

    def add(self,item):
        if self.esta_vacio():
            self.crear_hoja(item)
        else:
            if item < self.item:
                self.izquierda.add(item)
            elif item > self.item:
                self.derecha.add(item)
            else:
                self.item = item

    def nodes(self):
        if self.esta_vacio():
            return 0
        else:
            return 1 + self.izquierda.nodes() + self.derecha.nodes()

    def depht(self):
        if self.esta_vacio():
            return 0
        else:
            return 1 + max(self.izquierda.depth(),self.derecha.depht())

    def print_preorder(self):
        if not self.esta_vacio():
            print(self.item)
            self.izquierda.print_preorder()
            self.derecha.print_preorder()

    def print_inorder(self):
        if not self.esta_vacio():
            self.izquierda.print_inorder()
            print(self.item)
            self.derecha.print_inorder()

    def print_postorder(self):
        if not self.esta_vacio():
            self.izquierda.print_postorder()
            self.derecha.print_postorder()
            print(self.item)

    def contiene(self,item):
        if self.esta_vacio():
            return False
        else:
            if item == self.item:
                return True
            elif item < self.item:
                return self.izquierda.contiene(item)
            else:
                return self.derecha.contiene(item)

    def to_list(self):
        if self.esta_vacio():
            return []
        else:
            return self.izquierda.to_list() + [self.item] + self.derecha.to_list()


    def remove_alt(self,item):
        if not self.esta_vacio():
            if item == self.item:
                items = self.izquierda.to_list() + self.derecha.to_list()
                if items:
                    self.item = items.pop()
                else:
                    self.item = None
                self.izquierda = Bts()
                self.derecha = Bts()
                if items:
                    for item in items:
                        self.add(item)
                return True
            elif item < self.item:
                return self.izquierda.remove_alt(item)
            else:
                return self.derecha.remove_alt(item)
        return False'''

'Intento 3'
'''class Bts:
    def __init__(self):
        self.item = None
        self.izquierda = None
        self.derecha = None

    def esta_vacio(self):
        return self.item is None

    def crear_hoja(self,item):
        self.item = item
        self.izquierda = Bts()
        self.derecha = Bts()

    def add(self,item):
        if self.esta_vacio():
            self.crear_hoja(item)
        else:
            if item < self.item:
                self.izquierda.add(item)
            elif item > self.item:
                self.derecha.add(item)
            else:
                self.item = item

    def nodes(self):
        if self.esta_vacio():
            return 0
        else:
            return 1 + self.izquierda.nodes() + self.derecha.nodes()


    def depth(self):
        if self.esta_vacio():
            return 0
        else:
            return 1 + max(self.izquierda.depth(),self.derecha.depth())

    def contiene(self,item):
        if self.esta_vacio():
            return False
        else:
            if item == self.item:
                return True
            elif item < self.item:
                return self.izquierda.contiene(item)
            else:
                return self.derecha.contiene(item)


    def to_list(self):
        if self.esta_vacio():
            return []
        else:
            return self.izquierda.to_list() + [self.item] + self.derecha.to_list()

    def print_preorder(self):
        print(self.item)
        self.izquierda.print_preorder()
        self.derecha.print_preorder()

    def print_inorder(self):
        self.izquierda.print_inorder()
        print(self.item)
        self.derecha.print_inorder()

    def print_postorder(self):
        self.izquierda.print_postorder()
        self.derecha.print_postorder()
        print(self.item)

    def remove_alt(self,item):
        if not self.esta_vacio():
            if item == self.item:
                items = self.izquierda.to_list() + self.derecha.to_list()
                if items:
                    self.item = items.pop()
                else:
                    self.item = False
                self.izquierda = Bts()
                self.derecha = Bts()
                return False
            else:
                if item < self.item:
                    return self.izquierda.remove_alt(item)
                else:
                    return self.derecha.remove_alt(item)
        return False'''

'Intento 4'
'''class Bts:
    def __init__(self):
        self.item = None
        self.izquierda = None
        self.derecha = None

    def esta_vacio(self):
        return self.item is None

    def crear_hoja(self,item):
        self.item = item
        self.izquierda = Bts()
        self.derecha = Bts()

    def add(self,item):
        if self.esta_vacio():
            self.crear_hoja(item)
        else:
            if item < self.item:
                self.izquierda.add(item)
            elif item > self.item:
                self.derecha.add(item)
            else:
                self.item = item

    def contiene(self,item):
        if self.esta_vacio():
            return False
        else:
            if item == self.item:
                return True
            elif item < self.item:
                self.izquierda.contiene(item)
            else:
                self.derecha.contiene(item)


    def nodos(self):
        if self.esta_vacio():
            return 0
        else:
            return 1 + self.izquierda.nodos() + self.derecha.nodos()

    def depth(self):
        if self.esta_vacio():
            return 0
        else:
            return 1 + max(self.izquierda.depth(),self.derecha.depth())

    def to_list(self):
        if self.esta_vacio():
            return []
        else:
            return self.izquierda.to_list() + [self.item] + self.derecha.to_list()

    def print_preorder(self):
        print(self.item)
        self.izquierda.print_preorder()
        self.derecha.print_preorder()

    def print_inorder(self):
        self.izquierda.print_inorder()
        print(self.item)
        self.derecha.print_inorder()
    def print_postorder(self):
        self.izquierda.print_postorder()
        self.derecha.print_postorder()
        print(self.item)


    def remove_alt(self,item):
        if not self.esta_vacio():
            if item == self.item:
                items = self.izquierda.to_list() + self.derecha.to_list()
                if items:
                    self.item = items.pop()
                else:
                    self.item = None
                self.izquierda = Bts()
                self.derecha = Bts()
                return True
            else:
                if item < self.item:
                    self.izquierda.remove_alt(item)
                else:
                    self.derecha.remove_alt(item)
        return False'''

'Intento 5'
'''class Bts:
    def __init__(self):
        self.izquierda = None
        self.derecha = None

    def crear_hoja(self,item):
        self.item = item
        self.izquierda = Bts()
        self.derecha = Bts()

    def esta_vacio(self):
        return not self.item

    def add(self,item):
        if self.esta_vacio():
            self.crear_hoja(item)
        else:
            if item < self.item:
                self.izquierda.add()
            elif item > self.item:
                self.derecha.add()
            else:
                self.item = item

    def nodes(self):
        if self.esta_vacio():
            return 0
        else:
            return 1 + self.izquierda.nodes() + self.derecha.nodes()

    def depth(self):
        if self.esta_vacio():
            return 0
        else:
            return 1 + max(self.izquierda.nodes(),self.derecha.nodes())

    def to_list(self):
        if self.esta_vacio():
            return None
        else:
            return self.izquierda.nodes() + [self.item] + self.derecha.nodes()

    def contiene(self,item):
        if self.esta_vacio():
            return False
        else:
            if item == self.item:
                return True
            elif item < self.item:
                return self.izquierda.contiene(item)
            else:
                return self.derecha.contiene(item)

    def print_preorder(self):
        print(self.item)
        self.izquierda.print_preorder()
        self.derecha.print_preorder()

    def print_inorder(self):
        self.izquierda.print_inorder()
        print(self.item)
        self.derecha.print_inorder()

    def print_postorder(self):
        self.izquierda.print_postorder()
        self.derecha.print_postorder()
        print(self.item)

    def remove_alt(self,item):
        if not self.esta_vacio():
            if item == self.item:
                items = self.izquierda.to_list() + self.derecha.to_list()
                if items:
                    self.item = items.pop()
                else:
                    self.item = None
                self.izquierda = Bts()
                self.derecha = Bts()
                if items:
                    for item in items:
                        self.add(item)
                return True
            else:
                if item < self.item:
                    self.izquierda.remove_alt(item)
                else:
                    self.derecha.remove_alt(item)
        return False'''

'Intento 6'
'''class Bts:
    def __init__(self):
        self.item = None
        self.izquierda = None
        self.derecha = None

    def esta_vacio(self):
        return not self.item

    def crear_hoja(self,item):
        self.item = item
        self.izquierda = Bts()
        self.derecha = Bts()

    def add(self,item):
        if self.esta_vacio():
            self.crear_hoja(item)
        else:
            if item < self.item:
                self.izquierda.add(item)
            elif item > self.item:
                self.derecha.add(item)
            else:
                self.item = item

    def contiene(self,item):
        if self.esta_vacio():
            return None
        else:
            if item == self.item:
                return True
            elif item < self.item:
                self.izquierda.contiene(item)
            else:
                self.derecha.contiene(item)

    def nodes(self):
        if self.esta_vacio():
            return 0
        else:
            return 1 + self.izquierda.nodes() + self.derecha.nodes()

    def depth(self):
        if self.esta_vacio():
            return 0
        else:
            return 1 + max(self.izquierda.depth(),self.derecha.depth())

    def to_list(self):
        if self.esta_vacio():
            return []
        else:
            return self.izquierda.to_list() + [self.item] + self.derecha.to_listo()

    def print_preorder(self):
        if not self.esta_vacio():
            print(self.item)
            self.izquierda.print_preorder()
            self.derecha.print_preorder()

    def print_inorder(self):
        if not self.esta_vacio():
            self.izquierda.print_inorder()
            print(self.item)
            self.derecha.print_inorder()

    def print_postorder(self):
        if not self.esta_vacio():
            self.izquierda.print_postorder()
            self.derecha.print_postorder()
            print(self.item)

    def remover_alt(self,item):
        if not self.esta_vacio():
            if item == self.item:
                items = self.izquierda.to_list() + self.derecha.to_list()
                if items:
                    self.item = items.pop()
                else:
                    self.item = None
                self.izquierda = Bts()
                self.derecha = Bts()
                if items:
                    for item in items:
                        self.add(item)
                return True
            else:
                if item < self.item:
                    self.izquierda.remover_alt(item)
                else:
                    self.derecha.remover_alt(item)
        return False

bst = Bts()
bst.add(7)
bst.add(3)
bst.add(5)
bst.add(10)
print("Preorder:")
bst.print_preorder()
print()
print("Inorder:")
bst.print_inorder()
print()
print("Posorder:")
bst.print_postorder()

bst.remover_alt(10)
print('Nuevo indorder, 10 eliminado')
bst.print_inorder()'''

'Intento 7'
''''class Bst:
    def __init__(self):
        self.item = None
        self.izquierda = None
        self.derecha = None

    def esta_vacio(self):
        return not self.item

    def crear_hoja(self,item):
        self.item = item
        self.izquierda = Bst()
        self.derecha = Bst()

    def add(self,item):
        if self.esta_vacio():
            self.crear_hoja(item)
        else:
            if item < self.item:
                self.izquierda.add(item)
            elif item > self.item:
                self.derecha.add(item)
            else:
                self.item = item

    def nodes(self):
        if self.esta_vacio():
            return 0
        else:
            return 1 + self.izquierda.nodes() + self.derecha.nodes()

    def depth(self):
        if self.esta_vacio():
            return 0
        else:
            return 1 + max(self.izquierda.depth(),self.derecha.depth())

    def to_list(self):
        if self.esta_vacio():
            return []
        else:
            return self.izquierda.to_list() + [self.item] + self.derecha.to_list()

    def contiene(self,item):
        if self.esta_vacio():
            return False
        else:
            if item == self.item:
                return True
            elif item < self.item:
                return self.izquierda.contiene(item)
            else:
                return self.derecha.contiene(item)


    def print_preorder(self):
        if not self.esta_vacio():
            print(self.item)
            self.izquierda.print_preorder()
            self.derecha.print_preorder()

    def print_inorder(self):
        if not self.esta_vacio():
            self.izquierda.print_inorder()
            print(self.item)
            self.derecha.print_inorder()

    def print_postorder(self):
        if not self.esta_vacio():
            self.izquierda.print_postorder()
            self.derecha.print_postorder()
            print(self.item)

    def remove_alt(self,item):
        if self.esta_vacio():
            return "Arbol vacio"
        else:
            if item == self.item:
                items = self.izquierda.to_list() + self.derecha.to_list()
                if items:
                    self.item = items.pop()
                else:
                    self.item = None
                self.izquierda = Bst()
                self.derecha = Bst()
                if items:
                    for item in items:
                        self.add(item)
                return True
            else:
                if item < self.item:
                    self.izquierda.remove_alt(item)
                else:
                    self.derecha.remove_alt(item)
        return False





bst = Bst()
bst.add(7)
bst.add(3)
bst.add(5)
bst.add(10)
print("Preorder:")
bst.print_preorder()
print()
print("Inorder:")
bst.print_inorder()
print()
print("Posorder:")
bst.print_postorder()
print()
print(f"Nodes: {bst.nodes()}")
print(f"Depth: {bst.depth()}")
print(f"Contains 7? {bst.contiene(7)}")
print(f"Contains 5? {bst.contiene(5)}")
print(f"Contains 10? {bst.contiene(10)}")
print(f"Contains 3? {bst.contiene(3)}")
print(f"Contains 4? {bst.contiene(4)}")
print(f"To list: {bst.to_list()}")
print("Remove 3:")
bst.remove_alt(3)
bst.print_inorder()
print()
print("Remove 7:")
bst.remove_alt(7)
bst.print_inorder()
print()
print("Remove 10:")
bst.remove_alt(10)
bst.print_inorder()
print()
print("Remove 5:")
bst.remove_alt(5)
bst.print_inorder()
print()
bst.add(1)
bst.add(2)
bst.add(3)
bst.add(4)
bst.add(5)
bst.print_inorder()
print('Quito el 1')
bst.remove_alt(1)
bst.print_inorder()'''

'Intento 8'
'''class Bst:
    def __init__(self):
        self.item = None
        self.izquierda = None
        self.derecha = None

    def esta_vacio(self):
        return not self.item

    def crear_hoja(self,item):
        self.item = item
        self.izquierda = Bst()
        self.derecha = Bst()

    def add(self,item):
        if self.esta_vacio():
            self.crear_hoja(item)
        else:
            if item < self.item:
                self.izquierda.add(item)
            elif item > self.item:
                self.derecha.add(item)
            else:
                self.item = item

    def contiene(self,item):
        if self.esta_vacio():
            return False
        else:
            if item == self.item:
                return True
            elif item < self.item:
                return self.izquierda.contiene(item)
            else:
                return self.derecha.contiene(item)

    def nodes(self):
        if self.esta_vacio():
            return 0
        else:
            return 1 + self.izquierda.nodes() + self.derecha.nodes()

    def depth(self):
        if self.esta_vacio():
            return 0
        else:
            return 1 + max(self.izquierda.depth(),self.derecha.depth())

    def to_list(self):
        if self.esta_vacio():
            return []
        else:
            return self.izquierda.to_list() + [self.item] + self.derecha.to_list()

    def print_preorder(self):
        if not self.esta_vacio():
            print(self.item)
            self.izquierda.print_preorder()
            self.derecha.print_preorder()

    def print_inorder(self):
        if not self.esta_vacio():
            self.izquierda.print_inorder()
            print(self.item)
            self.derecha.print_inorder()

    def print_postorder(self):
        if not self.esta_vacio():
            self.izquierda.print_postorder()
            self.derecha.print_postorder()
            print(self.item)

    def remove_alt(self,item):
        if not self.esta_vacio():
            if item == self.item:
                items = self.izquierda.to_list() + self.derecha.to_list()
                if items:
                    self.item = items.pop()
                else:
                    self.item = None
                self.izquierda = Bst()
                self.derecha = Bst()
                if items:
                    for item in items:
                        self.add(item)
                return True
            else:
                if item < self.item:
                    self.izquierda.remove_alt(item)
                else:
                    self.derecha.remove_alt(item)
        return False

'Ejecucion'
bst = Bst()
bst.add(7)
bst.add(3)
bst.add(5)
bst.add(10)
print("Preorder:")
bst.print_preorder()
print()
print("Inorder:")
bst.print_inorder()
print()
print("Posorder:")
bst.print_postorder()
print()
print(f"Nodes: {bst.nodes()}")
print(f"Depth: {bst.depth()}")
print(f"Contains 7? {bst.contiene(7)}")
print(f"Contains 5? {bst.contiene(5)}")
print(f"Contains 10? {bst.contiene(10)}")
print(f"Contains 3? {bst.contiene(3)}")
print(f"Contains 4? {bst.contiene(4)}")
print(f"To list: {bst.to_list()}")
print("Remove 3:")
bst.remove_alt(3)
bst.print_inorder()
print()
print("Remove 7:")
bst.remove_alt(7)
bst.print_inorder()
print()
print("Remove 10:")
bst.remove_alt(10)
bst.print_inorder()
print()
print("Remove 5:")
bst.remove_alt(5)
bst.print_inorder()
print()
bst.add(1)
bst.add(2)
bst.add(3)
bst.add(4)
bst.add(5)
bst.print_inorder()'''

'Intento 8'
class Bst:
    def __init__(self):
        self.izquierda = None
        self.derecha = None
        self.item = None

    def esta_vacio(self):
        return not self.item

    def crear_hoja(self,item):
        self.item = item
        self.derecha = Bst()
        self.izquierda = Bst()

    def add(self,item):
        if self.esta_vacio():
            self.crear_hoja(item)
        else:
            if item < self.item:
                self.izquierda.contiene(item)
            elif item > self.item:
                self.derecha.contiene(item)
            else:
                self.item = item

    def contiene(self,item):
        if self.esta_vacio():
            return False
        else:
            if item == self.item:
                return True
            elif item < self.item:
                self.izquierda.contiene(item)
            else:
                self.derecha.contiene(item)

    def nodes(self):
        if self.esta_vacio():
            return 0
        else:
            return 1 + self.izquierda.nodes() + self.derecha.nodes()

    def depth(self):
        if self.esta_vacio():
            return 0
        else:
            return 1 + max(self.izquierda.nodes(),self.derecha.nodes())

    def print_preorder(self):
        if not self.esta_vacio():
            print(self.item)
            self.izquierda.print_preorder()
            self.derecha.print_preorder()

    def print_inorder(self):
        if not self.esta_vacio():
            self.izquierda.print_inorder()
            print(self.item)
            self.derecha.print_inorder()

    def print_posorder(self):
        if not self.esta_vacio():
            self.izquierda.print_posorder()
            self.derecha.print_posorder()
            print(self.item)

    def to_list(self):
        if self.esta_vacio():
            return []
        else:
            return self.izquierda.to_list() + [self.item] + self.derecha.to_list()

    def remove_alt(self,item):
        if not self.esta_vacio():
            if item == self.item:
                items = self.izquierda.to_list() + self.derecha.to_list()
                if items:
                    self.item = items.pop()
                else:
                    self.item = None
                self.izquierda = Bst()
                self.derecha = Bst()
                if items:
                    for item in items:
                        self.add(item)
                return True
            else:
                if item < self.item:
                    self.izquierda.remove_alt(item)
                else:
                    self.derecha.remove_alt(item)
        return False

bst = Bst()
bst.add(7)
bst.add(3)
bst.add(5)
bst.add(10)
print("Preorder:")
bst.print_preorder()
print()
print("Inorder:")
bst.print_inorder()
print()
print("Posorder:")
bst.print_posorder()
print()
print(f"Nodes: {bst.nodes()}")
print(f"Depth: {bst.depth()}")
print(f"Contains 7? {bst.contiene(7)}")
print(f"Contains 5? {bst.contiene(5)}")
print(f"Contains 10? {bst.contiene(10)}")
print(f"Contains 3? {bst.contiene(3)}")
print(f"Contains 4? {bst.contiene(4)}")
print(f"To list: {bst.to_list()}")
print("Remove 3:")
bst.remove_alt(3)
bst.print_inorder()
print()
print("Remove 7:")
bst.remove_alt(7)
bst.print_inorder()
print()
print("Remove 10:")
bst.remove_alt(10)
bst.print_inorder()
print()
print("Remove 5:")
bst.remove_alt(5)
bst.print_inorder()
print()
bst.add(1)
bst.add(2)
bst.add(3)
bst.add(4)
bst.add(5)
bst.print_inorder()
print('Quito el 1')
bst.remove_alt(1)
bst.print_inorder()