from UF import UF
class UF3(UF):
    def __init__(self, U):
        super(UF2, self).__init__(U)
        self.size = {}
        for x in U: self.size[x] = 0
    def find2(self, u, v):
        return self.root2(u) == self.root2(v)
    def root2(self, u):
        if self.Id[u] != u:
            self.Id[u] = self.root2(Id[u])
        return self.Id[u]
    def union2(self, u, v):
        ru = self.root2(u)
        rv = self.root2(v)
        if self.size[ru] < self.size[rb]:
            self.Id[ru] = self.Id[rv]
        else:
            self.Id[rv] = self.Id[ru]
        if self.size[ru] == self.size[rv]:
            self.size[ru] += 1