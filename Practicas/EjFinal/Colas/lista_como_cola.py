class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            return None
        return self.items.pop(0)

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if self.is_empty():
            return None
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
q.enqueue(3)
while not q.is_empty():
    print(f"Dequeue: {q.dequeue()}")
