# import tweepy as tw
# import schedule
import re
import json

jsonData = open("Programs/Auto Post/config.json")

data = json.load(jsonData)

consumer_key = data['twitter']['consumer_key']
consumer_secret = data['twitter']['consumer_secret']
access_key = data['twitter']['access_key']
access_secret = data['twitter']['access_secret']

quotes = open("/Users/alexjshepler/Desktop/Epoch Industry/Programs/Auto Post/tweets/new.txt", 'r+')

try:
    previous = open("/Users/alexjshepler/Desktop/Epoch Industry/Programs/Auto Post/tweets/prev.txt", 'x')
except:
    previous = open("/Users/alexjshepler/Desktop/Epoch Industry/Programs/Auto Post/tweets/prev.txt", 'r+')


try:
    # Sets the sets the last tweet to the last entry in the previous file
    lastTweet = previous.readlines()[-1]
except:
    lastTweet = "Day 0000 XXXX XXXX"

# Moves the cursor to the last line and character
previous.seek(0, 2)

print(f"Last tweet: {lastTweet.strip()}")

# Splits the last tweet up into a prevDay and prevQuote variable
prevDay = re.search("\d{4}", lastTweet.strip())
prevQuote = re.split("\d{4}", lastTweet.strip())

print(f"prevDay: {prevDay.group()}")
print(f"prevQuote: {prevQuote[1].strip()}")

newQuote = ""
# Increments the day by one
newDay = int(prevDay.group().strip()) + 1

# This will get changed to True when we pass the last quote used
prevPassed = False
for line in quotes.readlines():

    # This compares every tweet in the file to the previous one and
    # Also checks to see if it has passed the previous tweet already
    if line.strip() == prevQuote[1].strip() or prevPassed == True:
        # If it hasn't passed the pervious tweet, it states that it has and moves onto the next possible tweet
        if not prevPassed:
            prevPassed = True
        # This runs when it has passed the previous tweet and makes the new one
        else:
            # Puts the quote for the tweet into a new variable with the "Day [Day number in XXXX format] [Quote]"
            newQuote = f"Day {newDay:04} {line.strip()}"
            print(f"Next quote: {newQuote}")
            # Adds the tweet into the list of used tweets
            previous.write(f"\n{newQuote}")
            break;

if not newQuote:
    quotes.seek(0)
    newQuote = f"Day {newDay:04} {quotes.readline().strip()}"
    print(f"Quote not found, using first one:\n{newQuote}")
    previous.write(f"\n{newQuote}")