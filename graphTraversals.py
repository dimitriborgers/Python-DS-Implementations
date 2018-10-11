def DFS(g, u, discovered):
    for e in g.incident edges(u): 
		v = e.opposite(u)
		if v not in discovered:
            discovered[v] = e 
    	    DFS(g, v, discovered)
