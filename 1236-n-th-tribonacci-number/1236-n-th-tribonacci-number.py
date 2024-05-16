class Solution:
    def tribonacci(self, n: int) -> int:
        # memo={}
        # def rec(n):
        #     if n<2:
        #         return n
        #     if n==2:
        #         return 1
        #     if n not in memo:
        #         memo[n]=rec(n-1)+rec(n-2)+rec(n-3)
        #     return memo[n]
        # return rec(n)

        #Bottom up
        arr=[0,1,1]
        for i in range(3,n+1):
            arr.append(arr[i-3]+arr[i-1]+arr[i-2])
        return arr[n]