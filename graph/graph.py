import numpy as np
import numpy.linalg as lin

class Graph:
    def __init__(self, adjMat, nodeProps):
        self.adjMat = adjMat
        self.nodeProps = nodeProps
        
    
    def isComplete(self): # A complete graph has one edge between every two vertices 
        for i in range(len(self.adjMat)):
            for j in range(len(self.adjMat)):
                if i == j and self.adjMat[i][j] != 0:
                    return False
                if i != j and self.adjMat[i][j] != 1:
                    return False
        return True
    
    def degreeVec(self): # Returns an array with entries being the degree of each vertex
        degreeVec = list(range(len(self.adjMat)))
        for i in range(len(self.adjMat)):
            sumRow = 0
            for j in range(len(self.adjMat)):
                sumRow += self.adjMat[i][j]
            degreeVec[i] = sumRow
        return degreeVec
    
    def degreeMat(self): # Returns a matrix where the diagonal entries are the degrees of each vertex
        degreeMat = np.zeros((len(self.adjMat), len(self.adjMat)))
        for i in range((len(self.adjMat))):
            sumRow = 0
            for j in range((len(self.adjMat))):
                sumRow += self.adjMat[i][j]
            degreeMat[i][i] = sumRow
        return degreeMat
    
    def connectedComponents(self): # Returns the number of connected components in the graph
        laplacian = self.degreeMat() - self.adjMat
        numColumns = len(self.adjMat)
        return numColumns - lin.matrix_rank(laplacian)
    
    def isConnected(self): # A graph is connected if there is at least one path between every two vertices
        return self.connectedComponents() == 1
    
    def numEdges(self): # Returns the number of edges in the graph
        return np.trace(lin.matrix_power(self.adjMat,2))/2
    
    def numTriangles(self): # A triangle is a cycle of length 3
        return np.trace(lin.matrix_power(self.adjMat, 3))/6 
    
    def numQuadrangles(self): # A quadrangle is a cycle of length 4
        sumSquares = 0
        for i in range(len(self.degreeVec())):
            sumSquares += pow(self.degreeVec()[i],2)
        return (np.trace(lin.matrix_power(self.adjMat,4)) + 2 * self.numEdges() - 2 * sumSquares)/8
    
    def isTree(self): # A tree is a graph in which there is a unique path between every two vertices (compare with connected) 
        return self.isConnected and self.numEdges() == len(self.adjMat) -1
    
    def numWalksBet(self, length, start, end): # Returns the number of walks of length "length" starting at "start" and ending at "end"
        return lin.matrix_power(self.adjMat, length)[start][end]
    
    def totalNumWalks(self, length): # Returns the total number of walks of length "length"
        rightmul = np.ones((1, len(self.adjMat)))
        leftmul = np.ones((len(self.adjMat), 1))
        return np.vdot(np.matmul(rightmul, lin.matrix_power(self.adjMat, length)), leftmul)

    def hasEulerianCycle(self): # An Eulerian cyce exists if and only if the degree of every vertex is even
        for i in range(len(self.degreeVec())):
            if self.degreeVec()[i] % 2 == 1:
                return False
        return True
    
    def hasHamiltonianCycle(self): # An Hamiltonian cycle exists on a simple graph with n >= 3 vertices if every vertex has degree >= n/2
        if len(self.adjMat) < 3:
            return False
        for i in range(len(self.degreeVec())):
            if self.degreeVec()[i] < len(self.adjMat)/2:
                return False
        return True
    
    def isBipartite(self): # A graph is bipartite iff it satisfies the property that lambda is an eigenvalue iff - lambda is an eigenvalue for adjMat
        eigvals = list(set(lin.eigvals(self.adjMat)))
        sumEigs = 0
        for i in range(len(eigvals)):
            sumEigs += round(eigvals[i], 10) # hopefully this is enough precision for our eigenvalues
        return sumEigs == 0
    
    def isStar(self): # A graph is a star iff it is a tree and is bipartite
        return self.isTree() and self.isBipartite()
    
    def isRegular(self): # A graph is regular if all of its vertices are of the same degree
        for i in range(len(self.degreeVec()) - 1):
            if self.degreeVec()[i] != self.degreeVec()[i+1]:
                return False
        return True