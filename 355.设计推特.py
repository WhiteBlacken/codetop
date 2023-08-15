#
# @lc app=leetcode.cn id=355 lang=python3
#
# [355] 设计推特
#

# @lc code=start
import heapq
timestamp = 0
class Twitter:

    def __init__(self):
        self.userMap = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.userMap:
            self.userMap[userId] = User(userId)
        self.userMap[userId].postTweet(tweetId)


    def getNewsFeed(self, userId: int) -> List[int]:
        if userId not in self.userMap:
            return []
        res = []
        tweets = []
        for uid in self.userMap[userId].followerSet:
            if uid in self.userMap:
                tweets.append(self.userMap[uid].tweetList[:]) # 隐藏很深的错误
        heap = []
        for i, tweet in enumerate(tweets):
            if tweet:
                heapq.heappush(heap, (-tweet[-1].time, i))
        cnt = 10
        while cnt > 0 and heap:
            _, index = heapq.heappop(heap)
            res.append(tweets[index].pop().tweetId)
            if tweets[index]:
                heapq.heappush(heap, (-tweets[index][-1].time, index))
            cnt -= 1
        return res

        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.userMap:
            self.userMap[followerId] = User(followerId)
        self.userMap[followerId].follow(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.userMap:
            self.userMap[followerId] = User(followerId)
        if followeeId in self.userMap[followerId].followerSet:
            self.userMap[followerId].unfollow(followeeId)
        

class User:
    def __init__(self, userId) -> None:
        self.userId = userId
        self.tweetList = []
        self.followerSet = set()
        self.followerSet.add(userId)
    
    def postTweet(self, tweetId):
        global timestamp
        tweet = Tweet(tweetId, timestamp)
        timestamp += 1
        self.tweetList.append(tweet)
    
    def follow(self, followeeId):
        self.followerSet.add(followeeId)
    
    def unfollow(self, followeeId):
        if followeeId == self.userId: return
        self.followerSet.discard(followeeId)


class Tweet:
    def __init__(self, tweetId, time) -> None:
        self.tweetId = tweetId
        self.time = time


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
# @lc code=end

