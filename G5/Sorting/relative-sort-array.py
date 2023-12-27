class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        # dc={}
        # for i in range(len(arr2)):
        #     dc[arr2[i]]=i
        # count={}
        # arr3=[]
        # for k in arr1:
        #     count[k]=count.get(k,0)+1
        #     if k not in dc:
        #         arr3.append(k)
        # k=0
        # arr=[0 for i in range(len(arr1))]
        # for i in arr2:
        #     for j in range(count[i]):
        #         arr[k]=i
        #         k+=1
        # arr3.sort()
        # for i in arr3:
        #     arr[k]=i
        #     k+=1
        # return arr

        enum=(list(enumerate(arr2)))
        dc={}
        for j in range(len(arr2)):
            dc[arr2[j]]=j
        arr3=[]
        for i in range(len(arr1)):
            if arr1[i] not in dc:
                arr3.append(arr1[i])
        arr3.sort()
        for i in range(len(arr3)):
            dc[arr3[i]]=len(arr2)+i
        def index(item):
            return dc[item]
        arr1.sort(key=lambda a:index(a))
        return(arr1)