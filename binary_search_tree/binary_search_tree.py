"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
import collections #get the deque from python
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree: provided by Sean(instructor)
    def insert(self, value):
        # compare the value to the root's value to determine which direction
        # we're gonna go in 
        # if the value < root's value 
        if value < self.value:
            # go left 
            # how do we go left?
            # we have to check if there is another node on the left side
            if self.left: 
                # then self.left is a Node 
                # now what?
                self.left.insert(value)
            else:
                # then we can park the value here
                self.left = BSTNode(value)
        # else the value >= root's value 
        else:
            # go right
            # how do we go right? 
            # we have to check if there is another node on the right side 
            if self.right:
                # then self.right is a Node 
                self.right.insert(value)
            else:
                self.right = BSTNode(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # if self.value == None:
        #     return False
        if target == self.value:
            return True
        elif target < self.value:
            if self.left:
                # print('got left')
                return self.left.contains(target)
        elif target > self.value:
            if self.right:
                # print('got right')
                return self.right.contains(target)
        else:
            # print('got end')
            return False

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right:
            return self.right.get_max()
        else:
            return self.value

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        #look left deeply
        fn(self.value)
        if self.left:
            self.left.for_each(fn)
        if self.right:
            self.right.for_each(fn)
        #this is actually a left to right depth first traversal if we move the fn(self.value)

    def iner_depth_first_for_each(self, fn):
        #with depth first there's a certain order to when we visit nodes
        #turns out that what we just did is last in first out ordering, recursion does so naturally
        stack=[]
        #put root node in the stack
        stack.append(self)
        #contine traversing until stack is empty
        while len(stack)>0:
            #pop off the stack
            current_node=stack.pop()
            #add it's children to the stack
            #add right first so that it's done last
            if current_node.right:
                stack.append(current_node.right)
            #left last to make sure it's popped first
            if current_node.left:
                stack.append(current_node.left)
            #call the fn function on self.value
            fn(self.value)

    def iter_breadth_first(self, fn):
        q= collections.deque()

        q.append(self)
        while len(q)>0:
            current_node = q.popleft()
            if current_node.left:
                q.append(current_node.left)
            if current_node.right:
                q.append(current_node.right)
            fn(self.value)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node=None):
        if self.left:
            self.left.in_order_print()
        #the reason the print goes here is that it checks through the lowest deeply first. 
        #but then goes from the shallowest number to the biggest. thus why it has to be over right
        print(self.value)
        if self.right:
            self.right.in_order_print()

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        q= collections.deque()
        q.append(node)
        while len(q)>0:
            current_node = q.popleft()
            if current_node.left:
                q.append(current_node.left)
            if current_node.right:
                q.append(current_node.right)
            print(current_node.value)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        stack=[]
        stack.append(node)
        while len(stack)>0:
            current_node=stack.pop()
            if current_node.right:
                stack.append(current_node.right)
            if current_node.left:
                stack.append(current_node.left)
            print(current_node.value)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
