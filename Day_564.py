


# pip install moviepy
from moviepy.editor import VideoFileClip, concatenate_videoclips

video1 = VideoFileClip('vid1.mp4')
video2 = VideoFileClip('vid2.mp4')

final_video = concatenate_videoclips([video1, video2])
final_video.write_videofile("concat.mp4")

video1.close()
video2.close()
final_video.close()