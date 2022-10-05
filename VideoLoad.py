from moviepy.editor import *
import os
import random
import fileLocations
import time

# Splice the video
def splice(video):

    output = fileLocations.splicedVideoDir

    # Duration of the video
    t = VideoFileClip(video).duration

    # Starting point of the end of the video clip
    clipEnd = 20

    # Filetype of the video clip
    fType = '.mp4'

    i = 0
    # Loop through the video while the clipEnd variable is less than 10 seconds before the video ends
    while clipEnd + 10 < t - 10:
        i = i + 1
        # Set the clip source, height = 1920 (width will be proportionate), and the clip length (the clipEnd - 10 seconds will be the starting point)
        clip = VideoFileClip(video).resize(height=1920).subclip(clipEnd - 10, clipEnd)
        # Crop the video to 1080x1920 in the center, which is the max size for a TikTok video
        clip = clip.crop(x_center=clip.w/2 , y_center=clip.h/2, width=1080, height=1920)
        # Remove any audio from the video
        clip = clip.without_audio()
        # Set the clip fps to 30
        clip = clip.set_fps(30)
        # Apply a gamma filter of 0.5 to make it darker
        clip = clip.fx(vfx.colorx, 0.5)

        # num will eventually be the video clip name
        num = 0
        vidNames = []

        print(f'{clipEnd}/{t} Seconds Completed')

        # Get every taken name in the output directory and append it to vidNames array
        for names in os.listdir(output):
            vidNames.append(names)

        # Shut the fuck up. I know that infinite loops is the highest of deadly sins. I don't care. It work. I'm not touching it. Not 100% sure how it works, but it does
        while True:
            # Set the previous num equal to what it currently is
            prevNum = num
            # For every video is vidNames
            for nam in vidNames:
                # If it has the same name increment by one
                if nam == format(str(num) + fType):
                    num = num + 1
                # If there was no change in 
            if prevNum == num:
                break;

        # Render out the video
        clip.write_videofile(output + str(num) + fType)
        # Progress by 10 seconds
        clipEnd = clipEnd + 10
        # Close the clip and release the memroy
        clip.close()
    screenshot(video, i)

# Get screenshots from a video
def screenshot(video, num):
    output = fileLocations.screenshotDir

    # Load the clip and set the height = 1080 (The width will scale proportionately)
    clip = VideoFileClip(video).resize(height=1080)
    # Crop the clip to 1080x1080 around the center
    clip = clip.crop(x_center=clip.w/2 , y_center=clip.h/2, width=1080, height=1080)
    # Apply a gamma filter of 0.5
    clip = clip.fx(vfx.colorx, 0.5)
    # Get the duration of the clip
    dur = clip.duration

    # Array of screenshots
    screenshots = []
    fType = '.png'

    # Create 10 screenshots
    for i in range(num):
        num = 0
        # Set the random seed
        random.seed((dur + i) * time.time())

        # Get the list of all of the existing screenshot names
        for names in os.listdir(output):
            screenshots.append(names)
            
        # I'm going to be honest. It took me like 10 min of staring at this to figure out how it worked. I know I shouldn't be using infinite loops, but I'm the on programming this, your not, its working. I'm not touching it
        while True:
            prevNum = num
            for screenshot in screenshots:
                if screenshot == format(str(num) + fType):
                    num = num + 1
            if prevNum == num:
                break;

        # Save the clip to the screenshot location at the random time
        clip.save_frame(format(output + str(num) + fType), t = int(random.randrange(int(dur) - 25) + 10))
        print(f'Captured screenshot \t{i + 1}/{num}')