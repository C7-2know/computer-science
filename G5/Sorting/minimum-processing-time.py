class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        processorTime.sort(reverse=True)
        tasks.sort()
        time=[]
        for j in range(len(processorTime)):
            time.append(processorTime[j]+tasks[j+(j+1)*3])
        # print(time)
        return max(time)
