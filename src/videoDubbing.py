
from moviepy.editor import *   #import moviepy
videoclip = VideoFileClip("movie.mp4") #video clip
audioclip = AudioFileClip("dubbing.mp3") #audio clip
audioclip2 = AudioFileClip("background.mp3") #background audioclip
new_audioclip = CompositeAudioClip([audioclip, audioclip2]) #Composite audioclip and audioclip2
videoclip.audio = new_audioclip
videoclip.write_videofile("result.mp4")