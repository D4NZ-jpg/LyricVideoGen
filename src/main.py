from moviepy.editor import *
from decimal import Decimal
import timing


audio_path = input("Path of Audio: ")
text_path = input("Path of Text: ")
background_path = input("Path of Background: ") 
output_path = input("Output Path: ")

# Get lyrics
lyrics = timing.get(audio_path, text_path)

# Prepare video
audio = AudioFileClip(audio_path)
background = VideoFileClip(background_path).without_audio().loop(duration = audio.duration)
background.audio = audio

# Add lyrics to video
text_clips = [background]
for leave in lyrics:
    if(leave.text) == "":
        continue

    txt = TextClip(leave.text, fontsize=40, color = "black", font="FreeSerif").set_pos("center").set_duration(float(leave.end-leave.begin))
    txt = txt.set_start(max(0,float(leave.begin)-0.2))
    text_clips.append(txt)


#export
background = CompositeVideoClip(text_clips)
background.write_videofile(output_path)
