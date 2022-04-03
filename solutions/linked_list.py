'''
Author: Ronald Coello
Credits: Brigham Young University Idaho
ronaldcoello85@gmail.com
Implementation of a Linked List
'''

class LinkedList:

    # Class to store the data of every element in the linked list
    class Node:
        def __init__(self, data):
            self.next = None
            self.prev = None
            self.data = data

    # Create an empty linked list 
    def __init__(self):
        self.head = None
        self.tail = None

    # Insert a node at the front of the linked list
    def insert_head(self, value):
        
        # Initialize new node
        new_node = LinkedList.Node(value)

        # If this is the first element and the list, set the head and tail to be the new new_node
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        
        # If the list is not empty, change the head to be the new node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insert_tail(self, value):

        # Initialize new node
        new_node = LinkedList.Node(value)

        # If this is the first element and the list, set the head and tail to be the new new_node
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        
        # If the list is not empty, change the tail to be the new node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node        

    def remove_head(self):

        # If there is only one element in the list, set the head and tail to none
        if self.head == self.tail:
            self.head = None
            self.tail = None
        
        # If there is more than one item, set the head to be the next element
        else:
            self.head.next.prev = None
            self.head = self.head.next
    
    def remove_tail(self):

        # If there is only one element in the list, set the head and tail to none
        if self.tail == self.head:
            self.tail = None
            self.head = None
        
        # If there is more than one item, set the tail to be the previous element
        else:
            self.tail.prev.next = None
            self.tail = self.tail.prev
    
    def remove_node(self, value):

        curr = self.head

        while curr is not None:
            if curr.data == value:

                # If head is the value we want to remove, call remove_head()
                if curr == self.head:
                    self.remove_head()

                # If tail is the value we want to remove, call remove_tail()
                elif curr == self.tail:
                    self.remove_tail
                
                # If the value we want to remove is anywhere else
                else:
                    curr.prev.next = curr.next
                    curr.next.prev = curr.prev
                return
            curr = curr.next



    def insert_next(self, value, new_value):

        # Where to start
        curr = self.head

        # Look for the node that matches value and replace it with the new vaule
        while curr is not None:

            if curr.data == value:
                
                # Check value is at the end of the list.
                if curr == self.tail:
                    self.insert_tail(new_value)
                
                # If value is located anywhere else insert it after value
                else:
                    new_node = LinkedList.Node(new_value)
                    new_node.prev = curr
                    new_node.next = curr.next
                    curr.next.prev = new_node
                    curr.next = new_node
                return
            curr = curr.next
    
    # Iterate foward through the Linked List
    def __iter__(self):
        curr = self.head  # Start at the begining since this is a forward iteration.
        while curr is not None:
            yield curr.data  # Provide (yield) each item to the user
            curr = curr.next # Go forward in the linked list

    # Return a string representation of the linked list.
    def __str__(self):
        output = "linkedlist["
        first = True
        for value in self:
            if first:
                first = False
            else:
                output += ", "
            output += str(value)
        output += "]"
        return output

                
            

