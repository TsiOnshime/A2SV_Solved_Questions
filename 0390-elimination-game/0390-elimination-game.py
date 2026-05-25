class Solution:
    def lastRemaining(self, n: int) -> int:
        # is all about mapping
        # at any point our number should be in range [1 - n]
        # so when we go from left to right we will always be left with even numbers since we start our elimination from odd number so the mapping could be 
        #      valid element    current element
        #           1               2
        #           2               4
        #           3               6
        # to make our recurssion easier we will use the valid elements but when we come back to it we should map the valid elements to the actual elements and we do that by 2 * validElem

        # when we go from right to left though things change since n could be odd or even
        # if it is odd we will be left with the even elements for which we can simply use the earlier mapping 2 * validElem
        # if it is even since we start eliminating from even numbers we will be left with odd numbers 
        #      valid element        current element
        #           1                   1
        #           2                   3
        #           3                   5

        # to get the current element from the valid element we would have to do (2 * validElem) - 1
        def last(n, left):
            if n == 1:
                return 1
            
            if left:
                return 2 * last(n // 2, False)
            else:
                if n % 2:
                    return 2 * last(n // 2, True)
                else:
                    return 2 * last(n // 2, True) - 1


        
        return last(n, True)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna