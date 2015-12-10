def BFS(S):
    t = 0 ; S.dist = 0; s.pred = None; s.couleur = "gris"
    Q = [S] # Queue
    S.debut = t; t += 1;
    while not(Q.vide()):
        noeud = Q.pop(0) # pop first
        noeud.couleur = "noir"
        noeud.fin = t; t += 1
        for v in noeud.voisins:
            if v.couleur == "blanc":
                v.pred = noeud
                v.dist = noeud.dist + 1
                v.debut = t; t += 1
                v.couleur = "gris"
                Q.push(v) #push last