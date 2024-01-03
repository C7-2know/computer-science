class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        right=len(people)-1
        left=0
        boats=0
        while left<=right:
            weight=people[right]+people[left]
            if weight<=limit:
                boats+=1
                right-=1
                left+=1
            else:
                boats+=1
                right-=1
            # print(boats)
        return boats
