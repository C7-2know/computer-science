class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # nums.sort()
        # right=len(nums)-1
        # out=[]
        # outs=set()
        # dc={}
        # visited=set()
        # for j in range(len(nums)):
        #     if nums[j] not in dc:
        #         dc[nums[j]]=[]
        #     dc[nums[j]].append(j)
        # for i in range(len(nums)):
        #     dc[nums[i]].pop(0)
        #     while right>i and nums[i] not in visited:
        #         summ=nums[i]+nums[right]
        #         arr=[nums[i],nums[right],-1*summ]
        #         summT=(arr[0],arr[1],arr[2])
        #         # if nums[right-1]<(-1*summ):
        #         #     break
        #         if (-1*summ) in dc and summT not in outs:
        #             found=False
        #             for k in dc[-1*summ]:
        #                 if i<k<right:
        #                     found=True
        #                     break
        #             if found:
        #                 out.append(arr)
        #                 outs.add(summT)
        #         right-=1
        #     visited.add(nums[i])
        #     right=len(nums)-1
        # return out

        out=[]
        dc=set()
        visited=set()
        nums.sort()
        for k in range(len(nums)):
            i=k+1
            j=len(nums)-1
            opp=0-(nums[k])
            while i<j and nums[k] not in visited:
                summ=nums[i]+nums[j]
                if summ==opp:
                    if (nums[k],nums[i],nums[j]) not in dc:
                        out.append([nums[k],nums[i],nums[j]])
                        dc.add((nums[k],nums[i],nums[j]))
                    i+=1
                    j-=1
                elif summ<opp:
                    i+=1
                else:
                    j-=1
            visited.add(nums[k])
        return list(out)
            