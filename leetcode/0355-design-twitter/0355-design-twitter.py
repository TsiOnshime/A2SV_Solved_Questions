class Twitter:

    def __init__(self):
        self.followings = defaultdict(set) # follower: [followees]
        self.tweets = defaultdict(list) # user: [[time, tweetId]]
        self.time = 1
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append([-self.time, tweetId])  
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        min_heap = []
        res = []
        self.follow(userId, userId)
        for followee in self.followings[userId]:
            if followee in self.tweets:
                index = len(self.tweets[followee]) - 1
                time, tweetId = self.tweets[followee][index]
                min_heap.append([time, tweetId, index - 1, followee])
        
        heapq.heapify(min_heap)
        while min_heap and len(res) < 10:
            time, tweetId, index, followee = heapq.heappop(min_heap)
            res.append(tweetId)
            if index >= 0:
                time, tweetId = self.tweets[followee][index]
                heapq.heappush(min_heap, [time, tweetId, index - 1, followee])

        return res
            


    def follow(self, followerId: int, followeeId: int) -> None:
        self.followings[followerId].add(followeeId)

        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followings[followerId]:
            self.followings[followerId].remove(followeeId)


        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna