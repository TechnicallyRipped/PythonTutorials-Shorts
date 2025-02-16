


# pip install moviepy

from moviepy.editor import VideoFileClip

og_vid = 'sample_video.mp4'
muted_path = 'muted_vid.mp4'

video = VideoFileClip(og_vid)

muted_vid = video.without_audio()

muted_vid.write_videofile(muted_path)

video.close()
muted_vid.close()
