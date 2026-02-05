class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        set1 = set(list1)
        set2 = set(list2)
        common_strings = set1 & set2
        
        least_index_sum = float('inf')

        element_sum = {}

        for element in common_strings:
            element_sum[element] = list1.index(element) + list2.index(element)



        for key, value in element_sum.items():
            least_index_sum = min(least_index_sum, value)

        return [key for key, value in element_sum.items() if value == least_index_sum]
        