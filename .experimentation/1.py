'''
import pyttsx3
engine = pyttsx3.init()
lyrics = (''You know you love me , I know you care 
Just shout whenever , and I'll be there 
You are my love , you are my heart 
And we will never, ever, ever be apart '')
engine.save_to_file(lyrics,'output_audio.mp3')
engine.say(lyrics)
engine.runAndWait()

import pyttsx3                      #changing the volume with 0.0 lowest and 1.0 highest
engine = pyttsx3.init()
volume = engine.getProperty('volume')
print({volume})
engine.setProperty('volume',0.5)
engine.say('hii how r u')
engine.runAndWait()  

import pyttsx3
engine = pyttsx3.init()
volume = engine.getProperty('volume')
print({volume})
engine.setProperty('volume',1.0)
engine.say('hii how r u')
engine.runAndWait()

import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[0].id)
engine.say("Hello! This is the male voice.")
engine.runAndWait()
 
engine.setProperty('voice', voices[1].id)
engine.say("Hi there! This is the female voice.")
engine.runAndWait()
 
engine.setProperty('voice', voices[2].id)
engine.say("Hi there! This is the mix voice.")
engine.runAndWait()
'''
 
import pyttsx3
engine = pyttsx3.init()
engine.say("I'm so excited to meet you!")
engine.runAndWait()
engine.setProperty('rate', 120)  # Slow down for dramatic effect
engine.say("Wait... Did you hear that?")
engine.runAndWait()
engine.setProperty('rate', 250)  # Speed up for urgency
engine.say("Quick! We have to run now!")
engine.runAndWait()