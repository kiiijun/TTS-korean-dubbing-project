
from moviepy.editor import *   #import moviepy
videoclip = VideoFileClip("movie.mp4") #video clip
audioclip = AudioFileClip("dubbing.mp3") #audio clip
new_audioclip = CompositeAudioClip([audioclip]) #Composite
videoclip.audio = new_audioclip
videoclip.write_videofile("result.mp4")