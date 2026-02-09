'''class Node:
    def __init__(self,item,next=None):
        self.item = item
        self.next = next

    def get_next(self ):
        return self.next

    def get_item(self ):
        return self.item

    def set_next(self,next):
        self.next = next

    def __str__(self):
        return str(self.item)

class Queue:
    def __init__(self):
        self.first = None
        self.last = None

    def esta_vacio(self):
        return not self.first and not self.last

    def enqueue(self,item):
        elemento = Node(item)
        if self.esta_vacio():
            self.first = elemento
        else:
            self.last.set_next(elemento)
        self.last = elemento

    def dequeue(self):
        if self.esta_vacio():
            return None
        else:
            item = self.first.get_item()
            self.first = self.first.get_next()
            if not self.first:
                self.last = None
            return item

    def peek(self):
        if self.esta_vacio():
            return None
        return self.first.get_item()

    def __str__(self):
        s = "["
        paux = self.first
        while paux:
            s += str(paux.get_item())
            if paux.get_next():
                s += ","
            paux = paux.get_next()
        s += "]"
        return s

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(f"Queue: {q}")
print(f"Peek: {q.peek()}")
print(f"Dequeue: {q.dequeue()}")
print(f"Queue: {q}")
print(f"Dequeue: {q.dequeue()}")
print(f"Queue: {q}")
print(f"Dequeue: {q.dequeue()}")
print(f"Queue: {q}")
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
while not q.is_empty():
    print(f"Dequeue: {q.dequeue()}")'''

'Intento'
'''class Node:
    def __init__(self,item,next=None):
        self.item = item
        self.next = next

    def get_next(self ):
        return self.next

    def get_item(self ):
        return self.item

    def set_next(self,next):
        self.next = next

    def __str__(self):
        return str(self.item)


class Queue:
    def __init__(self):
        self.first = None
        self.last = None

    def esta_vacio(self):
        return not self.first and not self.last

    def enqueue(self,item):
        elemento = Node(item)
        if self.esta_vacio():
            self.first = elemento
        else:
            self.last.set_next(elemento)
        self.last = elemento

    def dequeue(self):
        if self.esta_vacio():
            return None
        else:
            item = self.first.get_item()
            self.first = self.first.get_next()
            return item

    def peek(self):
        if self.esta_vacio():
            return None
        else:
            return self.first.get_item()

    def __str__(self):
        if self.esta_vacio():
            return f"Cola vacia"
        else:
            s = "["
            paux = self.first
            while paux:
                s += str(paux.get_item())
                if paux.get_next():
                    s += ","
            s += "]"
            return s'''

'Intento'
'''class Node:
    def __init__(self,item,next=None):
        self.item = item
        self.next = next

    def get_item(self):
        return self.item

    def get_next(self):
        return self.next

    def set_next(self,next):
        self.next = next

    def __str__(self):
        return str(self.item)

class Queue:
    def __init__(self):
        self.first = None
        self.last = None

    def esta_vacio(self):
        return not self.first and not self.last

    def enqueue(self,item):
        elemento = Node(item)
        if self.esta_vacio():
            self.first = elemento
        else:
            self.last.set_next(elemento)
        self.last = elemento

    def dequeue(self):
        if self.esta_vacio():
            return None
        else:
            item = self.first.get_item()
            self.first = self.first.get_next()
            if not self.first:
                self.last = None
            return item

    def peek(self):
        if self.esta_vacio():
            return None
        else:
            return self.first.get_item()

    def __str__(self):
        if self.esta_vacio():
            return f" Cola vacia "
        else:
            s = "["
            paux = self.first
            while paux:
                s += str(paux.get_item())
                if paux.get_next():
                    s += ","
                paux = paux.get_next()
            s += "]"
            return s

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(f"Queue: {q}")
print(f"Peek: {q.peek()}")
#print(f"Dequeue: {q.dequeue()}")
#print(f"Queue: {q}")
#print(f"Dequeue: {q.dequeue()}")
#print(f"Queue: {q}")
#print(f"Dequeue: {q.dequeue()}")
#print(f"Queue: {q}")
#q.enqueue(1)
#q.enqueue(2)
#q.enqueue(3)
while not q.esta_vacio():
    print(f"Dequeue: {q.dequeue()}")'''

'Intento'
'''class Node:
    def __init__(self,item,next=None):
        self.item = item
        self.next = next

    def get_item(self):
        return self.item

    def get_next(self):
        return self.next

    def set_next(self,next):
        self.next = next

    def __str__(self):
        return str(self.item)

class Queue:
    def __init__(self):
        self.first = None
        self.last = None

    def esta_vacio(self):
        return not self.first and not self.last

    def enqueue(self,item):
        elemento = Node(item)
        if self.esta_vacio():
            self.first = elemento
        else:
            self.last.set_next(elemento)
        self.last = elemento

    def dequeue(self):
        if self.esta_vacio():
            return None
        else:
            item = self.first.get_item()
            self.first = self.first.get_next()
            if not self.first:
                self.last = None
            return item

    def peek(self):
        if self.esta_vacio():
            return None
        else:
            return self.first.get_item()

    def __str__(self):
        if self.esta_vacio():
            return "Cola vacia"
        else:
            s = ""
            paux = self.first
            while paux:
                s += str(paux.get_item())
                if paux.get_next():
                    s += ","
                paux = paux.get_next()
            return s


q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(f"Queue: {q}")
print(f"Peek: {q.peek()}")
print(f"Dequeue: {q.dequeue()}")
print(f"Queue: {q}")
print(f"Dequeue: {q.dequeue()}")
print(f"Queue: {q}")
print(f"Dequeue: {q.dequeue()}")
print(f"Queue: {q}")
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)'''

'Intento'
'''class Node:
    def __init__(self,item,next=None):
        self.item = item
        self.next = next

    def get_item(self):
        return self.item

    def get_next(self):
        return self.next

    def set_next(self,next):
        self.next = next

    def __str__(self):
        return str(self.item)


class Queue:
    def __init__(self):
        self.last = None
        self.first = None

    def esta_vacio(self):
        return not self.first and not self.last

    def enqueue(self,item):
        elemento = Node(item)
        if self.esta_vacio():
            self.first = elemento
        else:
            self.last.set_next(elemento)
        self.last = elemento

    def dequeue(self):
        if self.esta_vacio():
            return None
        else:
            item = self.first.get_item()
            self.first = self.first.get_next()
            if not self.first:
                self.last = None
            return item

    def peek(self):
        if self.esta_vacio():
            return None
        else:
            return self.first.get_item()

    def __str__(self):
        if self.esta_vacio():
            return "Cola vacia"
        else:
            s = "["
            paux = self.first
            while paux:
                s += str(paux.get_item())
                if paux.get_next():
                    s += ","
                paux = paux.get_next()
            s += "]"
            return s


q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(f"Queue: {q}")
print(f"Peek: {q.peek()}")
print(f"Dequeue: {q.dequeue()}")
print(f"Queue: {q}")
print(f"Dequeue: {q.dequeue()}")
print(f"Queue: {q}")
print(f"Dequeue: {q.dequeue()}")
print(f"Queue: {q}")
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)'''

'Intento'

class Node:
    def __init__(self,item,next=None):
        self.item = item
        self.next = next

    def get_item(self):
        return self.item

    def get_next(self):
        return self.next

    def set_next(self,next):
        self.next = next

    def __str__(self):
        return str(self.item)

class Queue:
    def __init__(self):
        self.first = None
        self.last = None

    def esta_vacio(self):
        return not self.first and not self.last

    def enqueue(self,item):
        elemento = Node(item)
        if self.esta_vacio():
            self.first = elemento
        else:
            self.last.set_next(elemento)
        self.last = elemento

    def dequeue(self):
        if self.esta_vacio():
            return None
        else:
            item = self.first.get_item()
            self.first = self.first.get_next()
            if not self.first:
                self.last = None
            return item



    def peek(self):
        if self.esta_vacio():
            return None
        else:
            return self.first.get_item()

    def __str__(self):
        s = "["
        paux = self.first
        while paux:
            s += str(paux.get_item())
            if paux.get_next():
                s += ","
            paux = paux.get_next()
        s += "]"
        return s


q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(f"Queue: {q}")
print(f"Peek: {q.peek()}")
print(f"Dequeue: {q.dequeue()}")
print(f"Queue: {q}")
print(f"Dequeue: {q.dequeue()}")
print(f"Queue: {q}")
print(f"Dequeue: {q.dequeue()}")
print(f"Queue: {q}")
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)