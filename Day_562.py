


# pip install moviepy

from moviepy.editor import VideoFileClip,vfx

og_vid = 'sample_video.mp4'
x_out = 'x_mir.mp4'
y_out = 'y_mir.mp4'

video = VideoFileClip(og_vid)

x_mir = video.fx(vfx.mirror_x)
y_mir = video.fx(vfx.mirror_y)

x_mir.write_videofile(x_out)
y_mir.write_videofile(y_out)

video.close()
x_mir.close()
y_mir.close()