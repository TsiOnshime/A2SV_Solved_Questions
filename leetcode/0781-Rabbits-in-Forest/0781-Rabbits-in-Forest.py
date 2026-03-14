class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        # if a rabbit says there are zero other rabbits with the same colour as his doesn't exist
        # if he says 1 and he's blue it means there are two blue rabbits
        # what we can drive from this is if a rabbit says n that means including him there are n + 1 rabbits of that colour
        # so we count the number of rabbits each time we see the number
        # when count = n + 1 it means they have formed a group and we can add n + 1 to our answer and set the count to zero to count the other group of rabbits with the same colour
        rabbits = 0
        count = defaultdict(int)
        for i in range(len(answers)):
            count[answers[i]] += 1
            if count[answers[i]] == answers[i] + 1: #they have formed complete group
                rabbits += count[answers[i]]
                count[answers[i]] = 0
        # now its time to count rabbits that formed incomplete groups
        for key, value in count.items():
            if count[key] != 0:
                rabbits += (key + 1)
        return rabbits