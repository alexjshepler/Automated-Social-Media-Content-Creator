from moviepy.editor import *
import os
import re
import random
from mutagen.mp3 import MP3

videoDir = r"/Users/alexjshepler/Desktop/Epoch Industry/Videos"
soundDir = r"/Users/alexjshepler/Desktop/Epoch Industry/Sounds"
quoteFile = r"/Users/alexjshepler/Desktop/Epoch Industry/Programs/Auto Post/tweets/CurrentQuotes.txt"

quotes = open(quoteFile, 'r')

videos = []
sounds = []

def render(video, audio, quote, name):

    mp3 = format(soundDir + '/' + audio)

    # Cropping the clip
    # print("Cropping")
    clip = VideoFileClip(format(videoDir + '/' + video.strip())).resize(height=1920).subclip(0, 10 if MP3(mp3).info.length > 10 else MP3(mp3).info.length)
    clip = clip.crop(x_center=clip.w/2 , y_center=clip.h/2, width=1080, height=1920)

    # Adding text
    # print("Adding text")
    txt_clip = TextClip(quote.strip(), fontsize=50, method='caption', color='white', size=(1080,1920))
    txt_clip = txt_clip.set_duration(10 if MP3(mp3).info.length > 10 else MP3(mp3).info.length)

    # Rendering
    # print("Rendering")
    renderVideo = CompositeVideoClip([clip, txt_clip])

    renderVideo.write_videofile(videoDir + '/' + name + '.mp4')

def loadClips(length):
    while len(videos) < length:
        for file in os.listdir(videoDir):
            if file.endswith('.m4v'):
                videos.append(file)
        
    while len(sounds) < length:
        for file in os.listdir(soundDir):
            if file.endswith('.mp3'):
                sounds.append(file)

    random.shuffle(videos)
    random.shuffle(sounds)

print("Loading clips...")
loadClips(len(quotes.readlines()))
quotes.seek(0, 0)
print("COMPLETED")

index = 0

for line in quotes.readlines():
    print(f"Rendering video {index}")
    render(videos[index], sounds[index], line.strip(), str(index))
    break