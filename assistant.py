import speech_recognition as sr
import pyttsx3 as ts
import pywhatkit
import datetime
import random
import pyjokes
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import wikipedia

listener = sr.Recognizer()
engine = ts.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 170)
chrome_driver_path = r"C:\Users\HP\Documents\Chrome Web Driver\chromedriver.exe"
doing = ["I am Building my AI Muscles", "Thinking about my creator", "Thinking about you"]


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'Liz' in command:
                command = command.replace('Liz', '')
                print(command)
    except:
        pass
    return command


def run_max():
    command = take_command()
    if 'play' in command:
        song = command.replace('play', '')
        talk("Playing" + song)
        print(song)
        pywhatkit.playonyt(song)
        exit(0)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk("Current Time is " + time)
    elif 'what are you doing' in command:
        do = random.choice(doing)
        print(do)
        talk(do)
    elif 'quit' in command:
        print(command)
        talk("Bye Have a Good Day Ahead")
        exit(0)
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'search' in command:
        query = command.replace('search', '')
        talk("Opening Chrome")
        search(query)
    elif 'who the heck is' in command:
        person = command.replace('who the heck is', '')
        print(person)
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'say hi to' in command:
        greet = command.replace('say hi to', 'hi')
        talk(greet)
    else:
        talk("Please Repeat")


def search(query):
    driver = webdriver.Chrome(executable_path=chrome_driver_path)
    driver.get("https://www.google.com/")
    search = driver.find_element_by_tag_name(name="input")
    search.send_keys(query)
    search.send_keys(Keys.ENTER)
    stats = driver.find_element_by_id("result-stats").text
    print(stats)
    talk(stats)


while True:
    run_max()
