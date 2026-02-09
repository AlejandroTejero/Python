class Node:
    def __init__(self, item, next=None):
        self.item = item
        self.next = next

    def get_item(self):
        return self.item

    def get_next(self):
        return self.next

    def __str__(self):
        return str(self.item)


class Stack:
    def __init__(self):
        self.top = None

    def esta_vacia(self):
        return not self.top

    def push(self,item):
        self.top = Node(item,self.top)

    # Añades el item a la pila vacia, entonces es el top.
    # El next = self.top = None, pq no hay nada mas por encima.

    def pop(self):
        if self.esta_vacia():
            return None
        else:
            item = self.top.get_item()
            self.top = self.top.get_next()
            return item

    # Si esta vacia no elimina nada
    # Si hay items, escoge que item = item, top = siguiente. (None)

    def peek(self):
        if self.esta_vacia():
            return None
        return self.top.get_item()

    # Consultar el top

    def __str__(self):
        if self.esta_vacia():
            return "Pila vacia"
        s = ""
        paux = self.top
        while paux:  # while paux is not None:
            s += str(paux.get_item()) + "\n"
            paux = paux.get_next()
        return s

s = Stack()
s.push(7)
s.push(9)
s.push(-1)
print(s)
print(s.peek())
print(s.pop())
while not s.esta_vacia():
    print(s.pop())

