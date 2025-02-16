


# pip install moviepy

from moviepy.editor import VideoFileClip

og_vid = 'sample_video.mp4'
output_vid = 'rotated_vid2.mp4'

video = VideoFileClip(og_vid)

rotated_vid = video.rotate(90)

rotated_vid.write_videofile(output_vid)

video.close()
rotated_vid.close()

