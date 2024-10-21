class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res=[]
        def bt(i,arr):
            if len(arr)>k:
                return []
            for j in range(i+1,n+1):
                arr.append(j)
                if len(arr)==k:
                    res.append(arr.copy())
                bt(j,arr)
                arr.pop()
        bt(0,[])
        return res