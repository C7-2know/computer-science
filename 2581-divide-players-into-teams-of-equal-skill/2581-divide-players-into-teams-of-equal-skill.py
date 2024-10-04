class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        com=skill[0]+skill[len(skill)-1]
        i,j=0,len(skill)-1
        ans=0
        while i<j:
            mul=skill[i]+skill[j]
            if mul!=com:
                return -1
            ans+=(skill[i]*skill[j])
            i+=1
            j-=1
        return ans