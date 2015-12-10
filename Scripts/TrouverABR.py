def TrouverABR(A, v):
	if v == A.val: return A
	elif v < A.val and A.gauche is not None:
		return TrouverABR(A.gauche, v)
	elif v > A.val and A.droite is not None:
		return TrouverABR(A.droite, v)
	return None