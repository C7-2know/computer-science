class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        tot=sum(chalk)
        k=k-(k//tot)*tot
        for i in range(len(chalk)):
            if k-chalk[i]<0:
                return i
            k-=chalk[i]

