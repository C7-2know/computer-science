class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        front=[0]
        dc={nums[0]:[0,1]}
        for i in range(1,len(nums)):
            if nums[i] in dc:
                ind=dc[nums[i]][0]
                c=dc[nums[i]][1]
                front.append((i-ind)*c+front[ind])
                dc[nums[i]]=[i,c+1]
            else:
                front.append(0)
                dc[nums[i]]=[i,1]
        back=[0 for i in range(len(nums))]
        dc={nums[-1]:[len(nums)-1,1]}
        for j in range(len(nums)-2,-1,-1):
            if nums[j] in dc:
                ind=dc[nums[j]][0]
                c=dc[nums[j]][1]
                back[j]=(ind-j)*c+back[ind]
                dc[nums[j]]=[j,c+1]
            else:
                back[j]=0
                dc[nums[j]]=[j,1]
        for k in range(len(front)):
            front[k]+=back[k]
        return front