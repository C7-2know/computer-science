class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left, right= 0, len(arr)-1
        while left<right:
            mid=(left+right)//2
            if arr[mid]<x:
                left=mid+1
            else:
                right=mid
        left=right-1
        while k>0:
            if right>=len(arr):
                left-=1
            elif left<0:
                right+=1
            elif left>=0 and abs(arr[left]-x)<abs(arr[right]-x):
                left-=1
            elif right <len(arr) and abs(arr[left]-x)>abs(arr[right]-x):
                right+=1
            else:
                if arr[left]<arr[right]:
                    left-=1
                else:
                    right+=1
            k-=1
        return arr[left+1:right]



            
