import os
import moviepy
import LoadNew
import random
import generateContent
from .. import fileLocations

usedQuotes = open(fileLocations.usedQuotes, 'r+')
unusedQuotes = open(fileLocations.unusedQuotes, 'r+')
videoDir = fileLocations.splicedVideoDir
screenshotDir = fileLocations.screenshotDir
audioDir = fileLocations.audioDir

def generateAll():
    audio = loadAudio()
    clip = loadClip()
    screenshot = loadScreenshot()
    quote = loadQuote()
    
    for i in range(len(quotes)):
        if audio is None:
            print('No audio files')
            break
        elif clip is None:
            print('No clips')
            break
        elif screenshot is None:
            print('No screenshots')
            break

        generateContent.generateTiktok(audio[random.randrange(len(audio))], clip[i], quote[i])
        generateContent.generateInsta(screenshot[i], quote[i])

        os.remove(clip[0])
        os.remove(screenshot[0])

        usedQuotes.seek(0, 2)
        usedQuotes.write(format('\n' + quote[i]))


def loadAudio():
    audio = []

    for a in os.listdir(audioDir):
        if a.endswith('.mp3'):
            audio.append(a)

    return format(audioDir + audio[random.randrange(len(audio))])

def loadClip():
    for c in os.listdir(videoDir):
        if c.endswith('.mp4'):
            return c
    return None

def loadScreenshot():
    screenshot = []

    for s in os.listdir(screenshotDir):
        if s.endswith('.png'):
            return s

    return None

def loadQuote():
    unusedQuotes.seek(0)
    if unusedQuotes.readall() is not None:

        for quote in unusedQuotes.readlines():
            quotes.append(quote.strip())
