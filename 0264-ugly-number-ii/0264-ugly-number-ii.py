class Solution:
    def nthUglyNumber(self, n: int) -> int:
        nums=[2,3,5]
        ans=set([1])
        while len(ans)//4<n:
            ls=list(ans)
            for j in nums[::-1]:
                for i in ls:
                    ans.add(j*i)
        print(ans)
        ans=list(ans)
        ans.sort()
        print(ans)
        return (ans[n-1])


        