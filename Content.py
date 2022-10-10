import os
import moviepy
import LoadNew
import random
import generateContent
import fileLocations

usedQuotes = open(fileLocations.usedQuotes, 'r+')
unusedQuotes = open(fileLocations.unusedQuotes, 'r+')
videoDir = fileLocations.splicedVideoDir
screenshotDir = fileLocations.screenshotDir
audioDir = fileLocations.audioDir

# Main content generation def
def generateAll():
    # Load the content
    audio = loadAudio()
    clip = loadClip()
    screenshot = loadScreenshot()
    quote = loadQuote()
    
    # Loop through whatever has the least amount of elements
    for i in range(min([len(clip), len(screenshot), len(quote)])):
        generateContent.generateTwitter(quote[i])
        generateContent.generateTiktok(audio[random.randrange(len(audio))], clip[i], quote[i])
        generateContent.generateInsta(screenshot[i], quote[i])

        # Remove the clip and screenshot that is unedited
        os.remove(clip[i])
        os.remove(screenshot[i])

        # Add the quote to the end of the used quotes text file
        usedQuotes.seek(0, 2)
        usedQuotes.write(format('\n' + quote[i]))

# Load the audio for the main def
def loadAudio():
    audio = []

    # Add every audio to the audio list
    for a in os.listdir(audioDir):
        if a.endswith('.mp3'):
            audio.append(format(fileLocations.audioDir + a))

    # Return the list
    return audio

# Load the clips fo the main def
def loadClip():
    clips = []

    # Add every clip to the clips list
    for c in os.listdir(videoDir):
        if c.endswith('.mp4'):
            clips.append(fileLocations.splicedVideoDir + c)

    # Return the list
    return clips

# Load the screenshots for the main def
def loadScreenshot():
    screenshot = []

    # Add every screenshot to the screenshot list
    for s in os.listdir(screenshotDir):
        if s.endswith('.png'):
            screenshot.append(format(fileLocations.screenshotDir + s))

    # Return the screenshot list
    return screenshot

# Load the quotes for the main def
def loadQuote():
    quotes = []
    unusedQuotes.seek(0)
    if unusedQuotes.readlines() is not None:
        unusedQuotes.seek(0)

        for quote in unusedQuotes.readlines():
            quotes.append(quote.strip())

    return quotes
