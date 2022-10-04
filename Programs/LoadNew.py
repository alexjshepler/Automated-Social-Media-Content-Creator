import os
import videoLoad
import random
import fileLocations

# Unspliced video dir
videoDir = fileLocations.fullVideoDir
splicedVideoDir = fileLocations.splicedVideoDir

# Screenshot directory
screenshotDir = fileLocations.screenshotDir

# Loads all new quotes
def loadNewQuotes():
    # Open the quote files
    allQuotes = open(fileLocations.allQuotes, 'r')
    unusedQuotes = open(fileLocations.unusedQuotes, 'r+')
    usedQuotes = open(fileLocations.usedQuotes, 'r+')
    
    # Go to the end of the unused quote file and add a new line at the end
    unusedQuotes.seek(0, 2)
    unusedQuotes.write('\n')

    # Create a temp file that we can dump the unused quotes in
    with open('temp.txt', 'w') as temp:
        # Add all quotes, regardless if used or not, to the unused quote file
        for line in allQuotes.readlines():
            unusedQuotes.write(line)

        # Set the cursor to the beginning of the file
        unusedQuotes.seek(0)

        # Check every line to see if it is in the used file
        for unused in unusedQuotes.readlines():
            # Bring the cursor to the beginning of the unused file
            usedQuotes.seek(0)
            isUsed = False
            # Go through every line in the used file
            for used in usedQuotes.readlines():
                # And check to see if that equals the current line in the unused file
                if unused.strip() == used.strip():
                    # If it matches set isUsed to True
                    isUsed = True
            
            # If isUsed is False it means that it hasn't been used. So we can write it to a temporary file
            if not isUsed:
                temp.write(unused)
        
        # Once every file in the unused file has been compared to the used file, and only the unused quotes are left. We can replace the unused file with the temp
        # because the temp file is where we were putting the quotes that we haven't used before, and the unused had the allQuotes file dumped in it
        os.replace('temp.txt', fileLocations.unusedQuotes)

    # Reopen the unusedQuotes file
    unusedQuotes = open(fileLocations.unusedQuotes, 'r+')
    # Create a temp file that we can dump the unique quotes in
    with open('temp.txt', 'w') as temp:
        # Set the cursor to the beginning of the unusedQuotes file
        unusedQuotes.seek(0)
        # Open the temp file in read and write mode, not just write
        temp = open('temp.txt', 'r+')
        # Go through every line of the unused quotes file
        for unused in unusedQuotes.readlines():
            # Set the cursor to the beginning of the temp file
            temp.seek(0)
            hasSeen = False
            try:
                # Go through every line of the temp file
                for seen in temp.readlines():
                    # If a line in the temp file matches the current line in the unusedQuotes file, we've seen that line before
                    if unused.strip() == seen.strip():
                        # Se the hasSeen variable to True because the line has been seen
                        hasSeen = True
            except:
                pass
            # If hasSeen remains False by the time we've iterated through the entirety of the temp file, we have not seen that line before and we add it
            if not hasSeen:
                # Go to the end of the temp file and write the line
                temp.seek(0, 2)
                temp.write(unused)
        # Replace the unusedQuotes file with the temp file, because the temp file contains only unique lines that do not have duplicates
        os.replace('temp.txt', fileLocations.unusedQuotes)

# Load in the new, untouched videos and splice them and take 10 screenshots
def loadAndSpliceVideos():
    # For every file in the video directory
    for video in os.listdir(videoDir):
        # That ends in '.mp4', '.m4v', or '.mkv' 
        if video.endswith('.mp4') or video.endswith('.m4v') or video.endswith('.mkv'):
            videoLoc = format(videoDir + video)
            # Splice that video and output the splices to the spliceVideoDir
            videoLoad.splice(videoLoc)
            # Then rename the video and add the .old filetype so it doesn't get spliced again
            os.rename(videoLoc, format(videoDir + video + '.old'))

    files = []
    # For every file in the spliceVideoDir
    for file in os.listdir(splicedVideoDir):
        # That has the file type of '.mp4'
        if file.endswith('.mp4'):
            # Add the '.temp' filetype
            os.rename(format(splicedVideoDir + file), format(splicedVideoDir + file + '.temp'))

    # For every file in the splicedVideoDir
    for file in os.listdir(splicedVideoDir):
        # That ends with '.temp'
        if file.endswith('.temp'):
            # Append that file to the array files
            files.append(file)

    # Shuffle the files array
    random.shuffle(files)

    i = 0

    # Rename every file in the files array in numeric order after its been shuffled
    for file in files:
        os.rename(format(splicedVideoDir + file), format(splicedVideoDir + str(i) + '.mp4'))
        i = i + 1

    files = []
    # For every file in the screenshotDir
    for file in os.listdir(screenshotDir):
        # That has the file type of '.png'
        if file.endswith('.png'):
            # Add the '.temp' filetype
            os.rename(format(screenshotDir + file), format(screenshotDir + file + '.temp'))

    # For every file in the screenshotDir
    for file in os.listdir(screenshotDir):
        # That ends with '.temp'
        if file.endswith('.temp'):
            # Append the file to the files array
            files.append(file)

    # Shuffle the files array
    random.shuffle(files)

    i = 0

    # Rename every file in the files array in numeric order after its been shuffled
    for file in files:
        os.rename(format(screenshotDir + file), format(screenshotDir + str(i) + '.png'))
        i = i + 1
