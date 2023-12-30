class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        mx=max(costs)
        arr=[0 for i in range(mx+1)]
        for i in costs:
            arr[i]+=1
        cos=0
        ln=0
        # print(arr)
        for j in range(len(arr)):
            if cos+j>coins:
                break
            for k in range(arr[j]):
                if cos+j>coins:
                    break
                cos+=j
                ln+=1
        return ln
            