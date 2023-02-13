class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed) == 1 or len(changed) == 0: return []
        res = []
        changed.sort()
        frequency = Counter(changed)
        for num in changed:
            if frequency[num] :
                frequency[num] -= 1 #since there may be more than one number
                res.append(num)
                if frequency[num*2]:
                    frequency[num * 2] -= 1
                else:
                    return [] #if there is no doubled value of the number then return empty
        return res
        
