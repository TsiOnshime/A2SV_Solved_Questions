class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        remove_duplicates = list(map(set, responses))

        print(remove_duplicates)
        count = defaultdict(int)
        
        for day in remove_duplicates:
            for response in day:
                count[response] += 1
      
            
        
            

        maxx = 0

        for key, value in count.items():
            maxx = max(maxx, value)
            

        if maxx == 0:
            return ''

        keys = sorted([key for key, value in count.items() if value == maxx])
        return keys[0]
         