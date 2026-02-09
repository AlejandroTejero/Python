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

    def esta_vacia(self):
        return not self.top

    def anadir(self,item):
        self.top = Node(item,self.top)

    def desapilar(self):
        if self.esta_vacia():
            return None
        else:
            item = self.top.get_item()
            self.top = self.top.get_next()
            return item

    def peek(self):
        if self.esta_vacia():
            return None
        return self.top.get_item()

'''class Node:
    def __init__(self,item, next=None):
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
        
    def esta_vacia(self):
        return not self.top

    def anadir(self, item):
        self.top = Node(item, self.top)
        
    def sacar(self):
        if self.esta_vacia():
            return None
        else:
            item = self.top.get_item()
            self.top = self.top.get_next()
            return item
        
    def consultar(self):
        if self.esta_vacia():
            return None
        return self.top.get_item()'''

