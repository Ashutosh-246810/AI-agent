# JARVIS Desktop AI Assistant

JARVIS is a simple voice-activated desktop assistant built using Python. It can recognize voice commands and perform basic tasks such as opening websites, searching information, playing music, telling the current time, and launching desktop applications.

## Features

- Voice command recognition
- Wikipedia search and summary
- Open common websites (YouTube, Google, Stack Overflow)
- Play local music files
- Report current system time
- Open Visual Studio Code or other desktop applications
- Search the web using pywhatkit
- Text-to-speech responses using the Windows voice engine

## Requirements

Install the following Python libraries before running the project:

```
pip install pyttsx3 SpeechRecognition wikipedia pywhatkit pipwin
pipwin install pyaudio
```

## Usage

1. Clone the repository or copy the code to your local machine.
2. Update file paths for music and application directories as needed.
3. Run the script using Python:

```
python jarvis.py
```

4. Speak your commands such as:
   - "Search Wikipedia for Python"
   - "Open YouTube"
   - "Play music"
   - "What is the time?"
   - "Open code"

5. Say "exit" or "stop" to close the assistant.

## Customization

- You can modify the `music_dir` and `codePath` to match your system paths.
- Additional features like sending emails, fetching weather reports, or adding GUI can be integrated as needed.

## Disclaimer

This is a basic project intended for educational and personal use. Voice recognition and accuracy may vary based on system configuration and environment.
