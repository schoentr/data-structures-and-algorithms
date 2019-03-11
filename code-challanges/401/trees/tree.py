class BinaryTree():
    def __init__(self):
        self.root = None

    def in_order(self, node = None):

        """This Method traverses across the tree in Order.
        """
        rtn = []
        if node is None:
            node=  self.root
        if node.child_left:
            rtn += self.in_order(node.child_left)
        rtn.append(node.value)
        if node.child_right:
            rtn += self.in_order(node.child_right)
        return rtn

    def post_order(self, node = None):
        rtn = []
        if node is None:
            node= self.root
        if node.child_left:
            rtn += self.in_order(node.child_left)
        if node.child_right:
            rtn += self.in_order(node.child_right)
        rtn.append(node.value)
        return rtn

    def pre_order(self, node = None):
        rtn = []
        if node is None:
            node=  self.root
        rtn.append(node.value)
        if node.child_left:
            rtn += self.in_order(node.child_left)
        if node.child_right:
            rtn += self.in_order(node.child_right)
        return rtn





def printInorder(root): 
  
    if root: 
  
        # First recur on left child 
        printInorder(root.left) 
  
        # then print the data of node 
        print(root.val), 
  
        # now recur on right child 
        printInorder(root.right) 
  
    def post_order(self):
        """This method traverses across the tree post Order.
        """
        pass
    def pre_order(curr=None, rtn=''):
        """This method traverses across the tree pre Order.
        "ROOT" -->left -->right
        """
        if curr is None:
            curr = self.root
        rtn += curr.value
        pre_order(curr.child_left)
        pre_order(curr.child_right)
        

class BinarySearchTree(BinaryTree):
    def __init__(self):
        self.root = None
    
    def add(self, value):
        node=Node(value)
        self.add_node(self.root, node)

    def add_node(self, curr, node):
        if not self.root:
            self.root = node
        if not curr:
            curr = self.root
        if curr.value > node.value:
            if curr.child_left is None:
                curr.child_left = node
            else:
                self.add_node(curr.child_left,node)
        if curr.value < node.value:
            if curr.child_right is None:
                curr.child_right = node
            else:
                self.add_node(curr.child_right,node)
    
    def contains(self,value, curr=None):
        if curr is None:
            curr = self.root
        print(curr.value, value)
        if value is curr.value:
            return True
        elif value > curr.value:
            if curr.child_right :
                return self.contains(value, curr.child_right)
            else:
                return False
        elif value < curr.value:
            if curr.child_left:
                return self.contains(value, curr.child_left)
            else:
                return False

        



        
class Node():

    def __init__(self, value):
        """Creates all nodes for the tree
        
        Arguments:
            value  -- [Any value you want to be held in the node]
        """
        self.value = value
        self.child_left = None
        self.child_right = None
