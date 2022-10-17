import pytube
import ffmpeg
import time
import ssl

def clean_filename(name):
    """Ensures each file name does not contain forbidden characters and is within the character limit"""
    # For some reason the file system (Windows at least) is having trouble saving files that are over 180ish
    # characters.  I'm not sure why this is, as the file name limit should be around 240. But either way, this
    # method has been adapted to work with the results that I am consistently getting.
    forbidden_chars = '"*\\/\'.|?:<>'
    filename = (''.join([x if x not in forbidden_chars else '#' for x in name])).replace('  ', ' ').strip()
    if len(filename) >= 176:
        filename = filename[:170] + '...'
    return filename 

ssl._create_default_https_context = ssl._create_unverified_context

link = 'https://www.youtube.com/watch?v=h3fUgOKFMNU&t=16s'

ti = time.time()
yt = pytube.YouTube(link, use_oauth=True, allow_oauth_cache=True)
print('Title:', yt.title)
print('Author:', yt.author)
print('Published date:', yt.publish_date.strftime("%Y-%m-%d"))
print('Number of views:', yt.views)
print('Length of video:', yt.length, 'sec')

vid = ''

try:
    yt.streams.filter(res='2160p', progressive=False).first().download(filename='video.mkv')
    yt.streams.filter(abr='160kbps', progressive=False).first().download(filename='audio.mp3')
    res = '2160p'
    vid = 'video.mkv'
except:
    try:
        yt.streams.filter(res='1440p', progressive=False).first().download(filename='video.mkv')
        yt.streams.filter(abr='160kbps', progressive=False).first().download(filename='audio.mp3')
        res = '1440p'
        vid = 'video.mkv'
    except:
        try:
            yt.streams.filter(res='1080p', progressive=False).first().download(filename='video.mp4')
            yt.streams.filter(abr='160kbps', progressive=False).first().download(filename='audio.mp3')
            res = '1080p'
            vid = 'video.mp4'
        except:
            yt.streams.filter(res='720p', progressive=False).first().download(filename='video.mp4')
            yt.streams.filter(abr='128kbps', progressive=False).first().download(filename='audio.mp3')
            res = '720p'
            vid = 'video.mp4'
    
audio = ffmpeg.input('audio.mp3')
video = ffmpeg.input(vid)
filename = clean_filename(yt.title) + '.mkv'    #for Windows output to folder C:\Users\Admin\Downloads\
ffmpeg.output(audio, video, filename).run(overwrite_output=True)
print(res, 'video successfully downloaded from', link)
print('Time taken: {:.0f} sec'.format(time.time() - ti))