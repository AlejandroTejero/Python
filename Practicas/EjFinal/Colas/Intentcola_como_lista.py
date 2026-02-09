'''class Queue:
    def __init__(self):
        self.items = []

    def esta_vacio(self):
        return len(self.items) == 0

    def enqueue(self,item):
        self.items.append(item)

    def dequeue(self):
        if self.esta_vacio():
            return None
        else:
            self.items.pop(0)

    def peek(self):
        if self.esta_vacio():
            return None
        else:
            return self.items[0]

    def __str__(self):
        return str(self.items)


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

'Intento 1'
'''class Queue:
    def __init__(self):
        self.items = []

    def esta_vacio(self):
        return len(self.items) == 0

    def __len__(self):
        return len(self.items)

    def enqueue(self,item):
        self.items.append(item)

    def dequeue(self):
        if self.esta_vacio():
            return None
        else:
            return self.items.pop()

    def peek(self):
        return self.items[-1]

    def __str__(self):
        s = "["
        if not self.esta_vacio():
            for item in self.items:
                s += str(item) + ","
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

'Intento 2'
class Queue:
    def __init__(self):
        self.items = []

    def esta_vacio(self):
        return len(self.items) == 0

    def enqueue(self,item):
        self.items.append(item)

    def dequeue(self):
        if self.esta_vacio():
            return None
        else:
            self.items.pop(0)

    def peek(self):
        if self.esta_vacio():
            return None
        else:
            return self.items[0]

    def __str__(self):
        return str(self.items)


q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(f"Queue: {q}")
q.dequeue()
print(f"Queue: {q}")
