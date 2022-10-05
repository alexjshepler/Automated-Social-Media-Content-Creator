import LoadNew
import Content
import os

# Load all of the quotes and videos. Import new quotes. Splice new videos
LoadNew.loadNewQuotes()
LoadNew.loadAndSpliceVideos()

# Generate all content
Content.generateAll()