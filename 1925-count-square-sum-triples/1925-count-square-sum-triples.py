class Solution:
    def countTriples(self, n: int) -> int:
        sets= set()
        for i in range(1, n+1):
            for j in range(1,i):
                sqr = i**2 + j**2
                if  sqr<= n**2 and sqrt(sqr) == int(sqrt(sqr)):
                    sets.add((i, j, math.sqrt(sqr)))
                    sets.add((j, i, math.sqrt(sqr)))
        return len(sets)
