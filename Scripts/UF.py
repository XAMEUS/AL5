class UF:
    def __init__(self, U):
        self.Id = {}
        for x in U:
            self.Id[x] = x
    def root1(self, u):
        while self.Id[u] != u:
            u = self.Id[u]
        return u
    def find1(self, u, v):
        return self.root1(u) == self.root1(v)
    def union1(self, u, v):
        if not self.find1(u, v):
            chefu = self.root1(u)
            chefv = self.root1(v)
            self.Id[chefu] = chefv
