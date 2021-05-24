#improyting all the required modules
import speech_recognition as sr
import pyttsx3 as tt
import datetime as date
import shutil
import smtplib
import wikipedia as wiki
import os
import webbrowser as wbb
import pywhatkit as pw
import random
import wolframalpha as wo
import psutil
import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver as wb
from pynput.mouse import Button, Controller
import datetime
import subprocess
from pygame import mixer 

#initilizing the required modules
mouse = Controller()
en = tt.init()
vo = en.getProperty('voices')
en.setProperty('voice', vo[3].id)
en.setProperty('rate', 160)
go = 'https://www.google.com'
yt = 'https://www.youtube.com'
insta = 'https://www.instagram.com'
wp = 'https://web.whatsapp.com/'
woappid = '*****YOUR WOLFRAMALPHA API KEY HERE*****'


#defining the required funcitons

def speak(audio):#used to convert the text to audio
    en.say(audio)
    en.runAndWait()



def take_command():#convert the audio to text
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
        return 'sr030'
 


def get_sysinfo():#used to get the system cpu usage
    info = []
    cpufreq = psutil.cpu_freq()
    info.append(f"Current Frequency of the CPU is: {cpufreq.current:.2f} Megahertz")
    info.append("CPU Usage Per Core:")
    for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
        info.append(f"Core {i}: {percentage}%")
    info.append(f"Total CPU Usage: {psutil.cpu_percent()}%")
    return info



def browser(site):#used to open the browse and search in google
    while True:   
        if ('google' in site):
            speak('openning google')
            driver = wb.Chrome("F:\pythonProject\chromedriver.exe")
            driver.get(go)
            time.sleep(2)
            speak('what do you want to search sir..')
            search = take_command()
            if 'sr030' not in search:
                bar = driver.find_element_by_name('q')
                bar.send_keys(search, Keys.ENTER)
                while True:
                    print('...........__________.............')
                    speak('do you what to exit')
                    exit = take_command()
                    if 'sr030' not in exit:
                        if('down' in exit) or ('scroll down' in exit):
                            for i in range(5):
                                mouse.scroll(0, -1)
                                time.sleep(0.5)
                        elif('up' in exit) or ('scroll up' in exit):
                            for i in range(5):
                                mouse.scroll(0, 1)
                                time.sleep(0.5)
                        if ('yes' in exit) or ('of course' in exit) or ('close' in exit) or ('exit' in exit):
                            speak('closing browser..')
                            driver.close()
                            return 'exit'
                    else:
                        speak('hmm')
                        continue
            else:
                speak('try again')
                driver.close()
                continue
     
        elif 'exit' in site:
            print('definition loop')
            return 'exit'
        else:
            speak('could not recognize, try again')
            return       
    


def wish_me():
    os.startfile('C:\\Program Files\\Rainmeter\\Rainmeter.exe')
    speak('awaking system protocols')
    speak('checking network protocols') 
    speak('getting system information , cpu usage..')
    info = get_sysinfo()
    for i in info:
        speak(i)
    speak('system is in optimal condition')
    hu = int(date.datetime.now().hour)
    if(hu > 0 and hu < 12):
        speak('Good Morning sir!')
    elif(hu > 12 and hu < 18):
        speak('Good Afternoon sir!')
    else:
        speak('Good evening sir!')
    speak('i am your personal Assistant, Draster 2 point o')
    speak('How can i help you sir?')

    


def send_email(to, content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('****YOUR MAIL ID****','****YOUR MAIL PASSWORD****')
    server.sendmail('****YOUR MAIL ID****',to,content)
    server.close()


wish_me()

#program starts here
if __name__ =='__main__':
    lambda : os.system('cls')# clearing the terminal

    mrun = True
    while mrun:


        task = take_command().lower()#getting the task from the user in voice form 
        print(task)
        
        if 'wikipedia' in task:     #wikipedia searches
            speak('analysing your command..')
            speak('Searching Wikipedia...')
            info = task.replace('wikipedia', '')
            try :
                res = wiki.summary(info, 3)
                speak('According to wikipedia..')
                print(res)
                speak(res)
            except:
                speak('not found in wikipedia , searching on google')
                speak('these are the results found on google')
                pw.search(info)
                
        elif 'send an email to me' in task:
            speak('analysing your command..')
            try:
                speak('What should I send ')
                content = take_command()
                to = '****YOUR MAIL ID****'
                speak('sending email to '+ to)
                send_email(to, content)
                speak('email has been sent succesfully sir..')
            except Exception as e:
                print(e)
                speak('i am not able to send this email')

        elif 'send an email' in task:       #send mail to the sepcified emali in the termianl
            speak('analysing your command..')
            try:
                speak('whom should i send')
                to = input('enter the email :')
                print(to)
                speak('what should i send')
                content = take_command()
                
                erun = True
                while erun:
                    speak('confirmation needed')
                    confo = take_command()
                    if ('send it' in confo) or ('yes' in confo) or ('do it' in confo):
                        send_email(to, content) 
                        speak('email sent succesfully..')
                        print('email sent succesfully..')
                        erun = False
                    elif ('don\'t send' in confo) or ('wait' in confo) or ('no' in confo):
                        speak('as your wish sir, cancelling the email')
                        erun = False
                    else:
                        speak('could not recognize , try again')
                        continue
                    
            except:
                speak('i am not able to send this email, please try again')

        elif 'open browser' in task:
            speak('analysing your command..')
            site = speak('which site do you want to open?')
            run = True
            while run:
                site = take_command()
                print(site)
                speak('just a minute sir')
                if 'sr030' not in site:
                    state = browser(site)
                if ('exit' in state) or 'close' in state:
                    run = False
                else:
                    speak('try again')
                    continue
            
        elif "open youtube" in task:    #opens youtube and play the specified sond, try sepaking open youtube and play the song needed
            speak('analysing your command..')
            speak('openning youtube..\n')
            if 'play' in task:
                speak('just a minute sir..')
                song = task.replace('open','')
                song = task.replace('youtube', '')
                sond = task.replace('and','')
                song = task.replace('play','')
                pw.playonyt(song)
            else:
                wbb.open('youtube.com')

        elif 'open google' in task:     #open google
            speak('analysing your command..')
            speak('hear you go to google')
            wbb.open('google.com')

        elif 'open instagram' in task:      #open instagram
            speak('analysing your command..')
            speak('openning insta')
            wbb.open('instagram.com')

        elif 'exit' in task:        # to exit the loop
            speak('Thanks for giving me your time')
            speak('see you later')
            subprocess.call(['taskkill','/F','/IM','Rainmeter.exe'])
            mrun = False

        elif 'song' in task or ('music' in task) or('on pc' in task) or ('in pc' in task):      #to play a random song from the specified folder
            speak('analysing your command..')
            i = random.randint(1,'***number of songs +1')
            speak('playin a song on pc')
            path = "****folder path containing songs"
            song_list = os.listdir(path)
            os.startfile(os.path.join(path, song_list[i]))
        
        elif 'time' in task:    # to know the time
            time = datetime.datetime.now().strftime('%I %M %p')
            print("the current time is ",time)
            speak("the current time is " + time)

        elif ('do you know tamil' in task):
            speak('enaku tamil theriyathu')

        elif ('open notepad' in task) or ('start notepad' in task):     #open notepad
            speak('opening notepad')
            os.startfile('C:\\Windows\\system32\\notepad.exe')

        elif ('close notepad' in task) or ( 'exit notepad' in task):        #close notepad
            speak('terminating notepad')
            subprocess.call(['taskkill','/F','/IM','notepad.exe']) 

        elif ('open paint' in task) or ('open mspaint' in task) or ('start paint' in task):        #open paint
            speak('opening microsoft paint')
            os.startfile('C:\\Windows\\system32\\mspaint.exe')
        
        elif ('close paint' in task) or ('terminate paint' in task) or ('exit paint' in task):        #closepaint
            speak('terminating microsoft paint') 
            subprocess.call(['taskkill','/F','/IM','mspaint.exe']) 

        elif 'who are you' in task:
            speak('i am draster , i am your personal assestant . i help you playing youtube videos, musics, getting informations , google searches, excetra')
        
        elif ('what ' in task) or('who' in task) or ('how' in task) or ('when' in task) or ('where' in task) or ('why' in task) or ('tell' in task):    # to get informations
            speak('analysing your command..')
            try:
                client = wo.Client(woappid)
                res = client.query(task)
                ans = next(res.results).text
                print(ans)
                speak(ans)
            except:
                speak('these are the results found on google')
                pw.search(task)

        else:
            print('.....')    
