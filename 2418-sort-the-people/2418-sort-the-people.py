class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        name_height = list(zip(names, heights))


        for i in range(len(heights)):
            max_index = i
            
            for j in range(i + 1, len(heights)):
                
                if heights[max_index] < heights[j]:
                    heights[max_index], heights[j] = heights[j], heights[max_index]
                    
            max_index += 1
        print(heights)

        names_new = []
        for i in heights:
            for name, age in name_height:
                if age == i:
                    names_new.append(name)

        return names_new
            
