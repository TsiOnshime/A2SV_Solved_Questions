class Solution:
    def celebrity(self, mat):
        
        top, bottom = 0, len(mat) - 1
        
        while top < bottom:
            if mat[top][bottom] == 1:
                top += 1
            elif mat[bottom][top] == 1:
                bottom -= 1
            else:
                top += 1
                bottom -= 1
        if top > bottom:
            return -1
        for i in range(len(mat)):
            if mat[top][i] == 1 and i != top:
                return -1
            if mat[i][top] != 1:
                return -1
        return top
                
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna