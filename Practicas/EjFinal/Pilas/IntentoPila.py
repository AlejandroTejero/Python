'''class Node:
    def __init__(self,item,next=None):
        self.item = item
        self.next = next

    def get_next(self ):
        return self.next

    def get_item(self ):
        return self.item

    def __str__(self):
        return str(self.item)

class Stack:
    def __init__(self):
        self.top = None

    def esta_vacio(self):
        return not self.top

    def push(self,item):
        self.top = Node(item,self.top)

    def pop(self):
        if self.esta_vacio():
            return None
        else:
            item = self.top.get_item()
            self.top = self.top.get_next()
            return item

    def peek(self):
        if self.esta_vacio():
            return None
        else:
            return self.top.get_item()

    def __str__(self):
        if not self.esta_vacio():
            s = ""
            paux = self.top
            while paux:
                s += str(paux.get_item())
                if paux.get_next():
                    s += "\n"
                paux = paux.get_next()
            return s


s = Stack()
s.push(3)
s.push(5)
s.push(8)


print(s)
print(f"La cima es: {s.peek()}")'''


'Intento'
'''class Node:
    def __init__(self,item,next=None):
        self.item = item
        self.next = next

    def get_next(self,):
        return self.next

    def get_item(self,):
        return self.item

    def __str__(self):
        return str(self.item)

class Stack:
    def __init__(self):
        self.top = None

    def esta_vacio(self):
        return not self.top

    def push(self,item):
        elemento = Node(item,self.top)
        self.top = elemento

    def pop(self):
        if self.esta_vacio():
            return None
        else:
            item = self.top.get_item()
            self.top = self.top.get_next()
            return item

    def peek(self):
        if self.esta_vacio():
            return None
        return self.top.get_item()

    def __str__(self):
        if self.esta_vacio():
            return f"Pila vacia"
        else:
            s = ""
            paux = self.top
            while paux:
                s += str(paux.get_item())
                if paux.get_next():
                    s += "\n"
                paux = paux.get_next()
            return s

s = Stack()
s.push(3)
s.push(5)
s.push(8)


print(s)
print(f"La cima es: {s.peek()}")'''

'Intento'
'''class Node:
    def __init__(self,item,next=None):
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

    def esta_vacio(self):
        return not self.top
        #return self.top is none

    def push(self,item):
        elemento = Node(item,self.top)
        self.top = elemento

    def pop(self):
        if self.esta_vacio():
            return None
        else:
            item = self.top.get_item()
            self.top = self.top.get_next()
            return item

    def peek(self):
        if self.esta_vacio():
            return None
        else:
            return self.top.get_item()

    def __str__(self):
        if self.esta_vacio():
            return f" Pila vacia "
        else:
            s = ""
            paux = self.top
            while paux:
                s += str(paux.get_item())
                if paux.get_next():
                    s += "\n"
                paux = paux.get_next()
            return s


s = Stack()
s.push(3)
s.push(5)
s.push(8)


print(s)
print(f"La cima es: {s.peek()}")'''

'Intento'
'''class Node:
    def __init__(self,item,next=None):
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

    def esta_vacio(self):
        return self.top is None

    def push(self,item):
        self.top = Node(item,self.top)

    def pop(self):
        if self.esta_vacio():
            return None
        else:
            item = self.top.get_item()
            self.top = self.top.get_next()
            return item

    def peek(self):
        if self.esta_vacio():
            return None
        else:
            return self.top.get_item()

    def __str__(self):
        if not self.esta_vacio():
            s = ""
            paux = self.top
            while paux:
                s += str(paux.get_item())
                if paux.get_next():
                    s += "\n"
                paux = paux.get_next()
            return s


s = Stack()
s.push(3)
s.push(5)
s.push(8)


print(s)
print(f"La cima es: {s.peek()}")'''

'Intento'
'''class Node:
    def __init__(self,item,next=None):
        self.item = item
        self.next = next

    def get_next(self):
        return self.next

    def get_item(self):
        return self.item

    def __str__(self):
        return str(self.item)

class Stack:
    def __init__(self):
        self.top = None

    def esta_vacio(self):
        return not self.top

    def push(self,item):
        elemento = Node(item,self.top)
        self.top = elemento

    def pop(self):
        if self.esta_vacio():
            return False
        else:
            item = self.top
            self.top = self.top.get_next()
            return item

    def peek(self):
        if self.esta_vacio():
            return None
        else:
            return self.top

    def __str__(self):
        if self.esta_vacio():
            return "Pila vacia"
        else:
            s = ""
            paux = self.top
            while paux:
                s += str(paux.get_item())
                if paux.get_next():
                    s += "\n"
                paux = paux.get_next()
            return s

s = Stack()
s.push(3)
s.push(5)
s.push(8)


print(s)
print(f"La cima es: {s.peek()}")'''

'Intento'
class Node:
    def __init__(self,item,next=None):
        self.item = item
        self.next = next

    def get_next(self):
        return self.next

    def get_item(self):
        return self.item

    def __str__(self):
        return str(self.item)

class Stack:
    def __init__(self):
        self.top = None

    def esta_vacio(self):
        return not self.top

    def push(self,item):
        elemento = Node(item,self.top)
        self.top = elemento

    def pop(self):
        if self.esta_vacio():
            return None
        else:
            item = self.top.get_item()
            self.top = self.top.get_next()
            return item

    def peek(self):
        if self.esta_vacio():
            return None
        else:
            return self.top.get_item()

    def __str__(self):
        s = ""
        paux = self.top
        while paux:
            s += str(paux.get_item())
            if paux.get_next():
                s += "\n"
            paux = paux.get_next()
        return s

s = Stack()
s.push(3)
s.push(5)
s.push(8)


print(s)
print(f"La cima es: {s.peek()}")




