from PriorityQueue import PriorityQueue
def Prim(G, w, s):
	inf = float("inf")
	H = PriorityQueue()
	T = []
	s.priorite = 0
	H.add_task(s, 0)
	i = 1
	for u in G.sommets:
		u.pred = None
		if u != s :
			H.add_task(u, inf)
			u.priorite = inf
	try:
		while True:
			u = H.pop_task()
			u.couleur = "noir"
			if u.priorite != inf:
				if u.pred is not None: T.append((u.pred, u))
				for v in u.voisins:
					if v.couleur == "blanc": #v n'est pas sorti du tas
						if w[(u, v)] < v.priorite:
							v.priorite = w[(u, v)]
							H.add_task(v, v.priorite)
							v.pred = u
	except:
		pass
	return T