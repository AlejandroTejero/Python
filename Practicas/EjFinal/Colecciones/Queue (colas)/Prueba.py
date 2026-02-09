class Node:
    def __init__(self,item,next):
        self.item = item
        self.next = next

    def get_next(self):
        return self.next

    def get_item(self):
        return self.item
    def set_next(self,next):
        self.next = next

    def __str__(self):
        return str(self.item)

class Queue:
    def __init__(self):
        self.first = None
        self.last = None

    def esta_vacia(self):
        return not self.first and not self.last

    def enqueue(self,item):
        elemento = Node(item)
        if self.esta_vacia():
            self.first = elemento
        else:
            self.last.set_next(elemento)
        self.last = elemento

    def dequeue(self):
        if self.esta_vacia():
            return None
        item = self.first.get_item()
        self.first = self.first.get_next()
        if not self.first:
            self.last = None
        return item

    def consultar(self):
        if self.esta_vacia():
            return None
        item = self.first.get_item()
        return item
        #return self.first.get_item()

    # def __str__(self:)


