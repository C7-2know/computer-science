class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        mx=max(arr)
        mx_num=1
        flips=[]
        ls=len(arr)-1
        while ls>0:
            # print(flips,arr)
            indx=arr.index(mx)
            if indx==ls:
                mx=max(arr[:indx])
                ls-=1
                continue 
            if indx!=0:
                k=indx+1
                flips.append(k)
                rev=arr[:indx+1][::-1]
                arr=rev+arr[indx+1:]

            arr=arr[:ls+1][::-1]+arr[ls+1:]
            flips.append(ls+1)
            mx=max(arr[:ls])
            ls-=1
            print(flips,arr,'max',mx)
        return flips