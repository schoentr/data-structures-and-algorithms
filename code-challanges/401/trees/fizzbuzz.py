from tree import BinaryTree


def fizzbuzz (self, node = None):

        """
        This Method traverses across the tree in Order.
         Replacing the value if divisable by 3 to Fizz,  if divisibale by 5  to buzz and if divisiable by both 3 and 5 to fizzbuzz 
        """
        rtn = []
        if node is None:
            node=  self.root
        if node.child_left:
            rtn += self.fizzbuzz(node.child_left)
        if (int(node.value) % 3 == 0) and (node.value % 5 == 0) :
            node.value = 'fizzbuzz'
        elif int(node.value) % 3 is 0:
            node.value = 'fizz'
        elif int(node.value) % 5 is 0:
            node.value = 'buzz'
        rtn.append(node.value)
        if node.child_right:
            rtn += self.fizzbuzz(node.child_right)
        
        return rtn
