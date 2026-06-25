MERRIOS - An AI Voice Assistant

MERRIOS is a Python-based AI voice assistant that can perform various tasks through voice commands, including opening applications, searching information, controlling system functions, checking weather, reading news, and interacting with Google's Gemini AI model.

Features

- Voice-activated assistant with customizable wake words
- AI-powered responses using Google Gemini
- Open websites such as YouTube, Google, GitHub, Gmail, and ChatGPT
- Wikipedia search and summaries
- Weather information
- Latest news headlines
- System controls:
  - Volume control
  - Lock PC
  - Shutdown PC
  - Restart PC
- Screenshot capture
- Battery, CPU, and RAM monitoring
- Text-to-speech responses using Edge TTS
- Music playback support

Technologies Used

- Python
- Google Gemini API
- SpeechRecognition
- Edge TTS
- Pygame
- Wikipedia
- Requests
- PyAutoGUI
- Psutil
- PyCAW

Installation

1. Clone the Repository

git clone https://github.com/Shauryashikhergupta/MERRIOS-AN-AI-CHAT-BOT.git
cd MERRIOS-AN-AI-CHAT-BOT

2. Install Dependencies

pip install -r requirements.txt

API Configuration

This project requires external API keys.

For security reasons, API keys are NOT included in this repository.

You must add your own API keys before running the project.

Required APIs:

- Google Gemini API
- OpenWeather API
- NewsAPI

Replace the placeholder values in the code with your own API keys:

GEMINI_API_KEY = "YOUR_GEMINI_API_KEY"

api_key = "YOUR_WEATHER_API_KEY"

api_key = "YOUR_NEWS_API_KEY"

Running the Project

python main.py

Wake Words

MERRIOS can be activated using phrases such as:

- Merry
- Hey Merry
- Hello Merry
- Hi Merry
- Wake Up Merry
- Hey Buddy
- Hello Buddy
- Wake Up Buddy

Example Commands

- Open YouTube
- Open Google
- Open GitHub
- What is Artificial Intelligence?
- Who is Alan Turing?
- Weather in Delhi
- Take Screenshot
- Lock PC
- Shutdown PC
- Restart PC
- Play Music
- Battery Status
- CPU Usage
- RAM Usage

Project Status

This project is actively being developed and improved with new AI-powered features and voice commands.

Author

Shaurya Shikher Gupta

License

This project is intended for educational and learning purposes.