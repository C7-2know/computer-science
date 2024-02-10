class Solution:
    def bestClosingTime(self, customers: str) -> int:
        c_time=-1
        total=0
        max_=0
        for i in range(len(customers)):
            if customers[i]=='Y':
                total+=1
            else:
                total-=1
            if total>max_:
                c_time=i
                max_=total
                # print(total)
        return c_time+1