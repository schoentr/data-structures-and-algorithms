from stacks_and_queues.stacks_and_queues import Queue

class BinaryTree():
    def __init__(self):
        self.root = None
    def traverse_in_order(self):
            
            def _traverse(node):
                if not node:
                    return
                yield from _traverse(node.child_left)
                yield node.value
                yield from _traverse(node.child_right)

            return _traverse(self.root)

    # def traverse_pre_order(self):
            
    #         def _traverse(node):
    #             if not node:
    #                 return
    #             yield from _traverse(node.left)
    #             yield node.value
    #             yield from _traverse(node.right)

    #         return _traverse(self.root)
    # def traverse_post_order(self):
            
    #         def _traverse(node):
    #             if not node:
    #                 return
    #             yield from _traverse(node.left)
    #             yield node.value
    #             yield from _traverse(node.right)

    #         return _traverse(self.root)
    # def traverse_in_order(self):
            
    #         def _traverse(node):
    #             if not node:
    #                 return
    #             yield from _traverse(node.left)
    #             yield node.value
    #             yield from _traverse(node.right)

    #         return _traverse(self.root)

    def breath_first(self):
        rtn = []
        queue = Queue()
        curr = self.root
        queue.enqueue(curr)
        # import pdb; pdb.set_trace()
        while queue.is_empty():
            curr = queue.dequeue()
            if curr.child_left:
                queue.enqueue(curr.child_left)
            if curr.child_right:
                queue.enqueue(curr.child_right)
            rtn.append(curr.value)
        return rtn
    
    def find_max_value(self):
        max_value = self.root.value
        curr=self.root
        queue=Queue()
        queue.enqueue(curr)
        # import pdb; pdb.set_trace()
        while queue.is_empty():
            curr = queue.dequeue()
            if curr.value > max_value:
                max_value=curr.value
            if curr.child_left:
                queue.enqueue(curr.child_left)
            if curr.child_right:
                queue.enqueue(curr.child_right)
        return max_value 
    
    
    def find_height(self):
        height_counter = 0
        marker= None
        curr = self.root
        queue = Queue()
        queue.enqueue(curr)
        check_queue = Queue()
        while queue.is_empty():
            curr=queue.dequeue()
            if curr.child_left:
                queue.enqueue(curr.child_left)
            if curr.child_right:
                queue.enqueue(curr.child_right)
            if marker is curr.value:
                marker= None
            if marker is None:
                if curr.child_left or curr.child_right:
                    if curr.child_left:
                        height_counter +=1  
                        marker = curr.child_left.value
                    if curr.child_right:
                        marker = curr.child_right.value
                        height_counter +=1
        return height_counter
            
                


    
    def fizzbuzz (self, node = None):

        """
        This Method traverses across the tree in Order.
         Replacing the value if divisable by 3 to Fizz,  if divisibale by 5  to buzz and if divisiable by both 3 and 5 to fizzbuzz 
        """
        rtn = []
        val = []
        if not self.root:
            return None
        if node is None:
            node=  self.root
        if node.child_left:
            rtn += self.fizzbuzz(node.child_left)
        if type(node.value) is int:
            print(type(node.value))
            if (node.value) % 3 == 0 and node.value % 5 == 0 :
                node.value = 'fizzbuzz'
            elif (node.value) % 3 == 0:
                node.value = 'fizz'
            elif (node.value) % 5 == 0:
                node.value = 'buzz'
            # else:
            #     node.value = str(node.value)

        rtn.append(node.value)
        if node.child_right:
            rtn += self.fizzbuzz(node.child_right)
        
        return rtn


    def in_order(self, node = None):

        """
        This Method traverses across the tree in Order.
         LEFT -> RIGHT -> ROOT   
        """
        rtn = []
        if node is None:
            node=  self.root
        if node.child_left:
            rtn +=self.in_order(node.child_left)
        rtn.append(node.value)
        if node.child_right:
            rtn += self.in_order(node.child_right)
        return rtn

    def post_order(self, node = None):
        """
        This Method traverses across the tree post-order.
        
        """
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
        """
        This Method traverses across the tree pre-order.
         Root -> Left -> Right
        """
        rtn = []
        if node is None:
            node=  self.root
        rtn.append(node.value)
        if node.child_left:
            rtn += self.in_order(node.child_left)
        if node.child_right:
            rtn += self.in_order(node.child_right)
        return rtn

class BinarySearchTree(BinaryTree):
    # def __init__(self):
        # self.root = None
    
    def add(self, value):
        """ 
        This take in a value and creates a Node with the value and passes to the add_node method]
        
        Arguments:
            value  -- [any data type]
        """

        node=Node(value)
        self._add_node(self.root, node)

    def _add_node(self, curr, node):
        """
        This is a private method used to add nodes to the tree
        
        Arguments:
            curr {node} -- [the current node being evaluated]
            node {node} -- [the node being added to the tree]
        """

        if not self.root:
            self.root = node
        if not curr:
            curr = self.root
        if curr.value > node.value:
            if curr.child_left is None:
                curr.child_left = node
            else:
                self._add_node(curr.child_left,node)
        if curr.value < node.value:
            if curr.child_right is None:
                curr.child_right = node
            else:
                self._add_node(curr.child_right,node)
    
    def contains(self,value, curr=None):
        """ 
        Arguments:
            value {} -- [any data type  which will be stored in the node]
        
        Keyword Arguments:
            curr {node} -- [the current node that is being evaluated]
        
        Returns:
            [Boolean] -- [True if value is in the tree, False if not in the tree]
        """

        if curr is None:
            curr = self.root
        if value is curr.value:
            return True
        if value > curr.value and curr.child_right :
                return self.contains(value, curr.child_right)
        elif curr.child_left:
                return self.contains(value, curr.child_left)
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
    
    def __repr__(self):
        return 'Tree Node - '+ (str(self.value))
    
    def __str__(self):
        return 'Tree Node - '+ (str(self.value))
