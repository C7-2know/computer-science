class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        count=Counter(ages)
        ages=list(set(ages))
        ages.sort()
        res=0
        for i in range(len(ages)):
            if ages[i]>(0.5*ages[i]+7):
                res+=(count[ages[i]]*(count[ages[i]]-1))
            j=i-1
            while j>=0:
                if ages[j]<=(0.5*ages[i]+7):
                    break
                res+=(count[ages[i]]*count[ages[j]])
                j-=1
        return res
