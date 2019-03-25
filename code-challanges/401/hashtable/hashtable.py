from linked_list.linked_list import LinkedList


class Hashtable():
    """
    A Hashtable data structure that uses key value pairs.
    """
    
    def __init__(self):
        """
        A hash table data structure
        """
        self._array = [None]*1026

    def add(self, key, value):
        """Adds a key value pair to the hashtable

        Arguments:
            key {string}
            value {[type]} 
        """
        index = self.hash(key)
        if self._array[index] is None:
            self._array[index] = LinkedList()
        self._array[index].insert((key, value))
        return self._array[index].head.value

    def get(self, key):
        """
        This method takes in a key and returns the value assoicated with the key in the hashtable

        Arguments:
            key {string}
        """
        index = self.hash(key)
        if not self._array[index]:
            return None
        current = self._array[index].head
        while current:
            if current.value[0] == key:
                return current.value[1]
            else:
                current = current._next
        return None

    def contains(self, key):
        """This method takes in a key and returns a boolean  if the key exists in the hashtable

        Arguments:
            key {string}
        Returns:
            Boolean --  True if key is in hashtable, False if not found
        """
        index = self.hash(key)
        if not self._array[index]:
            return False
        current = self._array[index].head
        while current:
            if current.value[0] == key:
                return True
            else:
                current = current._next
        return False

    def hash(self, key):
        """Takes in a key.  

        Arguments:
            key {string} 

        Returns:
            [integer] -- Index for the bucket for the hash table
        """
        letter_sum = 0
        for x in key:
            letter_sum += ord(x)
        multi_prime = letter_sum * 599
        safe_index = multi_prime//1026

        return safe_index
