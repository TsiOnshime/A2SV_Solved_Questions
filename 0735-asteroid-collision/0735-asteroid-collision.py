class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        

        stack = []

        for i in range(len(asteroids)):
            incoming = asteroids[i]
            while stack and incoming < 0 and stack[-1] >= 0:
                outgoing = stack[-1]

                if abs(incoming) > abs(outgoing):
                    stack.pop()
                elif abs(incoming) < abs(outgoing):
                    break
                else:
                    stack.pop()
                    break
            else:
                stack.append(incoming)

        return stack

                

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna