import os
import random
import json
from moviepy.editor import *
import time

config = json.load(open(r'config.json'))

# Video Directories
orDir = config['videoDir']['original']
spDir = config['videoDir']['spliced']

# Screenshot Directory
ssDir = config['screenshotDir']['screenshots']

# Updates the unused quote file
def updateQuotes():
    # Quote Files
    alQuotes = open(config['quoteDir']['all'], 'r')
    unQuotes = open(config['quoteDir']['unused'], 'r+')
    usQuotes = open(config['quoteDir']['used'], 'r+')

    # Read the unused and used quotes into lists and strip of new line
    un = unQuotes.read().splitlines()
    us = usQuotes.read().splitlines()

    # Check every quote in main quote file to see if it is in used or unused
    for al in alQuotes.readlines():
        if al.strip() in un or al.strip() in us:
            pass
        else:
            unQuotes.writelines(format(al.strip() + '\n'))

    unQuotes = open(config['quoteDir']['unused'], 'r+')

    q = unQuotes.read().splitlines()
    q = [*set(q)]

    unQuotes = open(config['quoteDir']['unused'], 'w')
    
    for l in q:
        unQuotes.write(format(l + '\n'))

def updateVideo():
    for v in os.listdir(orDir):
        if v.endswith('.mp4') or v.endswith('.m4v') or v.endswith('.mkv'):
            orLoc = format(orDir + v)
            t = VideoFileClip(orLoc).duration
            fType = '.mp4'
            sEnd = 20
            tSplice = 0
            cSplice = 0
            i = 0

            while i + 10 < t - 10:
                tSplice = tSplice + 1
                i = i + 10

            while sEnd < t - 10:
                splice = VideoFileClip(orLoc).resize(height=1920).subclip(sEnd - 10, sEnd).without_audio().set_fps(30).fx(vfx.colorx, 0.5)
                splice = splice.crop(x_center=splice.w/2, y_center=splice.h/2, width=1080, height=1920)

                name = 0
                spNames = []

                for n in os.listdir(spDir):
                    if n.endswith('.mp4'):
                        spNames.append(n)

                while format(str(name) + '.mp4') in spNames:
                    name = name + 1
                else:
                    lName = spDir + str(name) + '.mp4'

                splice.write_videofile(lName)
                sEnd = sEnd + 10

                splice = splice.resize(width=1080).crop(x_center=splice.w/2, y_center=splice.h/2, width=1080, height=1080)

                ssNames = []
                fType = '.png'
                name = 0

                random.seed(splice.duration * time.time())

                for n in os.listdir(ssDir):
                    if n.endswith('.png'):
                        ssNames.append(n)
                
                while format(str(name) + '.png') in ssNames:
                    name = name + 1
                else:
                    name = ssDir + str(name) + fType

                splice.save_frame(name, t = 0.01)

                splice.close()

def shuffleAll():
    sp = []

    for n in os.listdir(spDir):
        if n.endswith('.mp4'):
            os.rename(spDir + n, spDir + n + '.temp')

    for n in os.listdir(spDir):
        if n.endswith('.temp'):
            sp.append(n)

    random.shuffle(sp)

    for n in range(len(sp)):
        os.rename(spDir + sp[n], spDir + str(n) + '.mp4')