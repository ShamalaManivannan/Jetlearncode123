graph = { 'A':['B','C'], #list of values of neighbouring to them
         'B':['C'], 
         'C':['E','D'], 
         'E':['D'], 
         'D':[], }

visited = set() 

def DFS(visited,graph,root): #Depth First Search function
    if root not in visited: #Printing the root node itself
        print(root)
        visited.add(root) #Adding the root as visited
        for neighbour in graph[root]: 
            DFS(visited,graph,neighbour)  #recursive function
        
print('From root A:')   
DFS(visited,graph,'A')

print('From root B:')
DFS(visited,graph,'B')
