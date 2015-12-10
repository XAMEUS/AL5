def BFS(A):
    t = 0 ; d = 0
    Q = [(A,0)] # Queue
    A.couleur = "gris";
    A.debut = t; t += 1
    while not(Q.vide()):
        noeud, d = Q.pop(0) # pop first
        noeud.couleur = "noir"
        noeud.fin = t
        t += 1
        for v in noeud.fils:
            v.couleur = "gris"
            v.debut = t; t += 1
            Q.append((v, d + 1)) # push last