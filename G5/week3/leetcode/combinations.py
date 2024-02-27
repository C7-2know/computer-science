class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # ans=[]
        # for i in range(1,n+1):
        #     j=i
        #     while j<n:
        #         re=[i]
        #         for z in range(k-1):
        #             re.append(j+1)
        #             j+=1
        #         ans.append(re)
        # return ans
        ans=[]
        def combine(cand):
            if len(cand)==k:
                ans.append(cand[:])
                print(cand)
            last=cand[-1] if cand else 0
            for next in range(last+1,n+1):
                cand.append(next)
                # print(cand)
                combine(cand)
                cand.pop()
        combine([])
        return ans
            
