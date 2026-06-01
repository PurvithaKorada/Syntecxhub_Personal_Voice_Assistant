import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime
import os
import tkinter as tk
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('rate', 150)
engine.setProperty('volume', 1.0)
engine.setProperty('voice', voices[1].id)
def speak(text):
    output_label.config(text="Assistant: " + text)
    engine.say(text)
    engine.runAndWait()
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        output_label.config(text="Listening...")
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio)
        command = command.lower()
        user_label.config(text="You: " + command)
        if "open youtube" in command:
            speak("Opening YouTube")
            webbrowser.open("https://youtube.com")
        elif "open google" in command:
            speak("Opening Google")
            webbrowser.open("https://google.com")
        elif "open github" in command:
            speak("Opening GitHub")
            webbrowser.open("https://github.com")
        elif "time" in command:
            current_time = datetime.datetime.now().strftime("%I:%M %p")
            speak("Current time is " + current_time)
        elif "date" in command:
            today = datetime.datetime.now().strftime("%d-%m-%Y")
            speak("Today's date is " + today)
        elif "hello" in command:
            speak("Hello, nice to meet you")
        elif "open calculator" in command:
            speak("Opening Calculator")
            os.system("calc")
        elif "open notepad" in command:
            speak("Opening Notepad")
            os.system("notepad")
        elif "open paint" in command:
            speak("Opening Paint")
            os.system("mspaint")
        elif "exit" in command:
            speak("Goodbye")
            root.destroy()
        else:
            speak("Command not found")
    except:
        speak("Sorry, I did not understand")
root = tk.Tk()
root.title("Voice Assistant")
root.geometry("700x550")
title = tk.Label(
    root,
    text="Personal Voice Assistant",
    font=("Arial", 20)
)
title.pack(pady=20)
button = tk.Button(
    root,
    text="Start Listening",
    command=listen,
    font=("Arial", 14)
)
button.pack(pady=20)
user_label = tk.Label(
    root,
    text="",
    font=("Arial", 12)
)
user_label.pack(pady=10)
output_label = tk.Label(
    root,
    text="",
    font=("Arial", 12)
)
output_label.pack(pady=10)
commands = tk.Label(
    root,
    text="""
Sample Commands:
Open YouTube
Open Google
Open GitHub
Open Calculator
Open Notepad
Open Paint
What is the time
What is today's date
Hello
Exit
""",
    font=("Arial", 11)
)
commands.pack(pady=20)
root.after(1000, lambda: speak("Hello, I am your voice assistant"))
root.mainloop()
