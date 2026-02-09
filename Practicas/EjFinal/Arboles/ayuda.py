from Pila import Stack

class BT:
    def __init__(self, item=None, left=None, right=None):
        self.item = item
        self.left = left
        self.right = right

    def is_empty(self):
        return not self.item

    def get_item(self):
        return self.item

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right

    def print_preorder(self):
        if not self.is_empty():
            print(self.item)
            if self.left:
                self.left.print_preorder()
            if self.right:
                self.right.print_preorder()

    def print_inorder(self):
        if not self.is_empty():
            if self.left:
                self.left.print_inorder()
            print(self.item)
            if self.right:
                self.right.print_inorder()

    def print_posorder(self):
        if not self.is_empty():
            if self.left:
                self.left.print_posorder()
            if self.right:
                self.right.print_posorder()
            print(self.item)

    def posorder(self):
        if self.is_empty():
            return []
        else:
            return ((self.left.posorder() if self.left else []) +
                    (self.right.posorder() if self.right else []) +
                    [self.item])



# 1A
izq1 = BT(7)
der1 = BT(3)
operador1 = BT("+",izq1,der1)

izq2 = BT(5)
der2 = BT(2)
operador2 = BT("-",izq2,der2)

bt = BT("*",operador1,operador2)

print('1B')
bt.print_posorder()
print(bt.posorder())