import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        #we only have to care about the location of the head and the tail
        # self.storage = ?
        #this should also refer to the instantiated class

        self.storage = DoublyLinkedList() #instantiate the class

    def push(self, value):
        #because stacks are first in last out, we want to add the new elements to the tail (because it is easier to remove something from this)
        self.storage.add_to_tail(value)
        self.size = self.storage.length
        

    def pop(self):
        #because stacks are first in last out, we want to remove elements from where we added them
        if self.storage.tail is None:
            removed_from_stack = None
        else:
            removed_from_stack = self.storage.tail.value
            self.storage.remove_from_tail()

        self.size = self.storage.length
        return removed_from_stack

    def len(self):
        #this should work the same way as the queue
        self.size = self.storage.length
        return self.size
