import LoadNew
import Content

# Load all of the quotes and videos. Import new quotes. Splice new videos
LoadNew.loadNewQuotes()
LoadNew.loadAndSpliceVideos()

# Generate all content
Content.generateAll()

#So that edits to the terribly written loop actually get shared across all uses of it
#I'm going to be honest. It took me like 10 min of staring at this to figure out how it worked. I know I shouldn't be using infinite loops, but I'm the on programming this, your not, its working. I'm not touching it
#Shut the fuck up. I know that infinite loops is the highest of deadly sins. I don't care. It work. I'm not touching it. Not 100% sure how it works, but it does
#This piece of code appears like 5 times throughout the program. I don't know how it works. I don't know what I was thinking. I know its bad practice. But I know it works. Its staying
#Like I said. It work. Don't touch. If you touch it will break
def badLoop(List):
    while True:
    	# Set the previous num equal to what it currently is
        prevNum = num
        # For every name in List
        for name in List:
        	# If it has the same name increment by one
            if name == format(str(num) + fType):
                num = num + 1
        # If there was no change in 
        if prevNum == num:
            break;