class Solution:
    def decodeString(self, s: str) -> str:

# when we find an openning bracket we recurssively call
# the next function
# wehn we get ]
        def decode(i):
            result = ""
            k = 0
            
            while i < len(s):
                if s[i].isdigit():
                    k = k * 10 + int(s[i])
                
                elif s[i] == '[':
                    sub, i = decode(i + 1)
                    result += sub * k
                    k = 0
                
                elif s[i] == ']':
                    return result, i
                
                else:
                    result += s[i]
                
                i += 1
            
            return result, i
        
        return decode(0)[0]
            

            






















        # stack = []

        # for i in range(len(s)):
        #     if s[i] != "]":
        #         stack.append(s[i])
        #     else:
        #         substring = ""
        #         while stack[-1] != "[":
        #             substring = stack.pop() + substring
        #         stack.pop()

        #         k = ""
        #         while stack and stack[-1].isdigit():
        #             k = stack.pop() + k

        #         stack.append(int(k) * substring)
        
        # return "".join(stack)
            
                    