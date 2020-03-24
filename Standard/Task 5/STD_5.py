'''
    Linked List creation code
    input: To start the list no input needed, to create a new value (Node) needs value, head value needs a Node, to insert needs the node before and the new data
    output: The only output that can be received is if calling the listprint, it will print the list in the terminal
'''
class Node:
    def __init__(self, dataval = None):                                         # initiallize node
        self.dataval = dataval                                                  # value of the node
        self.nextval = None                                                     # value of the next node

class SLinkedList:                                                              # creating list
    def __init__(self):
        self.headval = None                                                     # initiallize first value as none

    def listprint(self):                                                        # print the list
        printval = self.headval                                                 # start with the head value
        while printval is not None:                                             # while we have a value to print
            print (printval.dataval)                                            # print the data in the node to print
            printval = printval.nextval                                         # move to the next node

    def AtBeginning(self,newdata):                                              # creates new node, will automatically be at the beggining of the list
        NewNode = Node(newdata)

    def AtEnd(self, newdata):                                                   # creates a node to insert at the end of the list
        NewNode = Node(newdata)                                                 # new node
        if self.headval is None:                                                # if the list is empty
            self.headval = NewNode                                              # new node will be the head value
            return
        last = self.headval                                                     # grab the node on the list's beginnning
        while(last.nextval):                                                    # while there is a next value
            last = last.nextval                                                 # move to next value
        last.nextval = NewNode                                                  # when the loop ends we are at the last value so insert new node as the value next to this

    def Insert(self, val_before, newdata):                                      # insert a node 
        if val_before is None:                                                  # if the value before is inexistent
            print("No node to insert after")                                    # inform user there is no value before equal to the input
            return
        else:                                                                   # if the before value exists
            NewNode = Node(newdata)                                             # create new node
            NewNode.nextval = val_before.nextval                                # set next value of the new node to be the same as the node before
            val_before.nextval = NewNode                                        # set the before's node next value to be the node to insert


list = SLinkedList()
list.headval = Node("Mon")

e2 = Node("Tue")
e3 = Node("Thur")
e4 = Node("Fri")
e5 = Node("Sat")
list.headval.nextval = e2
e2.nextval = e3
e3.nextval = e4
e4.nextval = e5


list.AtEnd("Sun")

list.Insert(e2, "Weds")
list.listprint()
