class Solution:
    def climbStairs(self, n: int) -> int:
        store={1:1,2:2}
        def climb(n):
            if n<=2:
                return n
            if n not in store:
                store[n]=climb(n-2)+climb(n-1)
            return store[n]
            # r=n-l
            # if l>=r:
            #     return store[l]
            # if r not in store:
            #     return store[r]
            # return store[r]
            # if l not in store:
            #     return store[l]
            # return store[r]
            # l=climb(l,r)
            # r=climb(l,r)
            # return store[n]
        return climb(n)
        