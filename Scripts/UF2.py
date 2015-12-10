from UF import UF
class UF2(UF):
    def __init__(self, U):
        super(UF2, self).__init__(U)
        self.size = {}
        for x in U:
            self.size[x] = 0
    def union2(self, u, v):
        chefu = self.root1(u)
        chefv = self.root1(v)
        if self.size[chefu] > self.size[chefv]:
            self.Id[chefv] = chefu
        else:
            self.Id[chefu] = chefv
        if self.size[chefu] == self.size[chefv]:
            self.size[chefv] += 1