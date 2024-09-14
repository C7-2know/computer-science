class Solution:
    def minimumXORSum(self, nums1: List[int], nums2: List[int]) -> int:
        visited='0'*len(nums1)
        count=0
        memo={}
        def dp(i):
            nonlocal visited,count,memo
            if count>=len(nums1):
                return 0
            min_=float('inf')
            for j in range(len(nums1)):
                if visited[j]=="0":
                    visited=visited[:j]+"1"+visited[j+1:]
                    count+=1
                    if (i,j,visited) not in memo:
                        memo[(i,j,visited)]=(nums1[i]^nums2[j])+dp(i+1)
                    min_=min(min_,memo[(i,j,visited)])
                    count-=1
                    visited=visited[:j]+"0"+visited[j+1:]
            return min_
        
        min_=dp(0)
        return min_