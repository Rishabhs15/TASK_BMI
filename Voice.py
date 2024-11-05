pip install SpeechRecognition pyttsx3

import speech_recognition as sr
import pyttsx3
from datetime import datetime
import webbrowser

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio).lower()
        print(f"You said: {command}")
    except sr.UnknownValueError:
        speak("Sorry, I didn't catch that. Could you please repeat?")
        return None
    except sr.RequestError:
        speak("Sorry, I'm having trouble connecting to the recognition service.")
        return None
    return command

def respond_to_command(command):
    if "hello" in command:
        speak("Hello! How can I assist you today?")
    elif "time" in command:
        current_time = datetime.now().strftime("%I:%M %p")
        speak(f"The current time is {current_time}.")
    elif "date" in command:
        current_date = datetime.now().strftime("%B %d, %Y")
        speak(f"Today’s date is {current_date}.")
    elif "search" in command:
        speak("What would you like me to search for?")
        query = listen()
        if query:
            url = f"https://www.google.com/search?q={query}"
            speak(f"Searching for {query}")
            webbrowser.open(url)
    else:
        speak("Sorry, I didn’t understand that command.")

def main():
    speak("Hello! I am your voice assistant. How can I help you?")
    while True:
        command = listen()
        if command:
            if "exit" in command or "quit" in command:
                speak("Goodbye!")
                break
            else:
                respond_to_command(command)

if _name_ == "_main_":
    main()