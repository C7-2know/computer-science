class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        max_=0
        pick1=0
        if len(arr)<3:
            return 0
        i=0
        if arr[i]<arr[i+1]:
            pick1=0
            i+=1
        else:
            i+=1
            while i<(len(arr)-1):
                if arr[i]<=arr[i-1] and arr[i]<arr[i+1]:
                    pick1=i
                    i+=1
                    break
                i+=1
        pick2=0
        while i<len(arr)-1:
            if arr[i]==arr[i-1]:
                pick2=0
                pick1=i
            if arr[i]>arr[i-1] and arr[i]>arr[i+1]:
                pick2=i
            elif arr[i]<=arr[i-1] and arr[i]<arr[i+1]:
                if pick2!=0:
                    max_=max(max_, i-pick1+1)
                pick2=0
                pick1=i
            if pick2!=0:
                max_=max(max_,i-pick1+1)
            i+=1
        print(pick1, pick2)
        if pick2!=0 and arr[-1]<arr[pick2]:
            max_=max(max_,len(arr)-pick1)
        return max_
            
            


                   