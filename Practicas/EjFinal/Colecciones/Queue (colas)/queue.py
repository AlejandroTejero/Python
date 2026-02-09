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

    def esta_vacia(self):
        return not self.first and not self.last

    #Ver si hay primero y ver si hay ultimo
    #Si solo hay 1 elementro, primero = ultimo = unico

    def enqueue(self,item):
        elemento = Node(item)
        if self.esta_vacia():
            self.first = elemento
        else:
            self.last.set_next(elemento)
        self.last = elemento

    # Igualas el 'numero intern' al elemento, si esta vacia el elemento entero es lo primero.
    # Si no esta vacía el siguente al 'antiguo ultimo' es el nuevo ultimo
    # Ultimo = Elemento

    def dequeue(self):
        if self.esta_vacia():
            return None
        item = self.first.get_item()
        self.first = self.first.get_next()
        if not self.first:
            self.last = None
        return item

    # Si la cola esta vacia no puede sacar nada de ella, metes un numero y le asignas la primera posicion
    # Asignas el primero a siguente que teneias delante (si eliminas el 1, el 2 pasa a ser el 1)
    # Si no hay siguente y has elimiando el 1, el siguente = None

    def peek(self):
        if self.esta_vacia():
            return None
        return self.first.get_item()

    # Accede a la ultima/primera posicion de la cola

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
q.enqueue(4)
q.enqueue(7)

#q.dequeue()
print(q)
print(f"La cima es : {q.peek()}")
