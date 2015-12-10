def InsererABR(A, v):
	if v == A.val: raise Exception("v deja dans l'arbre")
	if v < A.val:
		if A.gauche is not None:
			InsererABR(A.gauche, v)
		else: A.gauche = ABR(v, None, None)
	if v > A.val:
		if A.droite is not None:
			InsererABR(A.droite, v)
		else: A.droite = ABR(v, None, None)