# A binary tree node
class Node:
 
    # Constructor to create a new node
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

def insert(node, data):
 
    # 1. If the tree is empty, return a new node
    if node is None:
        return (Node(data))
 
    else:
        # 2. Otherwise check data if it's smaller but in left
        if data <= node.data:
            node.left = insert(node.left, data)
        else:
        # if it's larger put in right
            node.right = insert(node.right, data)
 
        # Return the node pointer
        return node
 

def minValueIteration(node):
    current = node
 
    # loop down to find the lefmost leaf which is the lowest value
    while(current.left is not None):
        current = current.left
 
    return current.data

def minValueRecursion(node):
    current = node
 
    # check if it's last on left then return it
    if  current.left is  None:
        return current.data
    else:
    #else reenter the function with left of the current
        return minValueRecursion(current.left)

        
 
#Trial
root = None
root = insert(root,9)
insert(root,21)
insert(root,11)
insert(root,3)
insert(root,4)
insert(root,9)
print ("minmum for loop "+str(minValueIteration(root)))
print("minmum recursion "+str(minValueRecursion(root)))