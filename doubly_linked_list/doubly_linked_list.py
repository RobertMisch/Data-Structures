"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""
    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""
    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""
    def add_to_head(self, value):
        new_node = ListNode(value)
        if(self.length <= 0):
            self.head=new_node
            self.tail=new_node
            self.length+=1
        else:
            # self.head.insert_before(new_node)
            self.head.prev=new_node
            new_node.next=self.head
            self.head=new_node
            self.length+=1
            return self.head
            

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""
    def remove_from_head(self):
        if(not self.head):
            return None
        else:
            data=self.head.value
            if(self.head.next):
                self.head=self.head.next
                self.head.prev=None
            else:
                self.head=None
                self.tail=None
            self.length-=1
            return data

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""
    def add_to_tail(self, value):
        new_node = ListNode(value)
        if(self.length <= 0):
            self.head=new_node
            self.tail=new_node
            self.length+=1
        else:
            self.tail.next=new_node
            new_node.prev=self.tail
            self.tail=new_node
            self.length+=1
            # print(f"add to tail {self.tail.prev}")
            return self.tail

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""
    def remove_from_tail(self):
        #blank list case
        if(not self.tail):
            return None
        else:
            data=self.tail.value
            if(self.tail.prev):
                self.tail=self.tail.prev
                self.tail.next=None
            #only node case
            else:
                self.head=None
                self.tail=None
            self.length-=1
            return data

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""
    def move_to_front(self, node):
        #store the node
        data = node.value
        #remove the node
        node.delete()
        self.length-=1
        #put the node as the head
        self.add_to_head(data)

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""
    def move_to_end(self, node):
        # if(self.tail==node):
        #     return
        data = node.value
        # print(data)
        if(self.head != node):
            node.delete()
            self.length-=1
            self.add_to_tail(data)
        else:
            # print("we got ehre")
            self.remove_from_head()
            self.add_to_tail(data)
        # node.delete()
        # print(self.tail.prev)
        # print(f"in move to end {self.tail.prev}")

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""
    def delete(self, node):
        if(node == self.head):
            self.remove_from_head()
        elif(node == self.tail):
            self.remove_from_tail()
        else:
            node.delete()

    """Returns the highest value currently in the list"""
    def get_max(self):
        #start at head
        searching = True
        current_highest=0
        current_node=self.head
        while searching:
            if current_highest< current_node.value:
                current_highest=current_node.value
            if current_node.next != None:
                current_node = current_node.next
            else:
                searching=False
                return current_highest
        
