import os
import moviepy
import LoadNew
import random
import generateContent

unusedQuotes = open(r'/Users/alexjshepler/Desktop/Epoch Industry/Programs/quotes/unused.txt', 'r+')
usedQuotes = open(r'/Users/alexjshepler/Desktop/Epoch Industry/Programs/quotes/used.txt', 'r+')
videoDir = r'/Users/alexjshepler/Desktop/Epoch Industry/Videos/Spliced/'
screenshotDir = r'/Users/alexjshepler/Desktop/Epoch Industry/Images/Screenshots/'
audioDir = r'/Users/alexjshepler/Desktop/Epoch Industry/Audio/'

audio = ""
clip = ""
screenshot = ""
quote = ""

def generateAll():
    audio = loadAudio()
    clip = loadClip()
    screenshot = loadScreenshot()
    quote = loadQuote()
    
    print(audio)
    print(clip)
    print(quote)
    # generateContent.generateTiktok(audio, clip, quote)
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

    return quote
