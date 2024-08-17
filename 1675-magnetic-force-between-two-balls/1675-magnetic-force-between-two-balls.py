class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        def helper(gap):
            st=position[0]
            count=1
            max_=float('inf')
            for p in position:
                if p-st>=gap:
                    count+=1
                    # print(gap,count)
                    st=p
            return count>=m
        ans=0
        mx,mn=position[-1],0
        while mn<mx:
            mid=(mx+mn)//2
            if helper(mid+1):
                # print(mid,'here')
                mn=mid+1
            else:
                mx=mid
        return mn