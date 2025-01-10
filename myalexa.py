import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import webbrowser

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Female voice


def talk(text):
    engine.say(text)
    engine.runAndWait()
    


def take_command():
    try:
        with sr.Microphone() as source: 
            print('Listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(f"Command: {command}")
    except:
        pass
    return command


def run_alexa():
    command = take_command()
    if 'play' in command:
        song = command.replace('play', '')
        talk('Playing ' + song)
        pywhatkit.playonyt(song)

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('The current time is ' + time)

    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        talk(info)

    elif 'search for' in command:
        query = command.replace('search for', '')
        url = f"https://www.google.com/search?q={query}"
        talk(f"Searching for {query} on Google.")
        webbrowser.open(url)

    elif 'open youtube' in command:
        talk('Opening YouTube.')
        webbrowser.open('https://www.youtube.com')

    elif 'open google' in command:
        talk('Opening Google.')
        webbrowser.open('https://www.google.com')

    elif 'joke' in command:
        talk(pyjokes.get_joke())

    elif 'how are you' in command:
        talk("I'm just a program create by My lovely Sir Ali Akbar, but I'm doing great! How can I help you?")

    elif 'date' in command:
        today = datetime.date.today().strftime('%B %d, %Y')
        talk(f"Today's date is {today}.")

    elif 'goodbye' in command or 'exit' in command or 'quit' in command:
        talk("Goodbye! Have a great day!")
        exit()

    else:
        talk("Sorry, I didn't understand that. Please say it again.")


# Run Alexa in a loop
while True:
    run_alexa()
