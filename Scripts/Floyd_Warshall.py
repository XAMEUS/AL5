from utils import dcopy
def Floyd_Warshall(G, w):
    inf = float("inf")
    D = {u:{u:inf for u in G.sommets} for u in G.sommets}
    Pred = {u:{u:None for u in G.sommets} for u in G.sommets}
    for u in G.sommets:
        for v in G.sommets:
            D[u][v] = w[u][v]
            Pred[u][v] = None if w[u][v] == inf else u
    D_next = dcopy(D)
    Pred_next = dcopy(Pred)
    for x in G.sommets:
        for u in G.sommets:
            for v in G.sommets:
                    if D[u][x] + D[x][v] < D_next[u][v]:
                        D_next[u][v] = D[u][x] + D[x][v]
                        Pred_next[u][v] = Pred[x][v]
        D = dcopy(D_next)
        Pred = dcopy(Pred_next)
    return (D, Pred)