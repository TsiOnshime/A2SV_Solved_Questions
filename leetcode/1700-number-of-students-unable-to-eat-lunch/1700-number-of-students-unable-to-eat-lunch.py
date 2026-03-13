class Solution:
    def countStudents(self, students, sandwiches):
        # [1,1,0,0]
        #  i
        # [1,1,0,0,1]
        #      i
        j = 0
        i = 0
        count = 0
        while j < len(sandwiches):
            if students[i] == sandwiches[j]:
                j += 1
                
                count = 0
            else:
                count += 1
                students.append(students[i])
            if count == len(sandwiches) - j:
                return count
            i += 1
        return 0
