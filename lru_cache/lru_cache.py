import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.

    num_nodes_max = int
    num_nodes_contained = length
    nodes_storage = dll
    nodes_dict = dictionary
    """
    def __init__(self, limit=10):
        self.num_nodes_max = limit
        self.nodes_storage = DoublyLinkedList()
        self.nodes_dict = {}
        self.num_nodes_contained = len(self.nodes_dict)

        

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.

    find it by key, -- so from dictionary
     capture it, -- copy it, dont mess with the actual node here?
      add it to head, -- dictionaries are unordered so we are working with the dll now
       delete it from location?, --the node in question's self.prev's next will now equal the node in question's self.next
       
        return what was captured or the head
    """
    def get(self, key):
        #find by key `if key in nodes_dict`
            #capturedValue = nodes_dict[key]
            # move the node with this value to the front (we have to find values in the middle here)
                #iterate through the dll.head.next(current_node) until the node.value equals the key that was entered (while the value doesn't equal what was entered we reassign the current_node = head.next)
                #move that entire node to the front (move_to_front(the node that was found))
                    #if that doesn't work call The ListNode's delete method and add the node to the head using the dll.add_to_head
                    #move to front should already delete it from it's prior location
            #return capturedValue
        # else
            #return None
        if key in self.nodes_dict:
            capturedValue = self.nodes_dict[key]
            current_node = self.nodes_storage.head
            while current_node.value != key:
                current_node = current_node.next
            self.nodes_storage.move_to_front(current_node)
            return capturedValue
        else:
            return None
        

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, value):
        if key not in self.nodes_dict:
            if int(len(self.nodes_dict)) == self.num_nodes_max:
                key_to_delete = self.nodes_storage.remove_from_tail() #this SHOULD return the value
                del self.nodes_dict[key_to_delete]
            self.nodes_storage.add_to_head(key)
            self.nodes_dict[key] = value
        else:
            self.nodes_dict[key] = value
            current_node = self.nodes_storage.head
            
            while current_node.value != key:
                current_node = current_node.next
            self.nodes_storage.move_to_front(current_node)

        #add the key value pair to the dictionary
            #if key doesn't exist 
                #if the length of the dictionary equals the max
                    #remove the tail
                    #remove the pair associated with the key returned from the tail from the dictionary
                #add the key to the head  (see below as to why we aren't using the k-v pair)
                #add the key value pair to the dictionary
            #else overwrite the value of the key in the dictionary
                #it will be easier to not find the value associated with this key in the "middle" of the dll so the dll must only care about the key values
                # move the node with this value to the front (we have to find values in the middle here)
                    #iterate through the dll.head.next(current_node) until the node.value equals the key that was entered (while the value doesn't equal what was entered we reassign the current_node = head.next)
                    #move that entire node to the front (move_to_front(the node that was found))
                        #if that doesn't work call The ListNode's delete method and add the node to the head using the dll.add_to_head
                        #move to front should already delete it from it's prior location
        
