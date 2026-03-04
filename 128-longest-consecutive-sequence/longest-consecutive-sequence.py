class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_=set(nums)
        seq=[]
        for num in set_:
            if num-1 in set_:
                continue
            seq.append([num])
        max_=0
        for i in range(len(seq)):
            st=seq[i][0]
            while st+1 in set_:
                seq[i].append(st+1)
                st+=1
            max_=max(max_, len(seq[i]))
        return max_
        