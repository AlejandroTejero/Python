
class Stack:
    def __init__(self):
        self.items = []

    def esta_vacio(self):
        return len(self.items) == 0

    def __len__(self):
        return len(self.items)

    def push(self,item):
        self.items.append(item)

    def pop(self):
        if self.esta_vacio():
            return None
        else:
            return self.items.pop()

    def peek(self):
        return self.items[-1]

    def __str__(self):
        s = ""
        if not self.esta_vacio():
            for item in self.items:
                s += str(item) + "\n"
        return s



q = Stack()
q.push(1)
q.push(2)
q.push(3)
print(f"Queue:\n {q}")
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