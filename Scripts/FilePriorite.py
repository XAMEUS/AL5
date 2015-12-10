class FilePriorite:
	def __init__(self):
		self.T = []
	def pere(self, i):
		return i//2
	def gauche(self, i):
		return 2*i
	def droite(self, i):
		return 2*i+1
	def entasser_min(self, i):
		m, l, r = i, self.gauche(i), self.droite(i)
		if l < len(self.T) and self.T[l][0] > self.T[i][0]: m = l
		if r < len(self.T) and self.T[r][0] > self.T[m][0]: m = r
		if m != i:
			self.T[i][1].idx, self.T[m][1].idx = self.T[m][1].idx, self.T[i][1].idx
			self.T[i], self.T[m] = self.T[m], self.T[i]
			self.entasser_min(m)
	def pop_min(self):
		m = self.T[0]
		if len(self.T) > 1:
			self.T[0] = self.T.pop()
			self.T[0][1].idx = 0
			self.entasser_min(0)
		else : self.T.pop()
		m[1].idx = None
		return m
	def diminuer_cle(self, i, cle):
		if cle > self.T[i][0]: return
		self.T[i][0] = cle
		while i >= 1 and self.T[self.pere(i)][0] > self.T[i][0]:
			self.T[i][1].idx, self.T[self.pere(i)][1].idx = self.T[self.pere(i)][1].idx, self.T[i][1].idx
			self.T[i], self.T[self.pere(i)] = self.T[self.pere(i)], self.T[i]
			i = self.pere(i)
	def inserer(self, k, v):
		v.idx = len(self.T)
		self.T.append([float("inf"), v])
		self.diminuer_cle(len(self.T)-1, k)
	def is_empty(self):
		return len(self.T) == 0