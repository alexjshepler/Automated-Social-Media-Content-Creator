from moviepy.editor import *
import os
import random
import time

def splice(video, output):

    t = VideoFileClip(video).duration

    clipEnd = 20

    fType = '.mp4'


    while clipEnd + 10 < t - 10:
        clip = VideoFileClip(video).resize(height=1920).subclip(clipEnd - 10, clipEnd)
        clip = clip.crop(x_center=clip.w/2 , y_center=clip.h/2, width=1080, height=1920)
        clip = clip.without_audio()
        clip = clip.set_fps(30)
        clip = clip.fx(vfx.colorx, 0.5)

        num = 0
        vidNames = []

        print(f'{clipEnd}/{t} Seconds Completed')

        for names in os.listdir(output):
            vidNames.append(names)

        while True:
            prevNum = num
            for nam in vidNames:
                if nam == format(str(num) + fType):
                    num = num + 1
            if prevNum == num:
                break;

        print(format(str(num) + fType))

        clip.write_videofile(output + str(num) + fType)
        clipEnd = clipEnd + 10
        clip.close()

def screenshot(video, output):
    print('Capturing Screenshots')
    clip = VideoFileClip(video).resize(height=1080)
    clip = clip.crop(x_center=clip.w/2 , y_center=clip.h/2, width=1080, height=1080)
    clip = clip.fx(vfx.colorx, 0.5)
    dur = clip.duration
    screenshots = []
    fType = '.png'


    for i in range(10):
        num = 0
        random.seed((dur + i) * time.time())
        for names in os.listdir(output):
            screenshots.append(names)
            
            while True:
                prevNum = num
                for screenshot in screenshots:
                    if screenshot == format(str(num) + fType):
                        num = num + 1
                if prevNum == num:
                    break;
        clip.save_frame(format(output + str(num) + fType), t = int(random.randrange(int(dur) - 25) + 10))
        print(f'Captured screenshot \t{i + 1}/10')