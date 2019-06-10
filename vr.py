import speech_recognition as vr

r = vr.Recognizer()
with vr.Microphone() as source:
    print("Speak Anything :")
    audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print("You said : {}".format(text))
    except:
        print("Unable to hear you, please repeat.")
        
