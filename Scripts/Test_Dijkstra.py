
class Noeud:
	def __init__(self, val):
		self.val = val
		self.voisins = list()
		self.couleur = "blanc"
		self.priorite = 0
		self.pred = None
		self.idx = 0
	def __str__(self):
		return "Noeud(" + str(self.val) + ")"

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
a.voisins.append(c)
b.voisins.append(a)
b.voisins.append(c)
b.voisins.append(d)
b.voisins.append(e)
c.voisins.append(a)
c.voisins.append(b)
c.voisins.append(d)
c.voisins.append(e)
d.voisins.append(b)
d.voisins.append(c)
d.voisins.append(e)
e.voisins.append(b)
e.voisins.append(c)
e.voisins.append(d)

w = {
	(a, b): 4,
	(a, c): 12,
	(b, a): 4,
	(b, c): 7,
	(b, d): 6,
	(b, e): 2,
	(c, a): 12,
	(c, b): 7,
	(c, d): 3,
	(c, e): 3,
	(d, b): 6,
	(d, c): 3,
	(d, e): 1,
	(e, b): 2,
	(e, c): 3,
	(e, d): 1,
}

G.sommets.append(a)
G.sommets.append(b)
G.sommets.append(c)
G.sommets.append(d)
G.sommets.append(e)

from Dijkstra import Dijkstra
T = Dijkstra(G, w, a)
for e in T:
	for v in e:
		print(str(v), end="")
	print(",")