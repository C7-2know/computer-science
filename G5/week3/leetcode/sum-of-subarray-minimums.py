class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        stack=[]
        sum_=0
        dc={}
        arr.append(0)
        for i in range(len(arr)):
            count=0
            while stack and arr[stack[-1]]>arr[i]:
                ind =stack.pop()
                pop=0
                if ind in dc:
                    pop=dc[ind]
                sum_+=((arr[ind])*(i-ind)+arr[ind]*pop*(i-ind))
                count+=(1+pop)
            dc[i]=count
            stack.append(i)
        # while stack:
        #     pop=dc[stack[-1]]
        #     ln=i-stack[-1]+1
        #     sum_+=(ln*arr[stack[-1]]+pop*ln*arr[stack[-1]])
        #     stack.pop()
        return sum_%(10**9+7)