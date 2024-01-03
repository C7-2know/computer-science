class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        summ=sum(skill)
        skil=summ*2/len(skill)
        left=0
        right=len(skill)-1
        out=0
        while left<right:
            if skill[left]+skill[right]==skil:
                out+=(skill[left]*skill[right])
                left+=1
                right-=1
            else:
                return -1
        return out