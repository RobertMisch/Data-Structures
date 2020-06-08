import singly_linked_list
"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""
# class Stack:
#     def __init__(self):
#         self.size = 0
#         self.storage = []

#     def __len__(self):
#         self.size = len(self.storage)
#         return self.size

#     def push(self, value):
#         # if(self.storage == None):
#         #     self.storage=[]
#         self.storage.append(value)
#         self.size = len(self.storage)
#         return self.storage

#     def pop(self):
#         data=None
#         if(len(self.storage)>=1):
#             data = self.storage.pop()
#         self.size = len(self.storage)
#         return data

#here if we need to impliment a linked list ourselves withing the stack class
# class Node:
#     def __init__(self, value, next=None):
#         self.value = value
#         self.next_node = next
# ​
#     def get_value(self):
#         # returns the node's data 
#         return self.value
# ​
#     def get_next(self):
#         # returns the thing pointed at by this node's `next` reference 
#         return self.next_node
# ​
#     def set_next(self, new_next):
#         # sets this node's `next` reference to `new_next`
#         self.next_node = new_next

class Stack:
    def __init__(self):
        self.size = 0
        self.storage=singly_linked_list.LinkedList()

    def __len__(self):
        return self.size

    def push(self, value):
        #here I don't have to make a new node since our list does it for me
        self.storage.add_to_tail(value)
        self.size= self.size + 1
        return self.storage.tail.value

    def pop(self):
        data = self.storage.remove_tail()
        if self.size != 0:
            self.size= self.size - 1
        # print(self.size)
        return data
            
