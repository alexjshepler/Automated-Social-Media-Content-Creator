import os
import moviepy
import LoadNew
import random
import generateContent
import fileLocations

usedQuotes = open(fileLocations.usedQuotes, 'r+')
videoDir = fileLocations.splicedVideoDir
screenshotDir = fileLocations.screenshotDir
audioDir = fileLocations.audioDir

audio = ""
clip = ""
screenshot = ""
quote = ""

def generateAll():

    while True:
        audio = loadAudio()
        clip = loadClip()
        screenshot = loadScreenshot()
        quote = loadQuote()
        
        print(quote)

        if quote != "False":
            generateContent.generateTiktok(audio, clip, quote)
            generateContent.generateInsta(screenshot, quote)
            os.remove(clip)
            os.remove(screenshot)
        else:
            break

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
    try:
        unusedQuotes = open(fileLocations.unusedQuotes, 'r+')
        unusedQuotes.seek(0)
        quote = unusedQuotes.readlines()[0]
        usedQuotes.seek(0,2)
        usedQuotes.write(quote)
        LoadNew.loadNewQuotes()

        return quote.strip()
    except:
        return "False"
