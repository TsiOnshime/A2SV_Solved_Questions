class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        x1, y1, x2, y2 = rec1
        a1, b1, a2, b2 = rec2

        # if rec1 is above rec2
        if b2 <= y1:
            return False
        # if rec1 is below rec2
        if b1 >= y2:
            return False
        
        # if rec1 is to the left of rec2
        if x2 <= a1:
            return False
        
        # if rec1 is to the right of rec2
        if a2 <= x1:
            return False
        
        return True


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna