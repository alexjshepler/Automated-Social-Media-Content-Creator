import os
from moviepy import *
import json
import random
from mutagen.mp3 import MP3

config = json.load(open(r'config.json'))

usQuotes = open(config["quoteDir"]["used"], 'r+')
unQuotes = open(config['quoteDir']['unused'], 'r+')

spLoc = config['videoDir']['spliced']
reLoc = config['videoDir']['rendered']

ssLoc = config['screenshotDir']['screenshots']

auLoc = config['audio']['audio']

def generateAll():
    au = load(auLoc, '.mp3')
    sp = load(spLoc, '.mp4')
    ss = load(ssLoc, '.png')
    un = loadQuotes()

    for i in range(min([len(au), len(sp), len(ss), len(un)])):
        t = 10 if MP3(au[i]).info.length > 10 else MP3(au[i]).info.length

        rend = VideoFileClip(sp[i]).subclip(0, t)
        text = TextClip(un[i].strip(), fontsize=50, method='caption', color='white', size=(1080, 1920)).set_duration(t)
        audi = AudioFileClip(au[i]).subclip(0, t)

        rend.audio = CompositeAudioClip([audio])

        render = CompositeVideoClip([rend, text])

        name = 0
        reNames = []

        for n in os.listdir(reLoc):
            if n.endswith('.mp4'):
                reNames.append(n)

        while format(str(name) + '.mp4') in spNames:
            name = name + 1
        else:
            name = reLoc + str(name) + '.mp4'

        renderVideo.write_videofile(name)

        ssNames = []
        name = 0

        for n in os.listdir(ssLoc):
            if n.endswith('.png'):
                ssNames.append(n)

        while format(str(name) + '.png') in ssNames:
            name = name + 1
        else:
            name = ssLoc + str(name) + '.png'

        splice.save_frame(name, t = int(random.randrange(int(t))))

        rend.close()

def load(loc, fType):
    l = []

    for i in os.listdir(loc):
        if i.endswith(fType):
            l.append(format(loc + i))

    return l

def loadQuotes():
    q = []

    for line in unQuotes.readlines():
        if len(line) > 0:
            q.append(line.strip())

    return q