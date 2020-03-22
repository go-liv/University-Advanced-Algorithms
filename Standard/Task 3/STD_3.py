class Graph(object):
    
    def __init__(self, size):
        self.adjMatrix = []
        for i in range(size):
            self.adjMatrix.append([0 for i in range(size)])
        self.size = size        

    #methods for (1) adding a vertex; (2) adding an edge; (3) removing an edge; and (4) printing the
    #matrix should appear here

    #Adding a vertex by calling this function
    def vertexAdd(self):
        for i in range(self.size):
            self.adjMatrix[i].append(0)
        self.size += 1
        self.adjMatrix.append([0 for i in range(self.size)])

    #Adding an edge by calling this function
    def edgeAdd(self, x, y):
        self.indexX = self.adjMatrix[x - 1]
        self.indexY = self.adjMatrix[y - 1]

        #there is no direct need to check if there is an edge already between both vertices since it would just spend more code than just changing them no matter the state of both
        # but code for that will be presented anyway
        #if there was an error and one of the lines reports an existing edge but the other line doesn then this should fix that error by creating the edge
        if(self.indexX[y - 1] == 1 and self.indexY[x - 1] == 1):
            print("Edge already exists")
            pass
        else:
            self.indexX[y - 1] = 1
            self.indexY[x - 1] = 1


    def edgeDel(self, x, y):
        self.indexX = self.adjMatrix[x - 1]
        self.indexY = self.adjMatrix[y - 1]

        #as before checking whether the edge is already removed space and time consuming since we are just changing values in a list, 
        # therefore no more that checking if there is an edge to remove will be done
        if(self.indexX[y - 1] == 0 and self.indexY[x - 1] == 0):
            print("Edge already removed or never created")
            pass
        else:
            self.indexX[y - 1] = 0
            self.indexY[x - 1] = 0


    def printMatrix(self):
        #the following code just prints the matrix in a easy way to read
        print("-----> Here is your graph as a matrix table. <-----")
        
        #print the first row to display collumns
        print("")
        print("        ", end = "")
        for i in range(self.size):
            print(" " + str(i + 1) + " ", end = " ")
        print("")
        print("")
        
        #print the other rows where the matrix is printed
        for i in range(self.size):
            print("   " + str(i + 1), end = "   |")
            for j in range(self.size):
                print(" " + str(self.adjMatrix[i][j]), end = " |")
            print("")
            print("")



#remember list indexing - this is 1 out, unless we start the matrix at 0 (not a +ve integer)     
def main():
        g = Graph(6)
        g.vertexAdd()
        g.edgeAdd(1, 2)
        g.edgeAdd(3, 2)
        g.printMatrix()

            
if __name__ == '__main__':
   main()
