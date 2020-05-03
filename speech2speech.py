import speech_recognition as sr 
from textblob import TextBlob
from gtts import gTTS
import os
from pygame import mixer
import pygame

#Sample rate is how often values are recorded 
sample_rate = 48000
#Chunk is like a buffer. It stores 2048 samples (bytes of data) 
#here.  
#it is advisable to use powers of 2 such as 1024 or 2048 
chunk_size = 2048
#Initialize the recognizer 
r = sr.Recognizer() 
  
#generate a list of all audio cards/microphones 
mic_list = sr.Microphone.list_microphone_names() 
device_id=0
#the following loop aims to set the device ID of the mic that 
#we specifically want to use to avoid ambiguity. 

#use the microphone as source for input. Here, we also specify  
#which device ID to specifically look for incase the microphone  
#is not working, an error will pop up saying "device_id undefined" 
with sr.Microphone(device_index = device_id, sample_rate = sample_rate,  
                        chunk_size = chunk_size) as source: 
    #wait for a second to let the recognizer adjust the  
    #energy threshold based on the surrounding noise level 
    r.adjust_for_ambient_noise(source) 
    print ("Say Something")
    #listens for the user's input 
    audio = r.listen(source) 
          
    try: 
        texts = r.recognize_google(audio) 
        print ("you said: " + texts )
      
    #error occurs when google could not understand what was said 
      
    except sr.UnknownValueError: 
        print("Google Speech Recognition could not understand audio") 
      
    except sr.RequestError as e: 
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

langs=input('Enter the languange in which you want to convert:')
trtext=TextBlob(texts)
tr_text=trtext.translate(to=langs)
print(tr_text)
ntext=str(tr_text)

myobj = gTTS(text=ntext, lang=langs, slow=False) 
  
## Saving the converted audio in a mp3 file named welcome  
myobj.save("w.mp3") 
  
## Playing the converted file 
mixer.init()
mixer.music.load('w.mp3')
mixer.music.play()
while pygame.mixer.music.get_busy(): 
    pygame.time.Clock().tick(10)
