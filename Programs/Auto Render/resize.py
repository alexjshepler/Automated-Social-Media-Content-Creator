from moviepy.editor import *
import os

# videos = open("Videos/")

subtitle = "test"

clip = VideoFileClip("/Users/alexjshepler/Desktop/Epoch Industry/Videos/video-2-of-87.m4v").resize(width=1920).subclip(0, 10)

txt_clip = TextClip(subtitle, 25, color='white')
txt_clip = txt_clip.set_pos('center').set_duration(10)

video = CompositeVideoClip([clip,txt_clip])

video.ipython_display()