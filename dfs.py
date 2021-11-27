from typing import List, Dict, Any
from pprint import pprint

Graph = {
    'A': ['B','C','D'],
    'B': ['A','C','D','E'],
    'C': [5],
    'D': [4, 6],
    'E': [5, 7],
    'F': [],
}

def dfs(visited, graph: Dict[Any, List[Any]], node: Any):
    if node not in visited: 
        if not len(visited):
            print(node,end="")
        else:
            print("->",node,end="")
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)
    
def main() -> None:
    visited=set()
    print("Graph (As adjacency list):")
    pprint(Graph, indent=4)
    print("Depth first search Graph traversal path:")
    dfs(visited,Graph, 0)

if __name__ == '__main__':
    main()
