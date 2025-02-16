


# pip install moviepy

from moviepy.editor import VideoFileClip

mp4_file = VideoFileClip('z_test.mp4')

audio_only = mp4_file.audio

audio_only.write_audiofile('z_test.mp3')

















