class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        answer = []

        even_sum = 0
        for j in nums:
            if j % 2 == 0:
                even_sum += j
     
        for i in range(len(queries)):
            
            if nums[queries[i][1]] % 2 == 0:
                even_sum -= nums[queries[i][1]]
            nums[queries[i][1]] = queries[i][0] + nums[queries[i][1]]
            if nums[queries[i][1]] % 2 == 0:
                even_sum += nums[queries[i][1]]
               
            
            answer.append(even_sum) 

            
        return answer
       