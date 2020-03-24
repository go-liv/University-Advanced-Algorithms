""" 
    Basic BST code for inserting (i.e. building) and printing a tree
    input: to create a node input is the data but it is optional, in case of no data the node is created with None, to create a tree there is no need for input aswell.
To insert a node we need the data of the node to insert, to find or remove we need the data of the target we are looking for.
    output: The find function outputs a boolean with the value True for found False for not found, the display function prints the tree with a nice formatting, so branches appear and connections,
the remove function outputs the same as the find but True for eliminated, False for not eliminated.
"""

import math

""" 
    Node class
"""

class Node:
    def __init__(self, data = None):
        self.data = data
        self.left = None
        self.right = None

""" 
    BST class with insert and display methods. 
    Display pretty prints the tree, adds branches between the nodes by going between them and checking if there are neighbour nodes, where they are,
so it can print the connections on the right positions.
    Insert allows the insertion of a new node, if the root of the tree is None then the new node will be inserted in the root, else we need to find where to insert it.
The function will then call another function that checks if the data in the node is less than the data of the current node (the last one to be inserted/used), if the data
is less than the current node's then we check if the current node already as a left neighbour, if it does we recursivelly run the function again so that we can find the correct place,
if there is no neighbour the node is inserted in there. Same goes for the case of the data of inserting node to be greater than the current node's we just use the right side now
instead of the left. If the value is equal to the current node then it means the value is already present in the tree.
"""

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(data, self.root)

    def _insert(self, data, cur_node):
        if data < cur_node.data:
            if cur_node.left is None:
                cur_node.left = Node(data)
            else:
                self._insert(data, cur_node.left)
        elif data > cur_node.data:
            if cur_node.right is None:
                cur_node.right = Node(data)
            else:
                self._insert(data, cur_node.right)
        else:
            print("Value already present in tree")

    ''' 
    - - - Iterative search - - - 
        This function allows for a target to be searched on the tree iteratively                                                                   
     It works by starting with the root node and going from that node to the upper one                                                           
     Therefore it checks if the value encontered on the current node is less or greater than the target to search                                
     If it is lower then the target should be more to the right of the node, if it's greater then it should be to the left                       
     The code will continue to go to right or left of the nodes until there are no more nodes in the tree or until it finds the required target 
    '''
    
    def find_i(self, target):
        if self.root != None:                                                                   # if there is a tree run the code
            cur_node = self.root                                                                # set current node as the root node                                                      
            while cur_node != None:                                                             # loop while there is a current node
                if cur_node.data == target:                                                     # if the node data is equal to what we are searching (target) return True
                    print("Iterative: True")
                    return True
                elif cur_node.data > target:                                                    # if target greater then current node data run the search using the left node
                    cur_node = cur_node.left
                else:                                                                           # if target less then run the search using the left node
                    cur_node = cur_node.right
            print("Iterative: False")
            return False
        else:                                                                                   # if there is no initial tree then don't run the code
            print("Iterative: No tree created")
            return None


    ''' 
    - - - Recursive search - - - 
        This function allows for a target to be searched on the tree recursively                                                                        
     It works by starting with the root node and going from that node to the upper one                                                                
     Therefore it checks if the value encontered on the current node is less or greater than the target to search                                     
     If it is lower then the function runs again but it uses the right node as the node to search from, if it's greater then it uses the left one     
     The code will continue to go to right or left of the nodes until there are no more nodes in the tree or until it finds the required target      
    '''

    def find_r(self, target):
        if self.root != None:                                                                  # if there is a tree it will run the code
            if self._find_r(target, self.root):                                                # call the _find_r function, if it returns True we can return True 
                print("Recursive: True")
                return True
            print("Recursive: False")                                                          # if the _find_r func returns false find_r will return false
            return False
        else:                                                                                  # without a tree the code will not run 
            print("Recursive: No tree created")
            return None
    
    def _find_r(self, target, cur_node):
        if target > cur_node.data and cur_node.right:                                          # if target greater then current node and we have a right node
            return self._find_r(target, cur_node.right)                                        # run the search using the right node
        elif target < cur_node.data and cur_node.left:                                         # if target less then current node and we have a left node
            return self._find_r(target, cur_node.left)                                         # run the search using the left node
        if target == cur_node.data:                                                            # if the current node's data is equal to the target
            return True                                                                        # return True


    def display(self, cur_node):
        lines, _, _, _ = self._display(cur_node)
        for line in lines:
            print(line)


    def _display(self, cur_node):
        
        if cur_node.right is None and cur_node.left is None:
            line = '%s' % cur_node.data
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        if cur_node.right is None:
            lines, n, p, x = self._display(cur_node.left)
            s = '%s' % cur_node.data
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2
        
        if cur_node.left is None:
            lines, n, p, x = self._display(cur_node.right)
            s = '%s' % cur_node.data
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        left, n, p, x = self._display(cur_node.left)
        right, m, q, y = self._display(cur_node.right)
        s = '%s' % cur_node.data
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2

    '''
    - - - Iterative Remove function and dependencies - - - 
        These functions handle any removal of a node.                                                                   
     In remove we handle the node removal by checking if it has any base cases we can get advantange from.           
     In if_left_and_right we handle a specific case where a node to be eliminated has children both left and right,  
     with that case we have to get the children in the right positions so that the tree stays composed              
    '''

    def if_left_and_right(self, node):                                                      # this function handles when children are encontered left and right, it will just check which child can replace the parent 
        delNodeParent = node
        delNode = node.right

        while delNode.left:                                                                 # here we can travel to the left side of the list of nodes but first the parent swaps with the delNode
            delNodeParent = delNode
            delNode = delNode.left
        
        node.data = delNode.data                                                            # change the data in the node we want to delete with the data on the last node on the left

        #then we can check if the values of the right node while a right one exist
        if delNode.right:                                                                   # we use this to be able to check whether we have any nodes on the right of our node to delete
            if delNodeParent.data > delNode.data:                                           # if so then we need to check where the right node needs to go
                delNodeParent.left = delNode.right                                          # if the data of the parent node is greater than the previous node we can swap them
            else:
                delNodeParent.right = delNode.right                                         # else the parent will have itself as the right neighbour
        else:
            if delNodeParent.data > delNode.data:                                           # with no right neighbours we can just check if the parent will have the left or right side removed
                delNodeParent.left = None                                                   # if the data of the parent is greater than the one of the node to delete we remove the left side of the parent
            else:
                delNodeParent.right = None                                                  # else we remove the right one

    def remove(self, target):
        if self.root is None:                                                               # if there is no root then there is nothing to remove
            return False

        elif self.root.data == target:                                                      # if the root node is the target then we can eliminate it right now 
            if self.root.left is None and self.root.right is None:                          # if it is isolated then just substitute it to none 
                self.root = None
            elif self.root.left and self.root.right is None:                                # if there is a left node then we put that left node in the space were the root node is
                self.root = self.root.left
            elif self.root.right and self.root.left is None:                                # same as above but with the right node
                self.root = self.root.right
            elif self.root.right and self.root.left:                                        # if there are nodes left and right then we need to call the function that can handle it
                self.if_left_and_right(self.root)
        parent = None
        node = self.root

        while node and node.data != target:                                                 # if the root node isn't the target we need to find the target first and then remove it
            parent = node
            if target < node.data:
                node = node.left
            elif target > node.data:
                node = node.right

        #if a target is found or not will depend on the value stored by the node variable
        #Target not found
        if node is None or node.data != target: 
            print("Target not found")
            return False
        #Target has no children
        elif node.left is None and node.right is None:                                      # if the target is alone without children then we just need to eliminate the target 
                                                                                            #from the corresponding node (smaller targets on the left, bigger on the right)
            if target < parent.data:
                parent.left = None
            else:
                parent.right = None
            print("Target eliminated...")
            return True
        #Target has left child only
        elif node.left and node.right is None:                                               # if just the left child is there then we just need to substitute the target node with this child
            if target < parent.data:
                parent.left = node.left
            else:
                parent.right = node.left
            print("Target eliminated...")
            return True
        #Target has right child only
        elif node.left is None and node.right:
            if target < parent.data:                                                         # same as above but with right child
                parent.left = node.right
            else:
                parent.right = node.right
            print("Target eliminated...")
            return True
        #Target has right and left children
        else:
            self.if_left_and_right(node)



#example calls, which construct and display the tree       
bst = BinaryTree()
bst.insert(4)
bst.insert(2)
bst.insert(6)
bst.insert(1)
bst.insert(3)
bst.insert(5)
bst.insert(7)
bst.insert(8)
bst.insert(9)
##bst.insert(10)
##bst.insert(11)
##bst.insert(12)
##bst.insert(13)
##bst.insert(14)
##bst.insert(15)
##bst.insert(100)
##bst.insert(200)

bst.display(bst.root)
bst.remove(3)
bst.display(bst.root)




 
