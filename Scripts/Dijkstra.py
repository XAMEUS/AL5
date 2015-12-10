from FilePriorite import FilePriorite
def Dijkstra(G, w, s):
	inf = float("inf")
	H = FilePriorite()
	T = []
	s.priorite = 0;	H.inserer(0, s)
	for u in G.sommets:
		u.pred = None
		if u != s :
			H.inserer(inf, u)
			u.priorite = inf
	while not H.is_empty():
		p, u = H.pop_min()
		if u.priorite != inf:
			if u.pred is not None: T.append((u.pred, u))
			for v in u.voisins:
				if v.idx is not None: #v n'est pas sorti du tas
					if u.priorite + w[(u, v)] < v.priorite:
						v.priorite = u.priorite + w[(u, v)]
						H.diminuer_cle(v.idx, v.priorite)
						v.pred = u
	return T