class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        arr2=[]
        for num in nums:
            n=''
            for i in str(num):
                n+=str(mapping[int(i)])
            num=n
            arr2.append(int(n))
        zipd=list(zip(nums,arr2))
        zipd.sort(key=lambda x:x[1])
        res=[i[0] for i in (zipd)]
        print(arr2)
        return res

