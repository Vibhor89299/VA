from cgitb import text
from email import message
import speech_recognition as sr
import yagmail

recognizer=sr.Recognizer()
with sr.Microphone() as source :
    print("Clearing Background Noise :")
    recognizer.adjust_for_ambient_noise(source,duration=1)
    print("waiting for your message....")
    recordedaudio=recognizer.listen(source)
    print("Done Recording......!")
try:
     print('printing the message...')
     text=recognizer.recognize_google(recordedaudio, language='en-US')
    
     print('your message: {}' .format(text))
   
except Exception as ex:
    print(ex)


