from UF import UF
def Kruskal (G, w):
	T = []; cout = 0;
	A = G.A # l'ensemble des arretes de G
	S = sorted(A) # A trie selon w croissant
	for (u, v) in S:
		if not UF.find(u, v): # si (u, v) ne forme pas de cycle
			T.append((u, v))
			cout += w[(u, v)]
			UF.union(u, v)
	return (T, cout)