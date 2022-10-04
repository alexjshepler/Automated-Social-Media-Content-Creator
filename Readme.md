# Social Media Manager


# Overview

Content.py - This is what calls all of the loading methods
fileLocations.py - This stores all of the file locations
generateContent.py - This is what generates the content with the audio and the quotes over the videos and screenshots
LoadNew.py - This is what loads all new clips and quotes
main.py - This is the entry point of the program
videLoad.py - This is what splices the video

## Basic Work Flow

1) Pull quote list
2) Compare to the used one. If match found, delete from temp. Remaining quotes get put into unused
3) Check for new videos. If new, split into 10 second segments, delete the first segment, and store into temp file
4) Move the videos from temp to the main one, fill in gaps.
5) Randomize the list of videos
6) Check for new links for sounds
7) Download and randomize them
8) Load one quote, one video, one image, and one audio
9) Send the quote and video to the tiktok and youtube short workflow
10) Send the quote and image to the instagram workflow
11) Take the quote and find the day number and send that to the twitter workflow
12) Move the quotes to the usedQuotes file
13) Delete the video clip and image

## Twitter Work Flow

## TODO

- [ ] Check to see if a new video has been added
- [ ] Check to see if there are new quotes
