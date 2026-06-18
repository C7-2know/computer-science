class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        sandwiches=sandwiches[::-1]
        while sandwiches:
            ls=sandwiches.pop()
            len_=len(students)
            for i in range(len_):
                if students[i]!=ls:
                    students.append(students[i])
                else:
                    break
            students=students[i+1:]
            if len(students)>len(sandwiches):
                return len(students)
            
        return 0
                    