import os
import moviepy
import LoadNew
import random
import generateContent
import fileLocations

unusedQuotes = open(fileLocations.unusedQuotes, 'r+')
usedQuotes = open(fileLocations.usedQuotes, 'r+')
videoDir = fileLocations.splicedVideoDir
screenshotDir = fileLocations.screenshotDir
audioDir = fileLocations.audioDir

audio = []
clip = []
screenshot = []
quote = ""

def generateAll():
    audio = loadAudio()
    clip = loadClip()
    screenshot = loadScreenshot()
    quote = loadQuote()
    
    generateContent.generateTiktok(audio, clip, quote)
    generateContent.generateInsta(screenshot, quote)

def loadAudio():
    audio = []

    for a in os.listdir(audioDir):
        if a.endswith('.mp3'):
            audio.append(a)

    return format(audioDir + audio[random.randrange(len(audio))])

def loadClip():
    clip = []

    for c in os.listdir(videoDir):
        if c.endswith('.mp4'):
            clip.append(c)
    return format(videoDir + clip[random.randrange(len(clip))])

def loadScreenshot():
    screenshot = []

    for s in os.listdir(screenshotDir):
        if s.endswith('.png'):
            screenshot.append(s)

    return format(screenshotDir + screenshot[random.randrange(len(screenshot))])

def loadQuote():
    quote = unusedQuotes.readlines()[0]
    usedQuotes.write(quote)

    LoadNew.loadNewQuotes()

    return quote
