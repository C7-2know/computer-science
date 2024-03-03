class Solution:
    def trap(self, height: List[int]) -> int:
        m_stack=[]
        water=0
        for i in range(len(height)):
            min_=float('-inf')
            while m_stack and m_stack[-1][0]<=height[i]:
                pre=m_stack.pop()
                if min_!=float('-inf') and min_<pre[0]:
                    c_hegh=min(pre[0],height[i])-min_
                    width=i-pre[1]
                    water+=(c_hegh*(width-1))
                min_=max(min_,pre[0])
            if m_stack and m_stack[-1][1]+2<=i and m_stack[-1][0]>height[i] and min!=float('inf'):
                c_hegh=min(m_stack[-1][0],height[i])-min_
                width=i-m_stack[-1][1]
                water+=(c_hegh*(width-1))
            m_stack.append([height[i],i])


        return water