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


class LinkedList:
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def add_first(self, item):
        new_node = Node(item, self.first)
        if self.is_empty():
            self.last = new_node
        self.first = new_node
        self.size += 1

    def add_last(self, item):
        if self.is_empty():
            self.add_first(item)
        else:
            new_node = Node(item)
            self.last.set_next(new_node)
            self.last = new_node
            self.size += 1

    def get_first(self):
        if self.is_empty():
            raise Exception("List is empty")
        return self.first.get_item()

    def get_last(self):
        if self.is_empty():
            raise Exception("List is empty")
        return self.last.get_item()

    def remove_first(self):
        if self.is_empty():
            raise Exception("List is empty")
        item = self.first.get_item()
        self.first = self.first.get_next()
        if not self.first:
            self.last = None
        self.size -= 1
        return item

    def remove_last(self):
        if self.is_empty():
            raise Exception("List is empty")
        item = self.last.get_item()
        previous = None
        current = self.first
        while current.get_next():
            previous = current
            current = current.get_next()
        self.last = previous
        if not self.last:
            self.first = None
        self.size -= 1
        return item

    def remove_item(self, item):
        previous = None
        current = self.first
        while current and current.get_item() != item:
            previous = current
            current = current.get_next()
        if current:
            if current == self.first:
                self.first = self.first.get_next()
                if not self.first:
                    self.last = None
            else:
                previous.set_next(current.get_next())
                if not current.get_next():
                    self.last = previous
            self.size -= 1

    def __iter__(self):
        self.current = self.first
        while self.current:
            yield self.current.get_item()
            self.current = self.current.get_next()

    def __str__(self):
        result = "["
        current = self.first
        while current:
            result += str(current)
            current = current.get_next()
            if current:
                result += ", "
        result += "]"
        return result


ll = LinkedList()
print(f"Size: {len(ll)}")
ll.add_first(1)
ll.add_last(2)
ll.add_last(3)
print(f"List: {ll}")
print(f"Size: {len(ll)}")
print(f"First: {ll.get_first()}")
print(f"Last: {ll.get_last()}")
for index, item in enumerate(ll):
    print(f"{index}: {item}")
#ll.remove_item(2)
ll.remove_first()
ll.remove_last()
print(f"List: {ll}")
