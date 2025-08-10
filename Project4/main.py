
import speech_recognition as sr
import webbrowser
import pyttsx3
from datetime import datetime
import requests
import pyjokes
import threading
import tkinter as tk
from datetime import datetime
import wikipedia
import smtplib
import os

recognizer = sr.Recognizer()
engine = pyttsx3.init()
# Set properties for the speech engine
engine.setProperty('rate', 150)
engine.setProperty('volume', 1.0)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif"open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif"open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")

    else:
        speak("")
if __name__ == "__main__":
    speak("Initializing Jarvis....")
    while True:
        r = sr.Recognizer()
        word = ""  # Initialize word to avoid UnboundLocalError
        
        #Listen for the wake work "jarvis"
        #obtain audio from the microphone
        r = sr.Recognizer()
        print("Recognising...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
            word = r.recognize_google(audio)
            if (word.lower() == "jarvis"):
                speak("Ya")
                # listen for command
                with sr.Microphone() as source:
                    print("Jarvis active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    processCommand(command)
        except Exception as e:
            print("Error: {0}".format(e))
            word = ""  # Ensure word is always defined
          

        # Additional advanced features for Jarvis

        # 1. Add more commands
        if 'time' in word.lower():
            now = datetime.now().strftime("%H:%M")
            speak(f"The current time is {now}")

        elif 'weather' in word.lower():
            api_key = "your_openweathermap_api_key"
            city = "your_city"
            url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
            try:
                response = requests.get(url)
                data = response.json()
                if data["cod"] == 200:
                    temp = data["main"]["temp"]
                    desc = data["weather"][0]["description"]
                    speak(f"The weather in {city} is {desc} with a temperature of {temp} degree Celsius.")
                else:
                    speak("Sorry, I couldn't fetch the weather.")
            except:
                speak("Sorry, I couldn't fetch the weather.")

        elif 'joke' in word.lower():
            joke = pyjokes.get_joke()
            speak(joke)

        elif 'exit' in word.lower() or 'quit' in word.lower():
            speak("Goodbye!")
            break

        # 2. Add a simple GUI for virtual appearance

        def run_gui():
            root = tk.Tk()
            root.title("Jarvis Virtual Assistant")
            root.geometry("400x200")
            label = tk.Label(root, text="Jarvis is running...", font=("Arial", 16))
            label.pack(pady=50)
            root.mainloop()

        gui_thread = threading.Thread(target=run_gui, daemon=True)
        gui_thread.start()

        # 3. Add greeting based on time
        hour = datetime.now().hour
        if hour < 12:
            greet = "Good morning!"
        elif hour < 18:
            greet = "Good afternoon!"
        else:
            greet = "Good evening!"
        speak(greet)

        # 4. Add Wikipedia search
        if 'wikipedia' in word.lower():
            speak("What should I search on Wikipedia?")
            with sr.Microphone() as source:
                audio = r.listen(source)
                query = r.recognize_google(audio)
                try:
                    result = wikipedia.summary(query, sentences=2)
                    speak(result)
                except:
                    speak("Sorry, I couldn't find anything on Wikipedia.")

        # 5. Add note taking
        if 'note' in word.lower():
            speak("What should I write in your note?")
            with sr.Microphone() as source:
                audio = r.listen(source)
                note = r.recognize_google(audio)
                with open("jarvis_notes.txt", "a") as f:
                    f.write(note + "\n")
                speak("Note saved.")

        # 6. Add email sending (requires setup)
        if 'email' in word.lower():
            speak("Who is the recipient?")
            with sr.Microphone() as source:
                audio = r.listen(source)
                recipient = r.recognize_google(audio)
            speak("What is the message?")
            with sr.Microphone() as source:
                audio = r.listen(source)
                message = r.recognize_google(audio)
            try:
                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                server.login('your_email@gmail.com', 'your_password')
                server.sendmail('your_email@gmail.com', recipient, message)
                server.quit()
                speak("Email sent successfully.")
            except:
                speak("Sorry, I couldn't send the email.")

        # 7. Add system commands
        if 'shutdown' in word.lower():
            speak("Shutting down the system.")
            os.system("shutdown /s /t 1")
        elif 'restart' in word.lower():
            speak("Restarting the system.")
            os.system("shutdown /r /t 1")
            
           
   

    # Recognize speech using Sphinx
    

