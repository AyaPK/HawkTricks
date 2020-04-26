import trickGenerator as trick
import tweet as twitter

send = trick.generate()
print(send)
twitter.writeTweet(send)
