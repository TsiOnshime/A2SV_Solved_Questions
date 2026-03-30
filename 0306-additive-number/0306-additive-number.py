class Solution:
    def isAdditiveNumber(self, num):
        if len(num) <= 2:
            return False
        length = 0
        state = []
        def solve():
            
            return search(0)

        def is_valid_state(i):
            if state[-3] + state[-2] > state[-1] or state[-3] + state[-2] < state[-1]:
                return False
            else:
                return True


            

        def get_candidates(i):
            res = []

            for j in range(i, len(num) + 1):
                if i == j:
                    continue
                if num[i:j].startswith('0') and len(num[i:j]) > 1:
                    continue
                
                res.append(int(num[i:j]))
            return res
        def search(length):
            
            if len(state) >= 3 and not is_valid_state(length):
                return False
            if length == len(num):
                return len(state) >= 3
            

            for candidate in get_candidates(length):
                length += len(str(candidate))
                
                state.append(candidate)
                if search(length):
                    return True
                length -= len(str(candidate))
                state.pop()
        if solve():
            return True
        return False


    
o = Solution()
print(o.isAdditiveNumber("112358"))