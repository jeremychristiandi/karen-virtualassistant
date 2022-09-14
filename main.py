import speech_recognition as sr
import pyttsx3 as ptt
import pyaudio
import pywhatkit as pwk
import datetime
import webbrowser as web
import wikipedia as wiki
import pyjokes as pj

r = sr.Recognizer()

#Inisialisasi engine
engine = ptt.init()

#Mengganti suara default ke wanita
engine.setProperty('rate', 170)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

global name, chromePath
chromePath = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
name = 'karen'

def speak(command):
    engine.say(command)
    engine.runAndWait()

print("Karen's here! How can I help you?")
speak("Karen's here! How can I help you?")

def runCommand():
    global command

    try:
        with sr.Microphone() as source:
            # Kalibrasi suara berdasarkan suara yang ada di background.
            r.adjust_for_ambient_noise(source, duration=1)

            # Deteksi suara input oleh user.
            print("Listening...")
            audio = r.listen(source)

            # Menggunakan google untuk mendeteksi input suara
            command = r.recognize_google(audio)
            print(command)
            print()
    except:
        print('Cannot recognize audio... Exiting the program')
        speak('Cannot recognize audio... Exiting the program')
        return 0
    return command

def runEngine():
    global command
    command = runCommand()

    if command == 0:
        return 0

    #Memerintahkan karen untuk memainkan lagu di youtube
    elif 'play' in command:
        song = command.replace('play', '')
        print('Playing ' + song + ' for you')
        speak('Playing ' + song + ' for you')
        pwk.playonyt(song)

    elif 'com' in command:
        command = command.replace('open', '')
        print('Opening url: ' + command)
        speak('Opening ' + command + ' for you.')
        web.get(chromePath).open(command)

    # Memerintahkan karen untuk memberi tahu tanggal hari ini
    elif 'date' in command:
        date = datetime.date.today()
        print(date)
        speak('The current date is ' + str(date))

    #Memerintahkan karen untuk memberi tahu waktu saat ini
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        speak('The current time is ' + time)

    elif 'who is' in command:
        subject = command.replace('who is', '')
        result = wiki.summary(subject, sentences=2)
        print(result)
        speak(result)

    #Memerintahkan karen untuk membuat joke
    elif 'joke' in command:
        joke = pj.get_joke()
        print(joke)
        speak(joke)

    elif 'love you' in command:
        print('I am sorry...')
        print('I think you are too good for me.')
        speak('I am sorry...I think you are too good for me.')

    elif 'hate you' in command:
        print('I am sorry...')
        print('I do not expect you to feel that way.')
        speak('I am sorry. I do not expect you to feel that way.')

    elif 'who are you' in command:
        print('Hi! My name is Karen. I am happy to meet you.')
        speak('Hi! My name is Karen. I am happy to meet you.')

    else:
        print("I don't understand! Let me go to the restroom.")
        speak("I don't understand! Let me go to the restroom.")

while True:
    print()
    command = runEngine()
    if command == 0:
        break
    else:
        continue


