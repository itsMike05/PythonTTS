
import pyttsx3 as tts

engine = tts.init()

engine.setProperty('rate', 150)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)

engine.say("Initializing text to speech models")
engine.say("Performing calculations")
print(engine.getProperty('rate'))
engine.runAndWait()


voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.say("What is up guys, Rick Kackis here")
print(engine.getProperty('rate'))
engine.runAndWait()

engine.stop()


