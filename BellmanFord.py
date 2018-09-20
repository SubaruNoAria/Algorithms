#Python Program for Bellman-Ford algorithm
#The shortest path algorithm

from collections import defaultdict
class graph:
    def __init__(self, node):
        self.V = node # Initialize the nodes
        self.graph = [] # default list to store graph

    #Add new edge to current graph
    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])

    #Utility to print the solution
    def printSolution(self, dist):
        print("Vertex Distance from source")
        for i in range(self.V):
            print("%d \t\t %d" % (i, dist[i]))

    #The main function that finds shortest distances from src to all other nodes
    #Also works for negative values
    def BallmanFord(self, src):
        #1. Initialize distances from src to all other nodes as INF
        dist = [float("Inf")] * self.V
        dist[src] = 0

        #2. Relax all edges |V| -1 times. A simple shortest path from src
        #to any other nodes can have at-most |V| - 1 edges
        for i in range(self.V - 1):
            #Update dist value and parent index of the adjacent vertices of the picked nodes
            #consider only those vertices are still in queue
            for u, v, w in self.graph:
                if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w

        #3. check for negative-weight cycles. Step 2 guarantees shortest distances if graph doesn't contain negative weight cycle
        #If a shorter path exist, then there is a cycle
        for u, v, w in self.graph:
            if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                print("Graph contains negative weight cycle")
                return

        #Print all distance
        self.printSolution(dist)

g = graph(5)
g.addEdge(0, 1, -1)
g.addEdge(0, 2, 4)
g.addEdge(1, 2, 3)
g.addEdge(1, 3, 2)
g.addEdge(1, 4, 2)
g.addEdge(3, 2, 5)
g.addEdge(3, 1, 1)
g.addEdge(4, 3, -3)
g.BallmanFord(0)

