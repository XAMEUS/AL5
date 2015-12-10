from heapq import heappush, heappop, heapreplace
def Prim(G, w, s):
	inf = float("inf")
	H = [] # heap
	T = []
	s.priorite = 0
	heappush(H, (0, s))
	i = 1
	for u in G.sommets:
		u.pred = None
		if u != s :
			heappush(H, (inf, u))
			u.priorite = inf
	while not len(H) == 0:
		p, u = heappop(H)
		u.couleur = "noir"
		if p != inf:
			if u.pred is not None: T.append((u.pred, u))
			for v in u.voisins:
				if v.couleur == "blanc": #v n'est pas sorti du tas
					if w[(u, v)] < v.priorite:
						v.priorite = w[(u, v)]
						heapreplace(H, (v.priorite, v))
						v.pred = u
	return T