import sys                                                      #needed for maxsize

'''
        The Prim's algorithm states that we should start on a random node so it was used the node 0.
    From this node we can start checking for the edges with the lowest weight.
        The graph list contains the edges for each node, so each element of the list is another list
    with each edge weight. The code will check the first line (first node) and since there are 2 
    connections it will save these two, so 0-1 and 0-3. Since 0-1 was the first edge found it will
    appear in the key list on the first index and the 0-3 was the second found but since it was
    found between 0 and 3 it will not be on the second index of the key list it will appear on the
    fourth (0, 1, 2, 3 -> 4th index).
        The function will then finish with the first list on the graph and step onto the next,
    if any existing edge is found it will only be used if it has less weight than the recorded one.
    In this case it first finds 1-0 but that already has been registred so it passes, then it finds 1-2
    with weight 3 and registers it, but after that it finds 1-3 with weight 8 but since it is greater than
    6 which was recorded before (0-3 weight 6) it will not save this value. It finishes by finding 1-4 weight
    5 and regists this value.
        The code can now go through the rest of the vertices but it never finds weights lower than the existant
    and since all the vertices already have connections it does nothing new.
        To print all of this there is need for 2 lists, one with the parent nodes for each connection (each index
    is equal to the node that the parent connects, so if the first index has -1 then -1 is parent of 0), and one
    which is the graph with all of the weights. 
'''

class Graph(): 
  
    def __init__(self, vertices):                               #implements graph as adjacency matrix
        self.V = vertices                                       #number of vertices
        self.graph = [[0 for column in range(vertices)]         #adjacency matrix with no edges (all connections set to zero)
                    for row in range(vertices)] 
  
    def printMST(self, parent): 
        print ("Edge \t Weight")
        for i in range(1, self.V): 
            print (parent[i], "-", i, "\t", self.graph[i][ parent[i] ])
  
                                                                #from reached nodes find the unreached node with the minimum cost
    def minKey(self, key, mstSet): 
        min = sys.maxsize                                       #set min to infinity (use maxsize which is next best thing!)
        for v in range(self.V):                                 #count through number of vertices
            if key[v] < min and mstSet[v] == False:             #if vertex is less than min and unreached
                min = key[v]                                    #assign to min 
                min_index = v                                   #min_index is position of min in key
        return min_index                                        #return min_index
  
                                                                #find MST 
    def primMST(self): 
        key = [sys.maxsize] * self.V                            #initialise key to list of values all set to infinity; same length as self.V              
        parent = [None] * self.V                                #list for constructed MST 
        key[0] = 0                                              #set first element of key to zero (this is where we start)                                                                                   
        mstSet = [False] * self.V                               #mstSet is list of booleans set to False
        parent[0] = -1                                          #first element of parent list set to -1                        

        for vertex in range(self.V):                            #go through all vertices
            u = self.minKey(key, mstSet)                        #call minKey; minKey returns u (index of unreached node) 
            mstSet[u] = True                                    #mstSet at index of node is set to True                                                                                                
            
                                                                #go through all vertices
            for v in range(self.V):                             #if edge from u to connected node v is > 0 (if there is an edge)   
                if(self.graph[u][v] > 0 and mstSet[v] == False  #and mstSet[v] is unreached
                and key[v] > self.graph[u][v]):
                                                                #and key[v] is greater than the edge cost                 
                    key[v] = self.graph[u][v]                   #(only if the current edge cost is greater will need to change)
                                                                #key[v] takes edge cost
                    parent[v] = u                               #parent[v] is index of node; so list of parents (nodes) is the MST
        self.printMST(parent)                                   #print the list of parents, i.e. the MST                                
  
g = Graph(5) 
g.graph = [ [0, 2, 0, 6, 0], 
            [2, 0, 3, 8, 5], 
            [0, 3, 0, 0, 7], 
            [6, 8, 0, 0, 9], 
            [0, 5, 7, 9, 0]] 
  
g.primMST(); 
