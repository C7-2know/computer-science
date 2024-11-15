class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        left,right=1,len(arr)-1
        while left<len(arr) and arr[left]>=arr[left-1]:
            left+=1
        left-=1
        while right>0 and arr[right]>=arr[right-1]:
            right-=1
        if left>=right:
            return 0
        l=left
        max_=max(left+1,len(arr)-right)
        while l>=0:
            r=right
            while r<len(arr):
                if arr[l]<=arr[r]:
                    max_=max(max_,l+(len(arr)-r)+1)
                    break
                r+=1
            l-=1
        return len(arr)-max_