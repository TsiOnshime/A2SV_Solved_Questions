class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:

        people.sort()

        l, r = 0, len(people)-1
        boats = 0

        while l <= r:
            if l == r:
                if people[l] <= limit:
                    boats += 1
                    l += 1

                else: 
                    break
            else:
                if people[l] + people[r] > limit:
                    r -= 1
                else:
                    l += 1
                    r -= 1
                boats += 1
        return boats
        