""" Basic BST code for inserting (i.e. building) and printing a tree

    Your ***second standard viva task*** (of 5) will be to implement a find method into
    the class BinaryTree from pseudocode. See the lab task sheet for Week 4. 

    Your ***first advanced viva task*** (of 3) will be to implement a remove (delete) method
    into the class Binary Tree from partial pseudocode. See the lab task sheet for Week 4.

    Since the given code is in python it is strongly suggested you stay with python; but
    if you want to reimplement as C++ this is also OK (see the lab sheet guidance). 
"""

import math

""" Node class
"""

class Node:
    def __init__(self, data = None):
        self.data = data
        self.left = None
        self.right = None

""" BST class with insert and display methods. display pretty prints the tree
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

    # - - - Iterative search - - - #
    ## This function allows for a target to be searched on the tree iteratively                                                                   #
    # It works by starting with the root node and going from that node to the upper one                                                           #
    # Therefore it checks if the value encontered on the current node is less or greater than the target to search                                #
    # If it is lower then the target should be more to the right of the node, if it's greater then it should be to the left                       #
    # The code will continue to go to right or left of the nodes until there are no more nodes in the tree or until it finds the required target ##
    def find_i(self, target):
        #if there is no tree it wont run the code
        if self.root != None:
            cur_node = self.root
            while cur_node != None:
                if cur_node.data == target:
                    print("Iterative: True")
                    return True
                #if target greater then run the search using the right node
                elif cur_node.data > target:
                    cur_node = cur_node.left
                #if target less then run the search using the left node
                else:
                    cur_node = cur_node.right
            print("Iterative: False")
            return False
        else:
            print("Iterative: No tree created")
            return None
    # - - - end of iterative - - - #


    # - - - Recursive search - - - #
    ## This function allows for a target to be searched on the tree recursively                                                                        #
    # It works by starting with the root node and going from that node to the upper one                                                                #
    # Therefore it checks if the value encontered on the current node is less or greater than the target to search                                     #
    # If it is lower then the function runs again but it uses the right node as the node to search from, if it's greater then it uses the left one     #
    # The code will continue to go to right or left of the nodes until there are no more nodes in the tree or until it finds the required target      ##
    def find_r(self, target):
        #if there is no tree it wont run the code
        if self.root != None:
            if self._find_r(target, self.root):
                print("Recursive: True")
                return True
            print("Recursive: False")
            return False
        else:
            print("Recursive: No tree created")
            return None
    
    def _find_r(self, target, cur_node):
        #if target greater then run the search using the right node
        if target > cur_node.data and cur_node.right:
            return self._find_r(target, cur_node.right)
        #if target less then run the search using the left node
        elif target < cur_node.data and cur_node.left:
            return self._find_r(target, cur_node.left)
        if target == cur_node.data:
            return True
    # - - - end of recursive - - - #

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
bst.find_i(10)
bst.find_r(10)





