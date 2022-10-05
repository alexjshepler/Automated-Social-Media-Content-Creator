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

def generateAll():
    audio = loadAudio()
    clip = loadClip()
    screenshot = loadScreenshot()
    quote = loadQuote()
    
    for i in range(len(quote)):
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

        os.remove(clip[i])
        os.remove(screenshot[i])

        usedQuotes.seek(0, 2)
        usedQuotes.write(format('\n' + quote[i]))


def loadAudio():
    audio = []

    for a in os.listdir(audioDir):
        if a.endswith('.mp3'):
            audio.append(format(fileLocations.audioDir + a))

    return audio

def loadClip():
    clips = []
    for c in os.listdir(videoDir):
        if c.endswith('.mp4'):
            clips.append(fileLocations.splicedVideoDir + c)
    return clips

def loadScreenshot():
    screenshot = []

    for s in os.listdir(screenshotDir):
        if s.endswith('.png'):
            screenshot.append(format(fileLocations.screenshotDir + s))

    return screenshot

def loadQuote():
    quotes = []
    unusedQuotes.seek(0)
    if unusedQuotes.readlines() is not None:
        unusedQuotes.seek(0)

        for quote in unusedQuotes.readlines():
            quotes.append(quote.strip())

    return quotes
