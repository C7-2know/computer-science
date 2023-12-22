class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        arr=[i for i in range(1,n+1)]
        di={i for i in range(1,n+1)}
        i=0
        while n>1:
            i=(i+k-1)%n
            elm=arr.pop(i)
            # print(arr)
            n-=1

        return arr[0]
