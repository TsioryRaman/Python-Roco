#IMPORT
import speech_recognition as sr

r = sr.Recognizer()
print(sr.Microphone.list_microphone_names()[5])
	
micro = sr.Microphone()
with micro as source:
    print("Speak!")
    audio_data = r.listen(source)
    print("End!")
result = r.recognize_google(audio_data,language="fr-FR")
print (">", result)