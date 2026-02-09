class BTS:
    def __init__(self):
        self.item = None
        self.left = None
        self.right = None

    def is_empty(self):
        return not self.item  # return self.item is None

    def create_leave(self, item):
        self.item = item
        self.left = BTS()
        self.right = BTS()

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
        if self.left.is_empty():
            return self.item
        else:
            return self.left.min()

    def remove_alt(self, item):
        if not self.is_empty():
            if item == self.item:
                items = self.left.to_list() + self.right.to_list()
                if items:
                    self.item = items.pop()
                else:
                    self.item = None
                self.left = BTS()
                self.right = BTS()
                if items:
                    for item in items:
                        self.add(item)
                return True
            elif item < self.item:
                return self.left.remove_alt(item)
            else:
                return self.right.remove_alt(item)
        return False


bts = BTS()
bts.add(7)
bts.add(3)
bts.add(5)
bts.add(10)
bts.add(11)
print(f"Arbol en preorder: {bts.print_preorder()}")
print(f"Eliminamos su raiz")
bts.remove_alt(7)
print(f"Arbol en preorder: {bts.print_preorder()}")
bts.remove_alt(11)
print(f"Arbol en preorder: {bts.print_preorder()}")


'''print("Preorder:")
bts.print_preorder()
print("Inorder:")
bts.print_inorder()
print("Postorder:")
bts.print_posorder()
print()
print(f"Nodes: {bts.nodes()}")
print(f"Depth: {bts.depth()}")
print(f"Contains 7? {bts.contains(7)}")
print(f"Contains 12? {bts.contains(12)}")
bts.remove_alt(7)
bts.print_inorder()'''