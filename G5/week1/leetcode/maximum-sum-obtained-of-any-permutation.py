class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        dc={}
        l1=[0 for _ in range(len(nums))]
        for st,end in requests:
            l1[st]+=1
            if end+1<len(l1):
                l1[end+1]-=1
        for i in range(1,len(l1)):
            l1[i]+=l1[i-1]
            if l1[i] not in dc:
                dc[l1[i]]=[]
            dc[l1[i]].append(i)
        nums.sort()
        l1.sort()
        total=0
        for k in range(len(nums)):
            total+=nums[k]*l1[k] 
        return total%(10**9 + 7)
        
