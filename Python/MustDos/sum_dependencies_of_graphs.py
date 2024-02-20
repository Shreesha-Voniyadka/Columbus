def addEdge(adj, u, v):

    adj[u].append(v)s


# Driver code
if __name__ == '__main__':

    V = 4
    adj = [[] for i in range(V)]

    addEdge(adj, 0, 2)
    addEdge(adj, 0, 3)
    addEdge(adj, 1, 3)
    addEdge(adj, 2, 3)

    print("Sum of dependencies is",
          findSum(adj, V))
