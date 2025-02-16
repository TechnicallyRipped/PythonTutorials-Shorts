


# pip install moviepy

from moviepy.editor import VideoFileClip
from moviepy.video.fx import blackwhite

og_vid = 'sample_video.mp4'
bw_vid = 'bw_vid.mp4' 

video = VideoFileClip(og_vid)

bw_video = video.fx(blackwhite.blackwhite)

bw_video.write_videofile(bw_vid)

video.close()
bw_video.close()

