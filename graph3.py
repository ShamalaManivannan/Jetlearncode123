class Graph():
    def __init__(self,V):
        self.V = V  #vertex number e.g 5
        self.adj = [[]for i in range(V)]

    def add_edges(self,v,w): #Connecting the vertices
        self.adj[v].append(w) 
        self.adj[w].append(v)
        
    def DFSUtil(self,temp,v,visited): #Creating the DFS Function
        visited[v] = True #Setting v as visited
        temp.append(v) #Appending v to the temporary list
        for i in self.adj[v]: #For all the adjecents 
            if visited[i] == False:  
                temp = self.DFSUtil(temp,i,visited)
        return temp
    
    def ConnectedComponents(self):
        visited = [] 
        cc = []
        for i in range(self.V):
            visited.append(False)
        for v in range(self.V):
            if visited[v] == False:
                temp = []
                cc.append(self.DFSUtil(temp,v,visited))     
        return cc
    

g = Graph(5)

g.add_edges(1,0)
g.add_edges(2,1)
g.add_edges(3,4)


cc=g.ConnectedComponents()
print("Following of the connected components:")
print(cc)

