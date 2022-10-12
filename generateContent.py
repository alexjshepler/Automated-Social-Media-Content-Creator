from moviepy.editor import *
import os
import random
from mutagen.mp3 import MP3
import json
import re

config = json.load(open(r'config.json'))

clipDir = config['videoDir']['rendered']
picDir = config['screenshotDir']['rendered']
twitter = config['quoteDir']['twitter']

# Generates a 10 second (or the duration of the sound) clip that is appropriate for TikTok
def generateTiktok(audio, video, quote):
    # Gets the duration. 10 seconds if the audio length is longer than 10 seconds, the length of the audio otherwise
    dur = 10 if MP3(audio).info.length > 10 else MP3(audio).info.length
    # Set the duration of the clip to the duration determined
    clip = VideoFileClip(video).subclip(0, dur)

    # Set the quote, font size, method, color, the size of the clip, and the duration
    txt_clip = TextClip(quote, fontsize=50, method='caption', color='white', size=(1080,1920)).set_duration(dur)

    # Sets the audio duration and the audio
    audio = AudioFileClip(audio).subclip(0, dur)
    # Applies the audio to the clip
    clip.audio = CompositeAudioClip([audio])

    # Composes the video and text
    renderVideo = CompositeVideoClip([clip, txt_clip])

    clipNames = []
    num = 0
    fType = '.mp4'

    # Get all of the names of the rendered files
    for names in os.listdir(clipDir):
            clipNames.append(names)

    # This piece of code appears like 5 times throughout the program. I don't know how it works. I don't know what I was thinking. I know its bad practice. But I know it works. Its staying
    while True:
        prevNum = num
        for nam in clipNames:
            if nam == format(str(num) + fType):
                num = num + 1
        if prevNum == num:
            break;

    # Render out the file
    renderVideo.write_videofile(format(clipDir + str(num) + fType))

def generateInsta(screenshot, quote):
    # Get the quote, set the font size, the method, color, and size
    txt_clip = TextClip(quote, fontsize=50, method='caption', color='white', size=(1080,1080))
    # Create the Image clip
    img = ImageClip(screenshot)
    # Compose the text and the image
    final = CompositeVideoClip([img, txt_clip])

    picNames = []
    num = 0
    fType = '.png'

    # Get a list of all taken names
    for names in os.listdir(picDir):
            picNames.append(names)

    # Like I said. It work. Don't touch. If you touch it will break
    while True:
        prevNum = num
        for nam in picNames:
            if nam == format(str(num) + fType):
                num = num + 1
        if prevNum == num:
            break;

    # Render out the screenshot
    final.save_frame(format(picDir + str(num) + fType))

def generateTwitter(quote):
    quotes = open(twitter, 'r+')

    quotes.write(f'Day {len(quotes.readlines()) + 1:04n} {quote}\n')