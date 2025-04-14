class Graph:
    def __init__(self):
        self.graph = {}  ##list of values of neighbouring to them
        self.visited = set()  #A set to take track of visited nodes so we dont revisit them

    def add_edge(self, node, neighbours): #Assigning node with its neighbors function
        self.graph[node] = neighbours  

    def dfs(self, root): #Depth First Search function
        if root not in self.visited: #If the root has not been visited
            print(root) #Printing the root node itself
            self.visited.add(root) #Adding the root as visited
            for neighbour in self.graph.get(root):  
                self.dfs(neighbour) #Recursive function


graph = Graph()


graph.add_edge('A', ['B', 'C'])
graph.add_edge('B', ['C'])
graph.add_edge('C', ['E', 'D'])
graph.add_edge('E', ['D'])
graph.add_edge('D', [])


print("From Root A:")
graph.dfs('A')
