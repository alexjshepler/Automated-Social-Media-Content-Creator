import json
import os
import ImportNew
import Generate
import sys

# [X] Check for unused quotes
ImportNew.updateQuotes()
# [X] Check for unused video
ImportNew.updateVideo()

ImportNew.shuffleAll()

# Generate.generateAll()