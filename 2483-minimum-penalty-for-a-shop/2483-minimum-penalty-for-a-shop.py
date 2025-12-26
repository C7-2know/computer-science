class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n, y = 0, 0
        for i in customers:
            if i =='N':
                n+=1
            else:
                y+=1
        tot_n, tot_y = n, y
        ind = 0
        penality = y
        for i in range(len(customers)+1):
            new_p = tot_n - n + y
            if new_p< penality:
                ind =i
                penality = new_p
            if i >= len(customers):
                continue
            if customers[i] == 'N':
                n-=1
            else:
                y-=1
        return ind
