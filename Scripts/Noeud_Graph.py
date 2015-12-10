class Noeud:
	def __init__(self, val, voisins=[]):
		self.val = val
		self.voisins = voisins
		self.couleur = "blanc"
		self.dist = 0