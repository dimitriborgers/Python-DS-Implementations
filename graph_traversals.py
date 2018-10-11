def DFS(g, u, discovered):
    for e in g.incident edges(u): 
        v = e.opposite(u)
        if v not in discovered:
            discovered[v] = e 
            DFS(g, v, discovered)

def BFS(g, s, discovered):
    level = [s]
    while len(level) > 0:
        next level = [ ] 
        for u in level:
            for e in g.incident edges(u): 
                v = e.opposite(u)
                if v not in discovered:
                    discovered[v] = e
                    next level.append(v) 
        level = next level
