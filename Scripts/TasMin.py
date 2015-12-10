def pere(i):
	return i//2
def gauche(i):
	return 2*i
def droite(i):
	return 2*i+1

def entasser_min(T, i):
	m, l, r = i, gauche(i), droite(i)
	if l < len(T) and T[l] > T[i] : m = l
	if r < len(T) and T[r] > T[m] : m = r
	if m != i:
		T[i], T[m] = T[m], T[i]
		entasser_min(T, m)

def pop_min(F):
	m = F[0]
	F[0] = F.pop()
	entasser_min(F, 0)
	return m

def diminuer_cle(F, i, cle):
	if cle > F[i]: return
	F[i] = cle
	while i >= 1 and F[pere(i)] > F[i]:
		F[i], F[pere(i)] = F[pere(i)], F[i]
		i = pere(i)

def inserer_cle(F, cle):
	F.append(float("inf"))
	diminuer_cle(F, len(F)-1, cle)

F = []
inserer_cle(F, 50)
inserer_cle(F, 12)
inserer_cle(F, 3)
inserer_cle(F, 514)
inserer_cle(F, 17)
print(F)
