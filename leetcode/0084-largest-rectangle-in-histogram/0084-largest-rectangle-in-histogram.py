class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # when a lesser element comes we pop the element at the top and calculate the max area = we substract (new element's index - the index of the element being popped) * value
        # after we pop all elements the index of the new element will be changed to the last element's index (which is popped)
        # then we append the element to the stack
        # after all this when we finish iterating through the list we may have element in our stack that were not popped because there were no elements lesser than them at the right of them 
        # so inorder to get the max area they form 
        # we pop each of them and multiply them with the (top element's index + 1 - their index ) * value

        stack = []
        max_area = 0
        for i in range(len(heights)):
            idx = i
            while stack and stack[-1][1] > heights[i]:
                popped = stack.pop()
                idx = popped[0]
                max_area = max(max_area, (i - idx) * popped[1])

            stack.append([idx, heights[i]])

        if stack:
            idx = len(heights) - 1
        while stack:
            popped = stack.pop()
            max_area = max(max_area, (idx - popped[0] + 1) * popped[1])
        return max_area
