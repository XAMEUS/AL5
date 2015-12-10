from utils import dcopy
from math import log, ceil
def PCC1(G, w):
    inf = float("inf")
    D = {u:{u:inf for u in G.sommets} for u in G.sommets}
    Pred = {u:{u:None for u in G.sommets} for u in G.sommets}
    for u in G.sommets:
        for v in G.sommets:
            D[u][v] = w[u][v]
            Pred[u][v] = None if w[u][v] == inf else u
    D_next = dcopy(D)
    Pred_next = dcopy(Pred)
    for t in range(2, ceil(log(len(G.sommets) - 1, 2))):
        for u in G.sommets:
            for v in G.sommets:
                for x in G.sommets:
                    if D_next[u][v] > D[u][x] + w[x][v]:
                        D_next[u][v] = D[u][x] + w[x][v]
                        Pred_next[u][v] = Pred[x][v]
        D = dcopy(D_next)
        Pred = dcopy(Pred_next)
    return (D, Pred)
