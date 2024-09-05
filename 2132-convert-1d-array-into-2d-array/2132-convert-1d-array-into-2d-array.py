class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        ans=[]
        st,end=0,n
        for i in range(m):
            if end>len(original):
                return []
            ans.append(original[st:end])
            st=end
            end+=n
        if st<len(original):
            return []
        return ans