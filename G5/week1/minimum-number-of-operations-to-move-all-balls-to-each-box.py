class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        oper_arr=[]
        for i in range(len(boxes)):
            num_oper=0
            for j in range(len(boxes)):
                num_oper+=abs(i-j)*int(boxes[j])
            oper_arr.append(num_oper)
        return oper_arr