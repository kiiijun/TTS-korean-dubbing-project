from moviepy.editor import *   #import moviepy
from moviepy.video.tools.subtitles import SubtitlesClip
from moviepy.video.io.VideoFileClip import VideoFileClip
videoclip = VideoFileClip("movie.mp4") #video clip
audioclip = AudioFileClip("dubbing.mp3") #audio clip
audioclip2 = AudioFileClip("background.mp3") #background audioclip
new_audioclip = CompositeAudioClip([audioclip, audioclip2]) #Composite audioclip and audioclip2
videoclip.audio = new_audioclip
videoclip.write_videofile("result.mp4")

generator = lambda txt: TextClip(txt, font='Georgia-Regular', fontsize=30, color='white',)
subtitles = SubtitlesClip("subtitles.srt", generator)
myvideo = VideoFileClip("result.mp4")
final = CompositeVideoClip([myvideo, subtitles.set_pos(('center','bottom'))])
final.write_videofile("final.mp4", fps=myvideo.fps)
