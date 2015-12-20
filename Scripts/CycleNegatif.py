def CycleNegatif(G, w):
    s = G.sommets[0] #un sommet de depart
    Bellman_Ford(G, w, s)
    for u in G.sommets:
        for v in u.voisins:
            if v.dist > u.dist + w[(u, v)]:
                return True
    return False