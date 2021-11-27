def heur(n):
    H_dict={
        'A':12,
        'B':4,
        'C':7,
        'D':3,
        'E':8,
        'F':2,
        'H':4,
        'I':9,
        'S':13,
        'G':0
    }
    return H_dict[n]

def neighbors(v):
    if v in nodes:
        return nodes[v]
    else:
        return None

def hill_climb(start_node, end_node):
    open_nodes=set(start_node)
    closed_nodes=set()
    g={}
    parents={}
    g[start_node]=0
    parents[start_node]=start_node
    while len(open_nodes)>0:
        n=None
        for v in open_nodes:
            if n==None or (g[v]+heur(v))<(g[n]+heur(n)):
                n=v
        
        if n==end_node or nodes[n]==None:
            pass
        else:
            for (m,weight) in neighbors(n):
                if m not in open_nodes and m not in closed_nodes:
                    open_nodes.add(m)
                    parents[m]=n
                    g[m]=g[n]+weight

                else:
                    if g[m]> g[n]+weight:
                        g[m]=g[n]+weight
                        parents[m]=n
                        if m in closed_nodes:
                            closed_nodes.remove(m)
                            open_nodes.add(m)

        if n==None:
            print("No possible path")
            return 0
        
        if n==end_node:
            path=[]

            while parents[n]!=n:
                path.append(n)
                n=parents[n]
            path.append(start_node)
            path.reverse()

            print(f'Path:{path}')
            return path
        open_nodes.remove(n)
        closed_nodes.add(n)
    print("No possible path")
    return 0

nodes={
    'S':[('A',3),('B',2)],
    'A':[('C',4),('D',1)],
    'B':[('E',3),('F',1)],
    'C':[('B',1)],
    'D':None,
    'E':[('H',5)],
    'F':[('I',2),('G',3)],
    'G':None,
    'H':None,
    'I':None
}

hill_climb('S','G')