import trickGenerator as trick
import tweet

send = trick.generate()
print(send)
tweet.writeTweet(send)
