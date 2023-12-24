class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        dec=False
        if len(arr)<3:
            return False
        if arr[0]>arr[1]:
            return False
        for i in range(1,len(arr)):
            if arr[i]<arr[i-1]:
                dec=True
                continue
            elif arr[i]>arr[i-1] and dec==False:
                continue
            else:
                return False
        return dec