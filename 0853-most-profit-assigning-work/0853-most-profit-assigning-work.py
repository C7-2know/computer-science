class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        total=0
        p1=len(difficulty)-1
        p2=len(worker)-1
        worker.sort()
        prof=list(zip(difficulty,profit))
        prof.sort(key=lambda x:x[1])
        print(prof)
        while p2>=0 and p1>=0:
            # print(difficulty[p1],worker[p2])
            if prof[p1][0]>worker[p2]:
                p1-=1
            else:
                total+=prof[p1][1]
                p2-=1
        return total