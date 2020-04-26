import trickGenerator as trick
import tweet as twitter

send = trick.generate()
twitter.writeTweet(send)
