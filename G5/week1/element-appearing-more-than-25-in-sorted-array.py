class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        if len(arr)==1:
            return arr[0]
        for i in range(len(arr)):
            indx=len(arr)//4
            if arr[i]==arr[i+indx]:
                return arr[i]