def pere(i):
	return i//2
def gauche(i):
	return 2*i
def droite(T, i):
	return 2*i+1

def entasser_max(T, i):
	m, l, r = i, gauche(i), droite(i)
	if l < len(T) and T[l] > T[i] : m = l
	if r < len(T) and t[r] > T[m] : m = r
	if m != i:
		T[i], T[m] = T[m], T[i]
		entasser_max(T, m)

def pop_max(F):
	m = F[0]
	F[0] = F.pop()
	entasser_max(F, 0)
	return m

def augmenter_cle(F, i, cle):
	if cle < F[i]: return
	F[i] = cle
	while i > 0 and F[pere(i)] < F[i]:
		F[i], F[pere(i)] = F[pere(i)], F[i]
		i = pere(i)

def inserer_cle(F, cle):
	F.append(-1)
	augmenter_cle(F, len(F)-1, cle)