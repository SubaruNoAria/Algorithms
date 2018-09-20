#Python Program for Floyd Warshall Algorithm

#Number of vertices in the graph
V = 4
#Set the infinity number to each node.
INF = 999999

#Solve all pair shortest path
def floydwarshall(g):
    """dist[][] will be the output matrix of the shortest distances
    between every pair of vertices"""
    """initializing the solution matrix same as input graph matrix
    it is based on shortest paths considering no intermediate vertices
    """
    #Note here, map function has changed from Py2 to Py3, map() retursn an iterator in Py3
    #use list(map()) to convert it into a subscriptable list
    dist = list(map(lambda i: list(map(lambda j: j, i)), g))
    """Add all vertices one by one to the set of intermediate vertices
    """
    """Before start of an iteration, we have shortest distances between all pairs of vertices
    such that the shortest distances consider only the vertices in the set {0, 1, .. k-1} as intermediate vertices"""
    """After the end of a iteration, vertex no. k is added to the set of intermediate vertices and the set becomes {0, 1, .. k-1}"""

    for k in range(V):
        #Pick all vertices as source one by one
        for i in range(V):
            #Pick all vertices as destination for the above picked source
            for j in range(V):
                #If vertex k is on the shortest path from i to j, then update the value of dist[i][j]
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    printSolution(dist)
#Print solution
def printSolution(dist):
    print("The shortest distances between every pair of vertices")
    for i in range(V):
        for j in range(V):
            if dist[i][j] == INF:
                print("%7s" % ("INF"))
            else:
                print("%7d\t" %(dist[i][j]))
            if j == V-1:
                print("")

g = [[0, 5, INF, 10],
     [INF, 0, 3, INF],
     [INF, INF, 0, 1],
     [INF, INF, INF, 0]
     ]
print(floydwarshall(g))

