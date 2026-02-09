class Node:
    def __init__(self, item, next=None):
        self.item = item
        self.next = next

    def get_item(self):
        return self.item

    def get_next(self):
        return self.next

    def set_next(self, next):
        self.next = next

    def __str__(self):
        return str(self.item)


class Queue:
    def __init__(self):
        self.first = None
        self.last = None

    def enqueue(self, item):
        n = Node(item)
        if self.is_empty():
            self.first = n
        else:
            self.last.set_next(n)
        self.last = n

    def dequeue(self):
        if self.is_empty():
            return None
        item = self.first.get_item()
        self.first = self.first.get_next()
        if not self.first:
            self.last = None
        return item

    def is_empty(self):
        return not self.first and not self.last

    def peek(self):
        if self.is_empty():
            return None
        return self.first.get_item()

    def __str__(self):
        s = "["
        paux = self.first
        while paux:
            s += str(paux.get_item())
            paux = paux.get_next()
            if paux:
                s += ", "
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
    print(f"Dequeue: {q.dequeue()}")
