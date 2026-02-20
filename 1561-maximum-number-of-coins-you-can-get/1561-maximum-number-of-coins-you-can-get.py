class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        tri = len(piles) // 3
        alice_me = piles[tri:]
        
        
        choice = 0

        for i in range(0, len(alice_me), 2):
            choice += alice_me[i]
        return choice




        # print(tri)
        # choice = 0

        # start = 0
        # end = 2

        # for i in range(tri):
        #     choice += (sorted(piles[start:end + 1])[1])

        #     start = end + 1
        #     end = start + 2
        # return choice