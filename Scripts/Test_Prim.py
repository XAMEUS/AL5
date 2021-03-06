from Prim import Prim

class Noeud:
    def __init__(self, val):
        self.val = val
        self.voisins = list()
        self.couleur = "blanc"
        self.priorite = 0
        self.pred = None
    def __str__(self):
        return "Noeud(" + str(self.val) + ")"
    def __lt__(self, other):
        return self.priorite < other.priorite
    def __le__(self, other):
        return self.priorite <= other.priorite
    def __gt__(self, other):
        return self.priorite > other.priorite
    def __ge__(self, other):
        return self.priorite >= other.priorite

class Graph:
    def __init__(self):
        self.sommets = []

G = Graph()

a = Noeud("A")
b = Noeud("B")
c = Noeud("C")
d = Noeud("D")
e = Noeud("E")

a.voisins.append(b)
a.voisins.append(d)
a.voisins.append(c)
b.voisins.append(a)
b.voisins.append(c)
c.voisins.append(a)
c.voisins.append(b)
c.voisins.append(d)
d.voisins.append(a)
d.voisins.append(c)
d.voisins.append(e)
e.voisins.append(d)

w = {
    (a, b): 1,
    (a, c): 7,
    (a, d): 18,
    (b, a): 1,
    (b, c): 3,
    (c, a): 7,
    (c, b): 3,
    (c, d): 2,
    (d, a): 18,
    (d, c): 2,
    (d, e): 10,
    (e, d): 10
    }

G.sommets.append(a)
G.sommets.append(b)
G.sommets.append(c)
G.sommets.append(d)
G.sommets.append(e)

T = Prim(G, w, a)

for e in T:
    for v in e:
        print(str(v), end="")
    print(",")


