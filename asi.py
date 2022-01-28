import pyttsx3
import speech_recognition as sr
import pywhatkit
import urllib.request
import json



listener = sr.Recognizer()

engine = pyttsx3.init()

name = 'angel'

key = 'AIzaSyCYM7PN1-PfAM2zh8uCUFdBUWHGbjJQftU'

voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)



def talk(text):
	engine.say(text)
	engine.runAndWait()



def listen():
	try:
		with sr.Microphone() as source:
			print('Escuchando...')
			voice = listener.listen(source)
			rec = listener.recognize_google(voice)
			rec = rec.lower()
			if name in rec:
				rec = rec.replace(name,'')
				print(rec)

	except:
		print('no se puede acceder al microfono')
		pass
	return rec


#cosas cool de ser ingeniero en sistemas

def run():
	rec = listen()
	
	if 'reproduce' in rec:
		music = rec.replace('reproduce','')
		talk('reproduciendo'+music)
		pywhatkit.playonyt(music)
		

run()
