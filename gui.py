import speech_recognition as sr 
from textblob import TextBlob
from gtts import gTTS
import os
from pygame import mixer
from tkinter import *

root=Tk()
root.geometry('800x400')
root.title("Google's Speech Application")
root.config(background='powder blue')

lab1=Label(root,text='Speech To Speech Translator',bg='powder blue',fg='black',font=('arial 16 bold')).pack()

def speech2text():
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
    return texts

inptext=speech2text()
inp_text = "Input speech is : " + inptext
print("the input text is : ", inptext)
lab2=Label(root,text=inp_text,font=('arial 16'),bg='powder blue',fg='black').pack()
mytext=StringVar()
lab3=Label(root,text='Enter language',font=('arial 16'),bg='powder blue',fg='black').pack()
lan=StringVar()

def fetch():
    trtext=TextBlob(inptext)
    language=lan.get()
    tr_text=trtext.translate(to=language)
    ntext=str(tr_text)
    fintext = "translated text : " + ntext
    labn=Label(root,text=fintext,font=('arial 16'),bg='powder blue',fg='black').place(x=200, y=230)
    myob=gTTS(text=ntext,lang=language,slow=False)
    myob.save('Voice1.mp3')

def play():
   from pygame import mixer
   mixer.init()
   mixer.music.load("Voice1.mp3")
   mixer.music.play()


def close_window():
    root.destroy()

ent2=Entry(root,tex=lan,font=('arial 13')).pack()

but1=Button(root,text='Convert',width=20,bg='brown',fg='white',command=fetch).place(x=100,y=100)

but2=Button(root,text='Play',width=20,bg='brown',fg='white',command=play).place(x=100,y=140)

but3=Button(root,text='Close',width=20,bg='brown',fg='white',command=close_window).place(x=100,y=180)


root.mainloop()

