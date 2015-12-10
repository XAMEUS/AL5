def DFS(S):
	pile = [S]; S.couleur = "gris"
	while not len(pile) == 0:
		next = pile[-1] # head
		for v in next.voisins:
			if v.couleur == "blanc":
				v.couleur = "gris"
				pile.push(v)
				break
		else:
			next.couleur = "noir"; pile.pop(-1)