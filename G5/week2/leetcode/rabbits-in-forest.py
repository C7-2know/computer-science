class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        set_={}
        number=0
        for i in answers:
            set_[i]=set_.get(i,0)+1
        for j in set_:
            amt=set_[j]/(j+1)
            number+=(math.ceil(amt)*(j+1))
        return number
