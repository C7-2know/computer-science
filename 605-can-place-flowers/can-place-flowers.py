class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        zeros=0 if flowerbed[0]==1 else 1
        ans=0
        for i in range(len(flowerbed)):
            if flowerbed[i]==1:
                if zeros%2==0 and zeros>0:
                    zeros-=1
                ans+=zeros//2
                zeros=0
            else:
                zeros+=1
        if zeros%2==0 and zeros>0 and flowerbed[-1]!=0:
            zeros-=1
        ans+=zeros//2
        return  ans>=n