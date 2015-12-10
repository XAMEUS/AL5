def DFS(A, t = 0):
    A.couleur = "gris"; A.debut = t; t += 1
    for v in A.fils:
        t = DFS(A, t)
    A.couleur = "noir"; A.fin = t; t += 1
    return t