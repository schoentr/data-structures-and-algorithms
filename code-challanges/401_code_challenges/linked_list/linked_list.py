from copy import copy, deepcopy


class LinkedList():
    head = None

    def __init__(self, iterable=None):
        """This initalizes the list
        """
        self.head = None
        if iterable:
            for value in iterable:
                self.insert(value)

    def __iter__(self):
        """This makes the linked list iterable
        """
        current = self.head
        while current:
            yield current.value
            current = current._next

    def __add__(self, iterable):
        """This makes it able to add an iterable to the linked-list
        
        """

        new_list = deepcopy(self)
        for value in iterable:
            new_list.insert(value)
        return new_list

    def __iadd__(self, value):
        """This method makes it able to use "+="to add value to linked list

        Arguments:
            value  -- [data to be added to the linked list]
        """
        self.insert(value)
        return self

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
                current = current._next
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

    def find_from_end(self, value):
        length = 0
        curr = self.head
        while curr:
            length += 1
            curr = curr._next
        distance = length - value - 1
        curr = self.head
        if length > value:
            for x in range(0, distance):
                curr = curr._next
            return curr.value
        else:
            return 'exception'


class Node():

    def __init__(self, value):
        """Creates all nodes for the list

        Arguments:
            value  -- [Any value you want to be held in the node]
        """
        self.value = value
        self._next = None
