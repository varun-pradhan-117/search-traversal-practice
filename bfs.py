from typing import List, Dict, Any
from pprint import pprint

Graph = {
    0: [1, 3, 4],
    1: [2, 4],
    2: [5],
    3: [4, 6],
    4: [5, 7],
    5: [],
    6: [4, 7],
    7: [5, 8],
    8: []
}

def bfs(graph: Dict[Any, List[Any]], start: Any) -> List[Any]:
    queue = []
    visited = set()
    path = []

    queue.append(start)
    visited.add(start)

    while queue:
        node = queue.pop(0) # pop first element from queue
        path.append(node)

        for neighbour in graph[node]: # check for connections of graph
            if neighbour not in visited: # If it was not visited append to visited and queue
                visited.add(neighbour) 
                queue.append(neighbour)
    
    return path
    
def main() -> None:
    nodes = bfs(Graph, 0)
    print("Graph (As adjacency list):")
    pprint(Graph, indent=4)
    print("Breadth first search Graph traversal path:")
    print("->".join(map(str, nodes)))


if __name__ == '__main__':
    main()
