class Graph:
    def __init__(self,n):
        self.n = n
        self.adj = [[] for i in range(n)]

    def Edge(self,x,y):
        self.adj[x-1].append(y-1)
        self.adj[y-1].append(x-1)

    #BFS is Breadth First Search

    def BFS(self,source):
        visited = [False]*self.n
        distance = [-1]*self.n #Initialize distances to (-1 not visited)
        queue = []    #empty list to insert the values that are visited
        queue.append(source)
        visited[source] = True #Setting it true if the source is visited
        distance[source] = 0
        
        result = []
        
        
        
        while queue: #making sure if queue is not empty
            s = queue.pop(0) #take the first element/source
            result.append(s)
            for node in self.adj[s]:
                if not visited[node]:
                    queue.append(node)
                    visited[node] = True
                    distance[node] = distance[s] + 1
        return distance
    

#Creating the object for the graph class

graph = Graph(5)
graph.Edge(1,2)
graph.Edge(1,3)
graph.Edge(2,4)
graph.Edge(4,5)

print(graph.BFS(0))
    
