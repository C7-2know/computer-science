class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        prefix=[arr[0]]
        for i in range(1,len(arr)):
            prefix.append(prefix[-1]^arr[i])
        ans=[]
        for q in queries:
            bf=0
            if q[0]>0:
                bf=prefix[q[0]-1]
            ans.append(prefix[q[1]]^bf)
        return ans
