import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime

# Initialize text-to-speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Speed of speech

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

def get_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        
        try:
            command = recognizer.recognize_google(audio)
            print("You said:", command)
            return command.lower()
        except sr.UnknownValueError:
            speak("Sorry, I did not catch that.")
            return ""
        except sr.RequestError:
            speak("Network error.")
            return ""

def run_assistant():
    while True:
        command = get_command()

        if 'hello' in command:
            speak("Hello! How can I help you?")
        
        elif 'time' in command:
            current_time = datetime.datetime.now().strftime('%I:%M %p')
            speak(f"The current time is {current_time}")

        elif 'date' in command:
            current_date = datetime.datetime.now().strftime('%B %d, %Y')
            speak(f"Today's date is {current_date}")

        elif 'search' in command:
            query = command.replace('search', '')
            speak(f"Searching the web for {query}")
            pywhatkit.search(query)

        elif 'exit' in command or 'stop' in command:
            speak("Goodbye!")
            break

        else:
            speak("Please say a valid command.")

# Run the assistant
run_assistant()