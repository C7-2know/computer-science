class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        lists=[(nums[j][i],j) for j in range(len(nums)) for i in range(len(nums[j]))]
        lists.sort()
        min_=lists[len(lists)-1][0]-lists[0][0]
        wind={i:0 for i in range(len(nums))}
        inds=set()
        left,right=0,len(lists)-1
        l=0
        for i in range(len(lists)):
            inds.add(lists[i][1])
            wind[lists[i][1]]+=1
            while len(inds)==len(nums):
                if min_>lists[i][0]-lists[l][0]:
                    min_=lists[i][0]-lists[l][0]
                    left=l
                    right=i
                wind[lists[l][1]]-=1
                if wind[lists[l][1]]==0:
                    inds.remove(lists[l][1])
                l+=1
        return [lists[left][0],lists[right][0]]
                    
