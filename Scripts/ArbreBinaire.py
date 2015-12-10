class ArbreBinaire:
    # par convention ArbreVide = None
    def __init__(self, v, g=None, d=None):
        self.val = v
        self.gauche = g 
        self.droite = d