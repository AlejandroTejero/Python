class Node:
    def __init__(self,item,next=None):
        self.item = item
        self.next = next

    def get_item(self):
        return self.item

    def get_next(self):
        return self.next

    def __str__(self):
        return str(self.item)
