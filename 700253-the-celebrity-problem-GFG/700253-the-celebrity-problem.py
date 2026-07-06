class Solution:
    def celebrity(self, mat):
        
        knowme = [0] * len(mat[0])
        iknow = [0] * len(mat[0])
        
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 1:
                    knowme[j] += 1
                    iknow[i] += 1
        for i in range(len(mat)):
            if knowme[i] == len(mat) and iknow[i] == 1:
                return i
        return -1
                
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna