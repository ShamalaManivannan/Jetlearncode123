class Graph:
    def __init__(self,n):
        self.n = n
        self.adj = [[]*n for i in range(n)]

    def Edge(self,x,y):
        self.adj[x-1].append(y-1)
        self.adj[y-1].append(x-1)

    #BFS is Breadth First Search

    def BFS(self,source):
        visited = [False]*self.n
        queue = []    #empty list to insert the values that are visited
        queue.append(source)
        visited[source] = True #Setting it true if the source is visited
        result = []
        while len(queue) > 0: #making sure if queue is not empty
            s = queue.pop(0) #take the first element
            result.append(s)
            for node in self.adj[s]:
                if visited[node] == False:
                    queue.append(node)
                    visited[node] = True
        return result
    

#Creating the object for the graph class

graph = Graph(5)
graph.Edge(1,2)
graph.Edge(1,3)
graph.Edge(2,4)
graph.Edge(4,5)

print(graph.BFS(1))
    
