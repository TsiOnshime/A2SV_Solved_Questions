class Solution:
    def findRestaurant(self, list1: list[str], list2: list[str]) -> list[str]:
        min_sum = float('inf')
        for i in range(len(list2)):
            list2[i] = [list2[i], i]
        list2.sort()
        res = []

        def find_word(word):
            l, r = 0, len(list2) - 1
            ans = float('inf')
            while l <= r:
                mid = l + (r - l)//2
                if list2[mid][0] == word:
                    ans = mid
                    r = mid - 1
                elif list2[mid][0] > word:
                    r = mid - 1
                else:
                    l = mid + 1
            return list2[ans][1] if ans < float('inf') else float('inf')

        for i in range(len(list1)):
            idx = find_word(list1[i])

            if idx == float('inf'):
                continue
            if idx + i < min_sum:
                res = [list1[i]]
                min_sum = idx + i
            elif idx + i == min_sum:
                res.append(list1[i])
            
        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna