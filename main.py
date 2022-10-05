from Programs import VideoLoad
from Programs import LoadNew
# from Programs import LoadNew
# from Programs import Content
import os

print(os.getcwd())
pass
# Load all of the quotes and videos. Import new quotes. Splice new videos
LoadNew.loadNewQuotes()
LoadNew.loadAndSpliceVideos()

# Generate all content
Content.generateAll()