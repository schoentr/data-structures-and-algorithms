class Queue():
    front = None
    rear = None

    def enqueue(self,value):
        node = Node(value)
        if not self.front:
            self.front = node
            self.rear = node
        else:
            self.rear._next= node
            self.rear = node
               
    def dequeue(self):
        self.front = self.front._next
    def peek(self):
        return self.front.value



class Stack():
    # _list = LinkedList()
    top = None
    def push(self, value):
        node = Node(value)
        node._next = self.top
        self.top = node

    def pop (self):
        self.top = self.top._next
    def peek(self):
        return self.top.value


class Node():

    def __init__(self, value):
        """Creates all nodes for the list
        
        Arguments:
            value  -- [Any value you want to be held in the node]
        """
        self.value = value
        self._next = None