class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        ans=[]
        start,end=0,n
        for i in range(m):
            if end>len(original):
                return []
            ans.append(original[start:end])
            start=end
            end+=n
        if start<len(original):
            return []
        return ans