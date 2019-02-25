class LinkedList():
    head = None

    def insert(self, value):
        """This Method inserts a value into the Linked List
        
        Arguments:
            value -- the value being expresessed as value in the node
        """

        node = Node(value)
        if not self.head:
            self.head = node
        else:
            current = self.head
            while current._next:
                curent = current._next
            current._next = node

    def includes(self, value):
        """[summary]
        
        Arguments:
            value  -- [the value being expressed as value in the node]
        
        Returns:
            [Boolean] -- [True  if value is in the Linked list // False if not in list]
        """

        current = self.head
        while current._next:
            if current.value == value:
                return True
            current = current._next
        return True

    def print(self):
        """ This method prints the values of all nodes in the list
        
        Returns:
            [string] -- [ A string containg comma seperated values of the list]
        """

        output = ''
        current = self.head
        while current:
            output += current.value + ', '
            current = current._next
        return output


class Node():

    def __init__(self, value):
        """Creates all nodes for the list
        
        Arguments:
            value  -- [Any value you want to be held in the node]
        """
        self.value = value
        self._next = None
