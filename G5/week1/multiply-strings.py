class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        result=0
        for i in range(len(num2)-1,-1,-1):
            rem=0
            middle=''
            for j in range(len(num1)-1,-1,-1):
                mult=int(num1[j])*int(num2[i])
               
                mult+=rem
                rem=0
                print('mult',mult)
                if mult>=10 and j!=0:
                    rem=mult//10
                    mult=mult%10
                middle=str(mult)+middle
                print(mult,rem)
            result+=int(middle)*10**(len(num2)-i-1)
            print(middle,result)

        return str(result)
        # for i in range(len(num2)):
        #     row=''
        #     rem=0
        #     for j in range(len(num1)):
        #         mult=int(num1[j])*int(num2[i])
        #         if rem!=0:
        #             mult+=rem
        #             rem=0
        #         if mult>=10:
        #             rem=mult//10
        #             mult=mult%10
        #         res=str(mult)+res
        #     result+= int(res)*10**(len(num1))
        # result=0
        # for i in range(len(num2)-1,-1,-1):
        #     res=''
        #     rem=0
        #     for j in range(len(num2)-1,-1,-1):
        #         mult=int(num2[i])*int(num1[j])
        #         print(mult)
        #         if rem!=0:
        #            mult+=rem
        #            rem=0
        #         if mult>=10:
        #             if j!=len(num1)-1:
        #                 rem=mult//10
        #                 mult=mult%10
        #             print(rem,mult)
        #         res=str(mult)+res
        #         print('res',res)
        #     result=int(res)*10**(len(num2)-1-i)+result
        #     # print(i,result)
        #     # print(res)

        # return str(result)