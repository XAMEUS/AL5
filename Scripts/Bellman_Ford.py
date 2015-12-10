def Bellman_Ford(G, w, s):
    inf = float("inf")
    for u in G.sommets:
        if u != s: u.dist = inf
        u.pred = None
    s.dist = 0
    for t in range(1, len(G.sommets)):
        for u in G.sommets:
            for v in u.voisins:
                if v.dist > u.dist + w[(u, v)]:
                    v.dist = u.dist + w[(u, v)]
                    v.pred = u
    return [(u.pred, u) for u in G.sommets if u != s]
    