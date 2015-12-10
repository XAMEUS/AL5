def DFS(S, t = 0):
    S.couleur = "gris"; S.debut = t; t += 1
    for v in A.fils:
    	if v.couleur == "blanc":
    		v.pred = S
	        t = DFS(v, t)
    S.couleur = "noir"; S.fin = t; t += 1
    return t