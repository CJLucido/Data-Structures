import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


class Queue:
    def __init__(self):
        # should increase when we enqueue and decrease if we dequeue OR should always just match the dll length
        self.size = 0 
        # Why is our DLL a good choice to store our elements?
        # Because we don't have to worry about whether we have another spot in memory at the tail end (and then pop the previous head) or shift everything over an index if we delete from the head to add to the tail.
        # This reduces our runtime complexity from O(n) in the latter case to O(1).

        # self.storage = ?
        # SCRATCH THIS we need somewhere to store all the node values, and then with the values we can change the head and the tail using the doubly_linked_list class
        # we don't need to store all the node values here because if we have the head we can get to the whole list, we only care about changing the head and tail, nothing in the middle

        self.storage = DoublyLinkedList() #should be the whole class because the class will have both a head and a tail on it

    def enqueue(self, value):
        #replace the head with the new value
        self.storage.add_to_head(value)
        # then we update our size here to match the new dll length given by this addition
        self.size = self.storage.length
        # print(self.storage.tail.value)
        

    def dequeue(self):
        #remove the tail and replace it with the previous value
        if self.storage.tail is None:
            removed_from_queue = None
        else:
            removed_from_queue = self.storage.tail.value
            self.storage.remove_from_tail()
        
        # then we update our size here to match the new dll length given by this subtraction
        self.size = self.storage.length
        return removed_from_queue

    def len(self):
        #return the self.size after fetching the dll length or just return the self.size if it has been updating with the queue methods
        self.size = self.storage.length
        return self.size
