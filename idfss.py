from collections import defaultdict

class Graph: 
    def __init__(self,vertices):
        self.V = vertices
        # default dictionary to store graph
        self.graph = defaultdict(list)
        self.visited=[]
  
    def addEdge(self,u,v):
        self.graph[u].append(v)
  
    def DLS(self,src,target,maxDepth):
        self.visited.append(src)
        if src == target : return True
  
        if maxDepth <= 0 : return False
        
        for i in self.graph[src]:
                if(self.DLS(i,target,maxDepth-1)):
                    return True
        return False

    def IDDFS(self,src, target, maxDepth):
  
        # Repeatedly depth-limit search
        for i in range(maxDepth):
            self.visited=[]
            if (self.DLS(src, target, i)):
                return i
            print(f"Depth{i} : ",end="")
            print(*self.visited,sep="->")
            print("Not found")
            print("-"*30)
        return -1

#Create a graph with greater depth on the left than right  
g = Graph(7);
g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(1,3)
g.addEdge(1,4)
g.addEdge(4,7)
g.addEdge(7,8)
g.addEdge(2,5)
g.addEdge(2,6)

src=0
target=int(input("Enter target node:"))
maxDepth=4

#walrus operator to get depth required
if (depth:=g.IDDFS(src, target, maxDepth)) >=0:
    print ("Target is reachable from source within depth =",depth)
    print("Path:",end="")
    print(*g.visited,sep="->")
else :
    print ("Target not found in given graph")
