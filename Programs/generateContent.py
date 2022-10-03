from moviepy.editor import *
import os
import random
from mutagen.mp3 import MP3

clipDir = r"/Users/alexjshepler/Desktop/Epoch Industry/Videos/Clips/"
picDir = r"/Users/alexjshepler/Desktop/Epoch Industry/Images/Rendered/"
def generateTiktok(audio, video, quote):
    dur = 10 if MP3(audio).info.length > 10 else MP3(audio).info.length
    clip = VideoFileClip(video).subclip(0, dur)

    txt_clip = TextClip(quote, fontsize=50, method='caption', color='white', size=(1080,1920))
    txt_clip = txt_clip.set_duration(dur)

    audio = AudioFileClip(audio).subclip(0, dur)
    clip.audio = CompositeAudioClip([audio])

    renderVideo = CompositeVideoClip([clip, txt_clip])

    clipNames = []
    num = 0
    fType = '.mp4'

    for names in os.listdir(clipDir):
            clipNames.append(names)

    while True:
        prevNum = num
        for nam in clipNames:
            if nam == format(str(num) + fType):
                num = num + 1
        if prevNum == num:
            break;

    renderVideo.write_videofile(format(clipDir + str(num) + fType))

def generateInsta(screenshot, quote):
    txt_clip = TextClip(quote, fontsize=50, method='caption', color='white', size=(1080,1080))
    img = ImageClip(screenshot)
    final = CompositeVideoClip([img, txt_clip])

    picNames = []
    num = 0
    fType = '.png'

    for names in os.listdir(picDir):
            picNames.append(names)

    while True:
        prevNum = num
        for nam in picNames:
            if nam == format(str(num) + fType):
                num = num + 1
        if prevNum == num:
            break;

    final.save_frame(format(picDir + str(num) + fType))
