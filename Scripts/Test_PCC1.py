from PCC1 import PCC1

class Graph:
    def __init__(self):
        self.sommets = list()

class Node:
    def __init__(self, name):
        self.voisins = list()
        self.name = name
    def __str__(self):
        return self.name

A = Node("A")
B = Node("B")
C = Node("C")
D = Node("D")
E = Node("E")
F = Node("F")
A.voisins.append(B);A.voisins.append(F)
B.voisins.append(A);B.voisins.append(C)
C.voisins.append(B);C.voisins.append(D);C.voisins.append(F)
D.voisins.append(C);D.voisins.append(E)
E.voisins.append(D);E.voisins.append(F)
F.voisins.append(A);F.voisins.append(C);F.voisins.append(E)

G = Graph()
G.sommets.append(A)
G.sommets.append(B)
G.sommets.append(C)
G.sommets.append(D)
G.sommets.append(E)
G.sommets.append(F)

inf = float("inf")

w = {
    A:{A:0,   B:20,  C:inf, D:inf, E:inf, F:2},
    B:{A:20,  B:0,   C:2,   D:inf, E:inf, F:inf},
    C:{A:inf, B:2,   C:0,   D:2,   E:inf, F:40},
    D:{A:inf, B:inf, C:2,   D:0,   E:2,   F:inf},
    E:{A:inf, B:inf, C:inf, D:2,   E:0,   F:2},
    F:{A:2,   B:inf, C:40,  D:inf, E:2,   F:0},
}

def print_pred(m):
    for i in m:
        print(str(i), end=": { ")
        for j in m[i]:
            print(str(j) + ":" + str(m[i][j] if m[i][j] is not None else 0), end=' ')
        print("}")
print_pred(PCC1(G, w)[1])
