class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        name_height = list(zip(names, heights))


        for i in range(len(heights)):
            j = 0
            while j + 1 < len(heights):
                if heights[j] > heights[j + 1]:
                    heights[j], heights[j + 1] = heights[j + 1], heights[j]
                j += 1
        heights = heights[::-1]

        names_new = []
        for i in heights:
            for name, age in name_height:
                if age == i:
                    names_new.append(name)

        return names_new
            
