class Twitter:

    def __init__(self):
        self.followers = dict()
        self.following = dict() # {followee_id : [follower_id]}
        self.tweets = dict() # {userId: tweetId}
        self.time = 1

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId in self.tweets.keys():
            self.tweets[userId].append([self.time, tweetId])
        else:
            self.tweets[userId] = [[self.time, tweetId]]
        self.time += 1


    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        userTweets = []
        if userId in self.tweets.keys():
            userTweets.extend(tweet for tweet in self.tweets[userId])
        otherTweets = []
        if userId in self.following.keys():
            for user in self.following[userId]:
                otherTweets.extend(self.tweets[user])
        combinedTweets = userTweets + otherTweets
        print(combinedTweets)
        recentTweets = [[-x[0], x[1]] for x in combinedTweets]
        heapq.heapify(recentTweets)
        while recentTweets and len(res) != 10:
            res.append(heapq.heappop(recentTweets)[1])
        return res

        
    def follow(self, followerId: int, followeeId: int) -> None:
        if followeeId == followerId:
            return
        if followeeId in self.followers.keys():
            if followerId not in self.followers[followeeId]:  
                self.followers[followeeId].append(followerId)
        else:
            self.followers[followeeId] = [followerId]
            
        if followerId in self.following.keys():
            if followeeId not in self.following[followerId]:
                self.following[followerId].append(followeeId)
        else:
            self.following[followerId] = [followeeId]  

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId == followerId:
            return           
        if followerId in self.followers[followeeId]:
            self.followers[followeeId].remove(followerId)
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)
              

        

        
