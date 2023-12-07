class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candy=max(candies)
        new_arr=[]
        for i in range(len(candies)):
            if candies[i]+extraCandies>=max_candy:
                new_arr.append(True)
            else:
                new_arr.append(False)
        return new_arr
        