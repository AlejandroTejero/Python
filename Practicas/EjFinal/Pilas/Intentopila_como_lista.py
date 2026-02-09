'''class Stack:
    def __init__(self):
        self.items = []

    def esta_vacio(self):
        return len(self.items) == 0

    def add(self,item):
        self.items.append(item)

    def pop(self):
        if self.esta_vacio():
            return None
        else:
            self.items.pop()

    def peek(self):
        return self.items[-1]

    def __str__(self):
        if self.esta_vacio():
            return "Pila vacia"
        else:
            s = ""
            for item in self.items:
                s += str(item) + "\n"
            return s

q = Stack()
q.add(1)
q.add(2)
q.add(3)
print("Queue")
print(q)
print(f"Peek: {q.peek()}")
print(f"Dequeue: {q.pop()}")
print(f"Queue: {q}")
print(f"Dequeue: {q.pop()}")
print(f"Queue: {q}")
print(f"Dequeue: {q.pop()}")
print(f"Queue: {q}")
q.add(1)
q.add(2)
q.add(3)'''

class Stack:
    def __init__(self):
        self.items = []

    def esta_vacio(self):
        return len(self.items) == 0

    def push(self,item):
        self.items.append(item)

    def pop(self):
        if not self.esta_vacio():
            return None
        else:
            self.items.pop()

    def peek(self):
        if not self.esta_vacio():
            return None
        else:
            return self.items[-1]

    def __str__(self):
        if self.esta_vacio():
            return "Pila vacia"
        else:
            s = ""
            for item in self.items:
                s += str(item) + "\n"
            return s


q = Stack()
q.push(1)
q.push(2)
q.push(3)
print("Queue")
print(q)
print(f"Peek: {q.peek()}")
print(f"Dequeue: {q.pop()}")
print(f"Queue: {q}")
print(f"Dequeue: {q.pop()}")
print(f"Queue: {q}")
print(f"Dequeue: {q.pop()}")
print(f"Queue: {q}")
q.push(1)
q.push(2)
q.push(3)