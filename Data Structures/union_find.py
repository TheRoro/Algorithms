
class DisjointSet:
    def __init__(self, n):
        self.id = [-1]*n

    def find(self, a):
        if self.id[a] >= 0:
            grandpa = self.find(self.id[a])
            self.id[a] = grandpa
            return grandpa

        return a

    def union(self, a, b):
        parentA = self.find(a)
        parentB = self.find(b)
        if parentA == parentB:
            return

        if -self.id[parentA] < -self.id[parentB]:
            self.id[parentB] += self.id[parentA]
            self.id[parentA] = parentB
        else:
            self.id[parentA] += self.id[parentB]
            self.id[parentB] = parentA