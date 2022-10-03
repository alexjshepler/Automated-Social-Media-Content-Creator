import os
import videoLoad
import random

videoDir = r'/Users/alexjshepler/Desktop/Epoch Industry/Videos/Original/'
splicedVideoDir = r'/Users/alexjshepler/Desktop/Epoch Industry/Videos/Spliced/'

screenshotDir = r'/Users/alexjshepler/Desktop/Epoch Industry/Images/Screenshots/'

def loadNewQuotes():
    allQuotes = open(r'/Users/alexjshepler/Desktop/Epoch Industry/Programs/quotes/quotes.txt', 'r')
    unusedQuotes = open(r'/Users/alexjshepler/Desktop/Epoch Industry/Programs/quotes/unused.txt', 'r+')
    usedQuotes = open(r'/Users/alexjshepler/Desktop/Epoch Industry/Programs/quotes/used.txt', 'r+')
    
    unusedQuotes.seek(0, 2)
    unusedQuotes.write('\n')

    with open('temp.txt', 'w') as temp:

        for line in allQuotes.readlines():
            unusedQuotes.write(line)

        unusedQuotes.seek(0)

        for unused in unusedQuotes.readlines():
            usedQuotes.seek(0)
            isUsed = False
            for used in usedQuotes.readlines():
                if unused.strip() == used.strip():
                    isUsed = True
            
            if not isUsed:
                temp.write(unused)
        os.replace('temp.txt', '/Users/alexjshepler/Desktop/Epoch Industry/Programs/unused.txt')

    unusedQuotes = open(r'/Users/alexjshepler/Desktop/Epoch Industry/Programs/unused.txt', 'r+')
    with open('temp.txt', 'w') as temp:
        unusedQuotes.seek(0)
        temp = open('temp.txt', 'r+')
        for unused in unusedQuotes.readlines():
            temp.seek(0)
            hasSeen = False
            try:
                for seen in temp.readlines():
                    if unused.strip() == seen.strip():
                        hasSeen = True
            except:
                pass
            if not hasSeen:
                temp.seek(0, 2)
                temp.write(unused)
        os.replace('temp.txt', '/Users/alexjshepler/Desktop/Epoch Industry/Programs/unused.txt')

def loadAndSpliceVideos():
    for video in os.listdir(videoDir):
        if video.endswith('.mp4') or video.endswith('.m4v') or video.endswith('.mkv'):
            videoLoc = format(videoDir + video)
            videoLoad.splice(videoLoc, splicedVideoDir)
            videoLoad.screenshot(videoLoc, screenshotDir)
            os.rename(videoLoc, format(videoDir + video + '.old'))

    files = []
    for file in os.listdir(splicedVideoDir):
        if file.endswith('.mp4'):
            os.rename(format(splicedVideoDir + file), format(splicedVideoDir + file + '.temp'))

    for file in os.listdir(splicedVideoDir):
        if file.endswith('.temp'):
            files.append(file)

    random.shuffle(files)

    i = 0

    for file in files:
        os.rename(format(splicedVideoDir + file), format(splicedVideoDir + str(i) + '.mp4'))
        i = i + 1

    files = []
    for file in os.listdir(screenshotDir):
        if file.endswith('.png'):
            os.rename(format(screenshotDir + file), format(screenshotDir + file + '.temp'))

    for file in os.listdir(screenshotDir):
        if file.endswith('.temp'):
            files.append(file)

    random.shuffle(files)

    i = 0

    for file in files:
        os.rename(format(screenshotDir + file), format(screenshotDir + str(i) + '.png'))
        i = i + 1
