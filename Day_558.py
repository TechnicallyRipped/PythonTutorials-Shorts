


# pip install moviepy

from moviepy.editor import VideoFileClip
from moviepy.video.fx import speedx

og_vid = 'sample_video.mp4'
output_vid = 'changed_speed.mp4'

video = VideoFileClip(og_vid)

vid2 = video.fx(speedx.speedx,factor=3)

vid2.write_videofile(output_vid)

video.close()
vid2.close()

