import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # if self.value == None: #this will never happen, the binarySearchTree class will only be called on the empty left and right not empty self.values
        #     self.value = value
        #     return
        if value < self.value:
            if not self.left:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)
        elif value >= self.value: # the tests require us to put dupes to the right but we could put them to the left if we wanted
            if not self.right:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # if self.value == None: #dont need to do this, there will never be an empty root
        #     return False
        if self.value == target:
            return True
        elif target < self.value:
            if not self.left:
                return False
            else:
                return self.left.contains(target)
        elif target > self.value:
            if not self.right:
                return False
            else: 
                return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        # if self.value == None: #again unneeded because it will never happen
        #     return "not instantiated"     
        if self.right:
            return self.right.get_max()
        else:
            return self.value
        

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        # if self.value == None: #unnecessary
        #     return "not instantiated"  
        # else:
        cb(self.value)

        if not self.left and not self.right:
            return
        elif not self.right:
            self.left.for_each(cb)
        elif not self.left:
            self.right.for_each(cb)
        else:#at this point we know both exist
            self.left.for_each(cb)
            self.right.for_each(cb)

        # the 4 line conditional can be changed to 
        # if self.right:
        #     self.right.for_each(cb)
        
        # if self.left:
        #     self.left.for_each(cb)


    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal



    def in_order_print(self, node):
        if node:
            node.in_order_print(node.left)
            print(node.value)
            node.in_order_print(node.right)        
# all we want to do is at every node we check right, self, left -> into the stack
# when there isn't left we remove that value from the stack
# we check the right, if there is something there we do the same thing
# then we go to the new leftmost value, should be the top of the stack and return that value as well
# at this point we dont want to check left, only right
# on the right value we want to start the process over again
# once we can't go right we want to return to the root
# then we want to go right and repeat the process until the stack is empty

# if node.left:
#     #we only care about right after we've exhausted left
#     # add the left to the backburner
#     #go left
# else:
#     if node.right:
    # add right node to stack
    #go right 

    #pop the previous node off the stack because it was the lowest
    # then you gotta check if there's a left for that right_node (recursion here)
    #after we are done with that we move to the previous member of the stack and only check its right (helper function? if it has a right we do recursion on that)
    # else:
    #     #print the node you are on
    #     #go back and print that node as well
    #     #helper function to move to the right of that node? (check the 2 for a 3 and if there call this function, if not just print this node value and move to the previous left most in the stack...we can't do pur recursion on that one either!!!!!)
    #         #recursion


    #     depth_stack = []
    #     #depth_stack.append(node) #we don't want to append the root to the stack do we? lower numbers will be above it
    #     while depth_stack != []:
    #         #node = depth_stack[-1]#pop doesn't happen until it has no left values (all the left values have been processed by recursion), BUT we still need to use the top of the stack to continue traversing
    #         if node.right:
    #             depth_stack.append(node.right)
    #         if node.left:
    #             depth_stack.append(node.left)  
    #             node.in_order_print(node.left)            
    #         else:
    #             node = depth_stack.pop(-1)
    #             if node.right:
    #                 print(node.value)
    #                 node.in_order_print(node.right)
    #             else:
    #                 node = depth_stack.pop(-1)
    #                 print(node.value)
                
        # pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal

        #     Iterative BFT
        # create queue
        # add root to queue
        # while queue is not empty
        # node = pop head of queue
        # DO THE THING!!! (print)
        # add children of node to queue
    def bft_print(self, node):
        breadth_queue = []
        breadth_queue.append(node) 
        output_for_tests = ""
        while breadth_queue != []:
            node = breadth_queue.pop(0)
            #______________________________________________________DON'T NEED TO MANUALLY MATCH THE "output", the stdout stream just matches what is in the terminal from your functions results/print
            # output_for_tests += (str(node.value)+"\\n")
            # print(output_for_tests)
            #sys.stdout.write(str(node.value) + "\n")
            #sys.stdout.write(output_for_tests)
            print(node.value)
            if node.left:
                breadth_queue.append(node.left)
            if node.right:
                breadth_queue.append(node.right)
        
        # print(output_for_tests)


    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal

        #     Iterative DFT
        # create stack
        # add root to stack
        # while stack is not empty
        # node = pop top of stack
        # DO THE THING!!! (print)
        # add children of node to stack
    def dft_print(self, node):
        depth_stack = []
        depth_stack.append(node) 

        while depth_stack != []:
            node = depth_stack.pop(-1)
            print(node.value)
            if node.left:
                depth_stack.append(node.left)
            if node.right:
                depth_stack.append(node.right)
        
        

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
