class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        c5=0
        c10=0
        c20=0
        for i in range(len(bills)):
            change=bills[i]-5
            if (change/5)%5==0:
                c5+=1
            else:
                if c5==0 or (c5*5+c10*10)<change:
                    return False
                else:
                    c5-=1
                    change-=5
                    if change>0:
                        if c10!=0:
                            c10-=1
                            change-=10
                        if change>0:
                            c5-=(change/5)
                        if c5<0:
                            return False
                        c20+=1
                    else:
                        c10+=1
        return True 
