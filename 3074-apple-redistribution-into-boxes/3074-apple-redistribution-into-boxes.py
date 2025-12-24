class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        capacity.sort(reverse = True)
        tot = sum(apple)
        i=0
        while tot>0:
            tot-= capacity[i]
            i+=1
        return i