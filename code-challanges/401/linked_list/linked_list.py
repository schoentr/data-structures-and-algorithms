class LinkedList():
    head = None

    def insert(self,value):
        node = Node(value)
        if not self.head:
            self.head = node
        else:
            current = self.head
            while current._next:
                curent = current._next
            current._next = node
    def includes(self,value):
        current = self.head
        while current._next:
            if current.value == value:
                return True
            current = current._next
        return True
    def print(self):
        output = ''
        current = self.head
        while current:
            output += current.value + ', '
            current = current._next
        return output
        



class Node():
    def __init__(self,value):
        self.value = value
        self._next = None
        
