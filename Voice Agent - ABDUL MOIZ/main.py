import speech_recognition as sr
import webbrowser
import pyttsx3

reccognizer = sr.Recognizer()
engine = pyttsx3.init()


def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    print(c)

if __name__ == "__main__":
    speak("ABDUL MOIZ VOICE BOT is initialize......")
    while True:
        r = sr.Recognizer()
        

        print("recognizing")
        try:
            with sr.Microphone() as source:
                print("listening...")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
            word = r.recognize_google(audio)
            if(word.lower() == "i need help"):
                speak("yeah please tell me how may I help you?")
                
                # listening for users audio
                with sr.Microphone() as source:
                    print("MOIZ VOICE BOT IS ACTIVE")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)

        except Exception as e:
            print(f"Error, {e}")
