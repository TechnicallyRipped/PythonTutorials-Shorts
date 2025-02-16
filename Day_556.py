


# pip install moviepy

from moviepy.editor import VideoFileClip

x = 'sample_video.mp4'

clip = VideoFileClip(x)
duration = clip.duration 
clip.close()

print(f'Clip is {duration} seconds long')


