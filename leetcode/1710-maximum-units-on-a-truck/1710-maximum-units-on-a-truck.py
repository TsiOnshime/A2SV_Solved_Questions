class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        max_units = 0

        boxTypes.sort(key=lambda x: x[1], reverse=True)


        _max = 3
        for i in range(len(boxTypes)):
            boxes, units = boxTypes[i]

            if boxes <= truckSize:
                max_units += (units * boxes)
                truckSize -= boxes
            else:
            
                max_units += (units * truckSize)
                break
        
        return max_units

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna