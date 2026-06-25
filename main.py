#Standard Libraries

import os
import random
import asyncio
import webbrowser
import ctypes
from datetime import datetime

#Third Party Libraries

import speech_recognition as sr
import requests
import edge_tts
import pygame
import wikipedia
import pyautogui
import psutil
import google.generativeai as genai

#PyCAW

from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume






GEMINI_API_KEY = "...."
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-2.5-flash")



recognizer = sr.Recognizer()

async def speak_async(text):
    communicate = edge_tts.Communicate(
        text=text,
        voice="en-GB-RyanNeural" 
    )

    await communicate.save("voice.mp3")

    pygame.mixer.init()
    pygame.mixer.music.load("voice.mp3")
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    pygame.mixer.quit()
    os.remove("voice.mp3")




def speak(text):
    asyncio.run(speak_async(text))

def set_volume(level):
    devices = AudioUtilities.GetSpeakers()
    
    print(type(devices))
    print(dir(devices))
    
    interface = devices.Activate(
        IAudioEndpointVolume._iid_,
        CLSCTX_ALL,
        None
    )

    volume = cast(interface, POINTER(IAudioEndpointVolume))

    volume.SetMasterVolumeLevelScalar(level / 100, None)

def ask_gemini(question):
     try:
         response = model.generate_content(question)
         return response.text
     except Exception as e:
         print(e)
         return "Sorry, I couldn't get a response from Gemini."
     
     
responses = [
    "Yes, fuhrer?",
    "How can I help you fuhrer?",
    "I'm listening, fuhrer.",
    "What can I do for you? fuhrer?",
    "At your service. fuhrer.",
    "Go ahead.fuhrer.",
]    

while True:
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print("Listening...")

        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
            
        except sr.WaitTimeoutError:
            print("Listening timed out while waiting for phrase to start")
            continue    
            

    try:
        command = recognizer.recognize_google(audio).lower()
        print("You said:", command)
        
        wake_words = ["merry", "hey merry", "ok merry", "hello merry", "hi merry", "wake up merry", "hello buddy", "hey buddy", "ok buddy", "hi buddy", "wake up buddy"]
        if any(wake_word in command for wake_word in wake_words):
            print("Wake word detected.")
            speak(random.choice(responses))
            while True:
                with sr.Microphone() as source:
                    print("Listening for command...")
                    audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
            
                command = recognizer.recognize_google(audio).lower()
                print("Command received:", command)
            
              
                
    

        if "youtube" in command:
            speak("Opening YouTube")
            webbrowser.open("https://youtube.com")

        elif "google" in command:
            speak("Opening Google")
            webbrowser.open("https://google.com")
            
        elif "time" in command:
            current_time = datetime.now().strftime("%I:%M %p")

            print(current_time)

            speak(f"The time is {current_time}")

        
        elif "notepad" in command:
            speak("Opening Notepad")
            os.system("notepad.exe")
        
        elif "calculator" in command:
            speak("Opening Calculator")
            os.system("calc.exe")
            
        
        
        elif "visual studio code" in command or "vscode" in command:
            speak("Opening Visual Studio Code")
            os.system("code") 
            
        elif "date" in command:
            current_date = datetime.now().strftime("%Y-%m-%d")
            print(current_date)
            speak(f"Today's date is {current_date}")
            
        elif "chat g p t" in command or "chatgpt" in command:
            speak("Opening Chat GPT")
            webbrowser.open("https://chatgpt.com")    
        
        elif "github" in command:
            speak("Opening GitHub")
            webbrowser.open("https://github.com")      
            
        elif "gmail" in command:
            speak("Opening Gmail")
            webbrowser.open("https://gmail.com")
            
        elif "who is" in command:
            try:
                person = command.replace("who is", "").strip()
                speak(f"Searching for {person} on Wikipedia")
                
                result = wikipedia.summary(person, sentences=2)
                print(result)
                speak(result)
            except Exception:
                speak("Sorry, I couldn't find information on that person.")
                
        elif "take screenshot" in command:
            speak("Taking screenshot")

            screenshot = pyautogui.screenshot()

            screenshot.save("screenshot.png")

            speak("Screenshot saved successfully")     
            
        elif "weather" in command:
            try:
                city= command.replace("weather in", "").strip()
                if city == "":
                    city = "Jaunpur"
                    
                api_key = "..." 
                url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
                response = requests.get(url)
                data = response.json()
                
                temperature = data["main"]["temp"]
                description = data["weather"][0]["description"]
                
                answer = f"The current temperature in {city} is {temperature} degrees Celsius with {description}."
                print(answer)
                speak(answer)
                
            except Exception as e:
                print(e)
                speak("Sorry, I couldn't fetch the weather information.")       
                
        elif "open spotify" in command:
            speak("Opening Spotify")
            os.system("start spotify")
            
            
        elif "play music" in command:
            speak("Playing music")

            song_path = r"C:\Users\shaur\OneDrive\Desktop\MERRYIOS\macarena_slowed.mp3"

            os.startfile(song_path)    
            
        elif "battery" in command:
            battery = psutil.sensors_battery()
            percent = battery.percent
            answer = f"The battery is at {percent} percent."
            print(answer)
            speak(answer)
            
        elif "ram" in command:
            memory = psutil.virtual_memory()

            used = round(memory.used / (1024 ** 3), 2)
            total = round(memory.total / (1024 ** 3), 2)

            answer = f"You are using {used} gigabytes out of {total} gigabytes of RAM"
            print(answer)
            speak(answer)
            
        elif "cpu" in command:
            cpu_usage = psutil.cpu_percent(interval=1)

            answer = f"The CPU usage is {cpu_usage} percent"

            print(answer)
            speak(answer)    
            
        elif "news" in command:
            try:
                api_key = "...."
                url = url = (f"https://newsapi.org/v2/everything?"
f"q=India&sortBy=publishedAt&language=en&apiKey={api_key}"
)
                response = requests.get(url)    
                news= response.json()
                print(news)
              
                articles = news["articles"][:5]
                speak("Here are the top news headlines:")

                for article in articles:
                    title = article["title"]
                    print(title)
                    speak(title)
                    
            except Exception as e:
                print(e)
                speak("Sorry, I couldn't fetch the news.")     
                
        elif "volume" in command:
            print("Volume command detected")
            if "up" in command or "increase" in command:
                set_volume(100)
                speak("Volume increased to maximum")
            elif "down" in command or "decrease" in command:
                set_volume(40)
                speak("Volume decreased to minimum")
            elif "mute" in command:
                set_volume(0)
                speak("Volume muted")    
    
        elif"lock pc" in command:
            speak("Locking the PC")
            ctypes.windll.user32.LockWorkStation()
            
        elif "shutdown" in command:
            speak("Shutting down the PC")
            os.system("shutdown /s /t 1")
            
        elif "restart" in command:
            speak("Restarting the PC")
            os.system("shutdown /r /t 1")
            
        elif "cancel shutdown" in command:
            speak("Cancelling the shutdown")
            os.system("shutdown /a")    
            
        elif "tell me"  in command or "what is" in command or " who is" in command or "explain" in command:
            answer = ask_gemini(command)
            print(answer)
            speak(answer)            
  
  

        elif "thanks buddy" in command:
            speak("HAVE A GOOD DAY bOSS")
            break     

        else:
            speak("Sorry, I don't know that command yet.")

    except Exception as e:
        print("Error:", e)
        print("Sorry, I couldn't understand.")