class MedianFinder:

    def __init__(self):
        self.half1=[]
        self.half2=[]
        heapify(self.half1)
        heapify(self.half2)

    def addNum(self, num: int) -> None:
        if self.half2:
            num1=heappop(self.half2)
            num2=float('-inf')
            if self.half1:
                num2=-1*heappop(self.half1)
            if num<=num2:
                heappush(self.half1,-1*num)
                heappush(self.half2,num1)
                if num2!=float('-inf'):
                    if len(self.half1)<len(self.half2)-1:
                        heappush(self.half1,-1*num2)
                    else:
                        heappush(self.half2,num2)
            elif num<num1:
                if num2!=float('-inf'):
                    heappush(self.half1,-1*num2)
                heappush(self.half2,num1)

                if len(self.half1)<len(self.half2)-1:
                    heappush(self.half1,-1*num)
                else:
                    heappush(self.half2,num)
            else:
                heappush(self.half2,num)
                if num2!=float('-inf'):
                    heappush(self.half1,-1*num2)
                if len(self.half1)<len(self.half2)-1:
                    heappush(self.half1,-1*num1)
                else:
                    heappush(self.half2,num1)
        else:
            heappush(self.half2,num)

    def findMedian(self) -> float:
        if len(self.half2)<1:
            return 0
        if (len(self.half1)+len(self.half2))%2!=0:
            mid=heappop(self.half2)
            heappush(self.half2,mid)
            return mid
        else:
            n1=heappop(self.half2)
            n2=heappop(self.half2)
            heappush(self.half2,n1)
            heappush(self.half2,n2)
            # print("n1,n2",n1,n2)
            mid=(n1+n2)/2
            return mid



# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()