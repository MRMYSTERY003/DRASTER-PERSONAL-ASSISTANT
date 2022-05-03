import datetime
import pyttsx3 as speaker # pip install pyttsx3
import speech_recognition as sr #pip install SpeechRecognition
from GoogleNews import GoogleNews as news_api #pip install googlenews
import psutil as system # pip install psutil
import wikipedia as wiki # pip install wikipedia
import pywhatkit as kit # pip install pywhatkit
import webbrowser as browser
import subprocess
import wolframalpha as brain #pip install wolframalpha
import random
import os

voice_engine = speaker.init()

voices = voice_engine.getProperty('voices')
voice_engine.setProperty('voice', voices[0].id)

voice_engine.setProperty('rate',175)


#convert the audio to text
def take_command():
    try:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            print('listerning....')
            audio = r.listen(source)
            text = r.recognize_google(audio)
            print('you said: ' + text)
            return (text.lower())
    except:
        print('unable to recognize voice')
        return '-010-'

#convert text to audio
def speak(text):
    print(text)
    voice_engine.say(text)
    voice_engine.runAndWait()

#fetches news
def get_news():
    news = news_api('en','d')
    news.search('Tamil Nadu')
    news.get_page(1)
    news.result()
    news_text = set(news.get_texts())
    return list(news_text)

def get_sysinfo():
    freq = system.cpu_freq()
    current_freq = f'current frequency of the cpu is {str(freq.current)} megaherts' # get the current frequency of the cpu

    return current_freq

def intro():
    speak('awaking system protocols')
    speak('checking network protocols')
    speak('getting system information, cpu usage')
    info = get_sysinfo()
    speak(info)
    speak('system is in optimal condition')
    hour = datetime.datetime.now().hour

    if 0 > hour < 12:
        speak('Good Morning sir')
    elif 12 > hour > 18 :
        speak('good afternoon sir')
    else:
        speak('good evening sir')

    speak('i am your personal assistant, draster 2 point o')
    speak('how can i help you sir')

def wikipedia_search(query):
    speak('searching on wikipedia')
    query = query.replace('wikipedia','')
    try:
        res = wiki.summary(query, 3)
        speak(res)
    except:
        speak('content not found on google, searching on google')
        kit.search(query)
        speak('these are the results found on google')

def play_on_yt(query):
    video = query.replace('youtube','')
    video = query.replace('and play','')
    speak('openning youtube')
    kit.playonyt(video)

def got_to_site(site):
    google = 'https://google.com'
    insta = 'https://instagram.com'
    classroom = 'https://classroom.google.com'
    github = 'https://github.com'
    if 'google' in site:
        browser.open(google)
        speak('openning google')
    elif 'instagram' in site:
        browser.open(insta)
        speak('openning instagram')
    elif 'classrooom' in site:
        browser.open(classroom)
        speak('openning google classroom')
    elif 'github' in site:
        browser.open(github)
        speak('openning github')
    else:
        speak('the specified site is not in my database, try updating it...')


def play_offline_song():
    song_dir = 'C:\\Users\\Admin\\Desktop\temp\\jarvis\\songs'
    songs = os.listdir(song_dir)
    index = random.randint(0,len(songs)-1)
    full_path = os.path.join(song_dir,songs[index])
    os.startfile(full_path)


def take_notes():
    time_now = datetime.datetime.now().strftime('%H %M %p')
    speak('enter the path of the file ,where you need to save (by default it is saved in desktop')
    file_path = input('Path :  ') or 'C:\\Users\\kamat\\Desktop\\'
    if not file_path.endswith('\\'):
        file_path += '\\'
    speak('enter the name of the file')
    name = input('File name : ')
    full_path = file_path+name+'.txt'
    file = open(full_path, 'a+')
    speak('write your notes here ,when completed hit enter to save')
    file.write('file opened at: '+time_now+'\n\n')
    content = input('enter the notes: ')
    file.writelines(content)
    file.close()
    speak('you can find the file at desktop with the name of'+name)

def open_apps(name):
    notepad = 'C:\\Windows\\system32\\notepad.exe'
    paint = 'C:\\Windows\\system32\\mspaint.exe'

    if 'notepad' in name:
        speak('openning notepad')
        os.startfile(notepad)
    elif 'paint' in name:
        speak('openning paint')
        os.startfile(paint)

def close_apps(name):
    notepad = 'notepad.exe'
    paint = 'mspaint.exe'

    if 'notepad' in name:
        speak('terminating notepad')
        subprocess.call(['taskkill', '/F' ,'/IM', notepad])
    elif 'paint' in name:
        speak('terminating paint')
        os.startfile(['taskkill', '/F' ,'/IM', paint])    


def query_handler(question):
    api_key = 'your-api-id'
    client = brain.Client(api_key)
    result = client.query(question)
    speak('analysing your query')
    result = next(result.results).text
    speak(result)


run  = True

intro()

while run:
    command = take_command()
    if command != '-010-':
        
        if 'who are you' in command or 'introduce yourself' in command or 'tell me about yourself' in command:
            speak('hi i am draster, i am your personal assistant, i am here to help you with various tasks, like playing musics online and offline, search for information on internet, operate application, taking notes, and many more')

        elif 'news' in command:
            news = get_news()
            for i in news:
                speak(i)

        elif 'youtube' in command:
            play_on_yt(command)

        elif 'play song on pc' in command or 'song' in command:
            play_offline_song()
        
        elif 'open notepad' in command:
            open_apps('notepad')
            
        elif 'close notepad' in command:
            close_apps('notepad')
        
        elif  'wikipedia' in command:
            wiki(command)
        
        elif 'who' in command or 'what' in command or 'when' in command or 'how' in command:
            query_handler(command)

        elif 'open google' in command or 'google' in command:
            got_to_site('google')
        
        elif 'open classroom' in command or 'classroom' in command:
            got_to_site('classroom')
        
        elif 'open github' in command or 'github' in command:
            got_to_site('github')
        
        elif 'exit' in command or 'bye' in command :
            run = False
            speak('thank you for spending time with me, see you later sir')
        


    else:
        print('i cannot understand you')


