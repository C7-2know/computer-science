class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack=[]
        ans=[-1 for i in range(len(nums))]
        queue=deque()
        for i in range(len(nums)):
            while stack and nums[stack[-1]]<nums[i]:
                ans[stack[-1]]=nums[i]
                # queue.appendleft(stack[-1])
                stack.pop()
            stack.append(i)
            queue.append(i)
        while stack and queue:
            if nums[stack[-1]]>=nums[queue[0]]:
                queue.popleft()
            elif stack[-1]<queue[0]:
                break
            else:
                ans[stack[-1]]=nums[queue[0]]
                stack.pop()

        return ans

        # inc_q=deque()
        # ans=[0]*len(nums)
        # for i in range(len(nums)):
        #     while inc_q and nums[inc_q[-1][0]]<nums[i] and inc_q[-1][1]==-1:
        #         print(inc_q)
        #         pop=inc_q.pop()
        #         ind=pop[0]
        #         ans[ind]=nums[i]
        #         inc_q.appendleft([ind,nums[i]])
        #     inc_q.append([i,-1])
        # for i in range(len(ans)):
        #     if  ans[i]==0:
        #         while inc_q and inc_q[]
        # print(ans)
        # return ans