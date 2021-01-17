import pyttsx3
import os

engine = pyttsx3.init() # object creation

input_file = 'chatlogs/tJ3HJmsa copy.txt'

""" RATE"""
rate = engine.getProperty('rate')   # getting details of current speaking rate
print (rate)                        #printing current voice rate
engine.setProperty('rate', 125)     # setting up new voice rate

"""VOLUME"""
volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
print (volume)                          #printing current volume level
engine.setProperty('volume', 1)    # setting up volume level  between 0 and 1

"""VOICE"""
voices = engine.getProperty('voices')       #getting details of current voice
#engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
engine.setProperty('voice', voices[0].id)   #changing index, changes voices. 1 for female

""" engine.say("Hello World!")
engine.say('My current speaking rate is ' + str(rate))
engine.runAndWait()
engine.stop() """

"""Saving Voice to a file"""
# On linux make sure that 'espeak' and 'ffmpeg' are installed
script = 'Stellaric: this is a message\nLordofpoop: this is a message'
engine.save_to_file(script, 'narration_temp.mp3')
engine.runAndWait()



os.system(f'.\\ffmpeg-2021-01-12-git-ca21cb1e36-essentials_build\\bin\\ffmpeg -loop 1 -i screenshot_cropped.png -i narration_temp.mp3 -c:v libx264 -tune stillimage -c:a aac -b:a 192k -pix_fmt yuv420p -shortest out1.mp4')

