import speech_recognition

recognizer = speech_recognition.Recognizer()

with speech_recognition.Microphone() as source:
    print("say something :")
    audio = recognizer.listen(source)

print(" it looks you said : ")
print(recognizer.recognize_google(audio))