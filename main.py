import LoadNew
import Content
import os
import logging

logging.basicConfig(format="[%(levelname)s %(acstime)s]: %(message)s ")

# Load all of the quotes and videos. Import new quotes. Splice new videos
LoadNew.loadNewQuotes()
LoadNew.loadAndSpliceVideos()

# Generate all content
Content.generateAll()