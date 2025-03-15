import speech_recognition as sr
import webbrowser
import pyttsx3
# from openai import OpenAI
import cohere
import os
from dotenv import load_dotenv

load_dotenv()
# Get API key from environment variables
api_key = os.getenv("API_KEY")

reccognizer = sr.Recognizer()
engine = pyttsx3.init()


def speak(text):
    engine.say(text)
    engine.runAndWait()

def aiProcess(command):
    # Initialize Cohere API client
    co = cohere.Client(api_key)  # Replace with your actual API key

    # Generate AI response
    response = co.chat(
        model="command-r",
        message=command,
        temperature=0.7, preamble="You are a virtual assistant of ABDUL MOIZ, skilled in UI/UX design and MERN Stack development. You function like Alexa and Google Cloud."
    )

    return response.text

    # for OPENAI
    # client = OpenAI(api_key)

    # completion = client.chat.completions.create(
    # model="gpt-4o-mini",
    # store=True,
    # messages=[
    #     {"role": "user", "content": "you are a virtual assistant of ABDUL MOIZ skilled in UI UX design and also a MERN Stack development you work as a Alexa and google cloud"},
    #     {"role": "user", "content": command}
    # ]
    # )

    # return completion.choices[0].message.content

def processCommand(c):
    print("PROCESS", c)
    if "google" in c.lower():
        webbrowser.open("https://google.com")
    elif "facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "play nusrat" in c.lower():
        webbrowser.open("https://www.youtube.com/watch?v=CXT4ASeh1L4")
    else:
        output = aiProcess(c)
        print(output)
        speak(output)

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
            if word.lower() == "i need help":
                speak("yeah please tell me how may I help you?")

                # listening for users audio
                with sr.Microphone() as source:
                    print("MOIZ VOICE BOT IS ACTIVE")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    print("COMMAND", command)
                    processCommand(command)

        except Exception as e:
            print(f"Error, {e}")
