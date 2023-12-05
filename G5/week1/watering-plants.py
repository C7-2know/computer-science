class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        
        amount=capacity
        steps=0
        for i in range(len(plants)-1):
            steps+=1
            amount=amount-plants[i]
            if amount<plants[i+1]:
                steps+=2*(i+1)
                amount=capacity
            if len(plants)-1==i+1:
                steps+=1        
        return steps
