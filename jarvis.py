import pyttsx3
import speech_recognition as sr
import webbrowser
import pywhatkit
import wikipedia
from bs4 import BeautifulSoup
import wikipedia as googlescrap
from googletrans import Translator
from pywikihow import search_wikihow
import os
import pyautogui
import requests
from tkinter import Label
from tkinter import Entry
from tkinter import Button
from tkinter import Tk
from gtts import gTTS
from tkinter import StringVar
import PyPDF2
from pytube import YouTube
from playsound import playsound
import keyboard
import pyjokes
from PyDictionary import PyDictionary as Diction
import datetime
import time
import sys
import pyttsx3.drivers





Assistant = pyttsx3.init('sapi5')
voices = Assistant.getProperty('voices')
print (voices)
Assistant.setProperty('voices',voices[1].id)
Assistant.setProperty('rate',150)

def Speak(audio):
    print("    ")
    Assistant.say(audio)
    print(f": {audio}")
    print("    ")
    Assistant.runAndWait()

def takecommand():
    command = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        command.pause_threshold = 1
        audio = command.listen(source)

    try:
        print("Recognizing...")
        query = command.recognize_google(audio, language='en-in')
        print(f"you said : {query}")

    except :
        return "none"

    return query.lower()



    


def taskExe():

    Speak("yes sir")


    def Music():
        Speak("sure sir")
        
        if 'gasolina' in query:
            os.startfile('D:\\Music\\Gasolina (Daddy Yankee) Remix_320(PagalWorld).mp3')
            Speak("here we go for gasolina")

        else:    
            pywhatkit.playonyt(query)
            Speak("playing on youtube"+query)

    def Whatsapp():
        Speak("Tell me the name of that person sir")
        name = takecommand()
         
        if 'bro' in name or 'noni' in name or 'anubhav' in name:
            Speak("tell me what to type! sir.")
            msg = takecommand()
            Speak("at what time in hour! sir")
            hour = int(takecommand())
            Speak("at what minitue!") 
            min =int(takecommand())
            pywhatkit.sendwhatmsg("+91",msg,hour,min,20)
            Speak("ok sir, sending message! ")

        elif 'vinni' in name or 'vini' in name:
            Speak("tell me what to type! sir.")
            msg = takecommand()
            Speak("at what time in hour! sir")
            hour = int(takecommand())
            Speak("at what minitue!") 
            min =int(takecommand())
            pywhatkit.sendwhatmsg("+918171794940",msg,hour,min,20)
            Speak("ok sir, sending message! ")  


        else:
            Speak("tell me the number of that person.")
            phone = int(takecommand())
            ph = '+91' + phone
            Speak("tell me what to type, sir!")
            msg = takecommand()
            Speak("at what time in hour! sir")
            hour = int(takecommand())
            Speak("at what minitue!") 
            min =int(takecommand())
            pywhatkit.sendwhatmsg(ph,msg,hour,min,20)
            Speak("ok sir, sending message! ")      

    def OpenApps():
        Speak("sure sir, wait for a while!")

        if 'chrome' in query:
            os.startfile("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe")
            Speak("opening")

        elif 'facebook' in query:
            webbrowser.open('https://www.facebook.com/')
            Speak("opening")

        elif 'maps'in query:
            webbrowser.open('https://www.google.com/maps') 
            Speak("opening")   

        elif 'youtube'in query:
            webbrowser.open('https://www.youtube.com') 
            Speak("opening")     

        elif 'whatsapp' in query:
            os.startfile("5319275A.WhatsAppDesktop_cv1g1gvanyjgm!WhatsAppDesktop.exe")    

    def Dict(): 
        Speak("Activated Dictionary")
        Speak("tell me the probleb")
        probl = takecommand()

        if 'meaning' in probl:
            probl = probl.replace("what is the", "")
            probl = probl.replace("jarvis", "")
            probl = probl.replace("of", "")
            probl = probl.replace("meaning of", "")
            result = Diction.meaning(probl)
            Speak(f"the meaning of {probl} is {result}")

        elif 'synonym' in probl:
            probl = probl.replace("what is the", "")
            probl = probl.replace("jarvis", "")
            probl = probl.replace("of", "")
            probl = probl.replace("synonym of", "")
            result = Diction.synonym(probl)
            Speak(f"the synonym of {probl} is {result}")

        elif 'antonym' in probl:
            probl = probl.replace("what is the", "")
            probl = probl.replace("jarvis", "")
            probl = probl.replace("of", "")
            probl = probl.replace("antonym", "")
            result = Diction.antonym(probl)
            Speak(f"the antonym of {probl} is {result}")

    def CloseApps():
        Speak("ok sir")

        if 'youtube' in query:
            os.system("TASKKILL/F / im chrome.exe")
            Speak("closing")

        elif 'chrome' in query:
            os.system("TASKKILL/F / im chrome.exe")   

        Speak("closing")    

    def YoutubeAuto():
        Speak("what to do")
        comm = takecommand()

        if 'pause' in comm:
            keyboard.press('space bar')

        elif 'restart' in comm:
            keyboard.press('0')    

        elif 'mute' in comm:
            keyboard.press('m')  

        elif 'skip' in comm:
            keyboard.press('l')    

        elif 'back' in comm:
            keyboard.press('j')

        elif 'full screen' in comm:
            keyboard.press('f')   

        elif 'film mode' in comm or 'cenima mode' in comm:
            keyboard.press('t') 

        Speak("ok sir")

    def ChromeAuto():
        Speak("chrome Automation activated!")

        command = takecommand()

        if 'close this tab' in command:
            keyboard.press_and_release('ctrl + w')

        elif 'open new window' in command:
            keyboard.press_and_release('cntrl + t') 

        elif 'open new window' in command:
            keyboard.press_and_release('cntrl + n')       

            Speak("command completed")

    def TakeHindi():
        command = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening......")
            command.pause_threshold = 1
            audio = command.listen(source)

            try:
                print("Recognizing.....")
                query = command.recognize_google(audio,language='hi')
                print(f"You Said : {query}")

            except:
                return "none"

            return query.lower()

    def Tran():
        Speak("Tell Me The Line!")
        line = TakeHindi()
        traslate = Translator()
        result = traslate.translate(line)
        Text = result
        Speak(Text)
        
    def Delete():
        Speak("are you sure sir, to delete this")

        command = takecommand()

        if 'yes' in command:
            keyboard.press('delete')
            Speak("Deleted succesfully")

        elif 'no' in command:
            Speak("ok sir, not deleting the file")    

        else:
            Speak("process undone")

    def Splitwin():
        Speak("split it to right or to left sir")

        command = takecommand()

        if 'right' in command:
            keyboard.press_and_release('Win+Right arrow')
            Speak("window splited" +command)

        elif 'left' in command:
            keyboard.press_and_release('Win+left arrow')
            Speak("window splited" +command)

        else:
            Speak("I cancelled the process, sir")
            Speak("if you want to do it, just give me an order sir")    

    def shiftdekstop():
        Speak("shift it to right or to left sir")

        command = takecommand()

        if 'right' in command:
            keyboard.press_and_release('Win+ctrl+Right arrow')
            Speak("Dekstop shifted" +command)

        elif 'left' in command:
            keyboard.press_and_release('Win+ctrl+left arrow')
            Speak("Dekstop shifted" +command)

        else:
            Speak("I cancelled the process, sir")
            Speak("if you want to do it, just give me an order sir")

    def PCdown():
        Speak("please confirm sir, you want shutdown or log out")
        Speak("make sure no application remains open, otherwise you may loose data")

        command = takecommand()

        if 'shutdown' in command:
            Speak("PC is going to shutdown")
            os.system("shutdown /s /t 1")

        elif 'log out' in command or 'log off' in command or 'log of' in command:
            Speak("logging off")
            os.system("shutdown -l")
        
        elif 'no' in command or 'noh' in command or 'dont' in command or 'dont do' in command or 'stop' in command:
            Speak("ok, you can continue")
            
    def Temp():
            search = f"temperature in {query}"
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text,"html.parser")
            temperature = data.find("div",class_ = "BNeawe").text
            Speak(f"The Temperature in {query} is {temperature}")

    def Reader(): #not proper
        Speak("Tell Me The Name Of The Book!")

        name = takecommand()

        if 'india' in name:

            os.startfile('E:\\Kaushik Shresth\\Books\\Social Science\\History\\ch 1.pdf')
            book = open('E:\\Kaushik Shresth\\Books\\Social Science\\History\\ch 1.pdf','rb')
            pdfreader = PyPDF2.PdfFileReader(book)
            pages = pdfreader.getNumPages()
            Speak(f"Number Of Pages In This Books Are {pages}")
            Speak("From Which Page I Have To Start Reading ?")
            numPage = int(input("Enter The Page Number :"))
            page = pdfreader.getPage(numPage)
            text = page.extractText()
            Speak("In Which Language , I Have To Read ?")
            lang = takecommand()

            if 'hindi' in lang:
                transl = Translator()
                textHin = transl.translate(text,'hi')
                textm = textHin.text
                speech = gTTS(text = textm )

                try:
                    speech.save('book.mp3')
                    playsound('book.mp3')

                except:
                    playsound('book.mp3')

            else:
                Speak(text)

        elif 'europe' in name:
            os.startfile('E:\\Kaushik Shresth\\Books\\Social Science\\History\\ch 3.pdf')
            book = open('E:\\Kaushik Shresth\\Books\\Social Science\\History\\ch 3.pdf','rb')
            pdfreader = PyPDF2.PdfFileReader(book)
            pages = pdfreader.getNumPages()
            Speak(f"Number Of Pages In This Books Are {pages}")
            Speak("From Which Page I Have To Start Reading ?")
            numPage = int(input())
            page = pdfreader.getPage(numPage)
            text = page.extractText()
            Speak("In Which Language , I Have To Read ?")
            lang = takecommand()

            if 'hindi' in lang:
                transl = Translator()
                textHin = transl.translate(text,'hi')
                textm = textHin.text
                speech = gTTS(text = textm )
                try:

                    speech.save('book.mp3')
                    playsound('book.mp3')

                except:
                    playsound('book.mp3')

            else:
                Speak(text)
        
    def SpeedTest():
        import speedtest
        Speak("Initializing your internet sir. ")
        speed = speedtest.Speedtest()
        downloading = speed.download()
        correctDown = int(downloading/800000)
        uploading = speed.upload()
        correctUpload = int(uploading/800000)

        if 'uploading' in query:
            Speak(f"Your Uploading Speed Is {correctUpload} mbp s")

        elif 'downloading' in query:
            Speak(f"Your Downloading Speed Is {correctDown} mbp s")  

        else:
            Speak(f"your Downloading speed is {correctDown} mbp s")
            Speak(f"And your Uploading speed is {correctUpload} mbp s")      

    def Wishme():
        hour = int(datetime.datetime.now().hour)
        if hour >= 0 and hour < 12:
            Speak("Good Morning Sir !")
            Speak("jarvis 2 point O is in your service")

        elif hour >= 12 and hour < 18:
            Speak("Good Afternoon Sir !")
            Speak("jarvis 2 point O is in your service")

        else:
            Speak("Good Evening Sir !")
            Speak("jarvis 2 point O is in your service")
            
   
    


        


    while True:
        
        query = takecommand()

        if 'hello' in query:
            Wishme()
            break

        elif 'read for me' in query:    #NOT PROPER
            Reader()
            break

        elif 'Kya hal hai' in query:
            query = query.replace("Jarvis"," ")
            Speak("Mai bhadiya hoon aap btao") 
            break

        elif 'open youtube' in query:
            OpenApps()
            break

        elif 'youtube'  in query:
            query = query.replace("jarvis","")
            query = query.replace("on youtube","")
            query = query.replace("youtube","")
            query = query.replace("search","")
            Speak("here we go for" +query)
            web = 'https://www.youtube.com/results?search_query=' + query
            webbrowser.open(web)
            break

        elif 'open google' in query:
            webbrowser.open_new_tab("https://www.google.com")
            Speak("Google is opening")
            break

        elif 'google' in query:
            query = query.replace("jarvis", "")
            query = query.replace("search ","")
            query = query.replace("on google","")
            query = query.replace("google", "")
            Speak("searching on google" +query)
            
            try:
                pywhatkit.search(query)
                result = googlescrap.summary(query,3)
                Speak(result)    

            except:  
               pywhatkit.search(query) 
               Speak("there is no open data available sir! but you can visit the site data here") 

               break            

        elif 'website' in query or 'site' in query:
            query = query.replace("jarvis", "")
            query = query.replace("search", "")
            query = query.replace("website", "")
            query = query.replace("site", "")
            query = query.replace(" ","")
            web1 = query.replace("open", "")
            web2 = 'https://www.' + web1 + '.com'
            webbrowser.open(web2)
            Speak("opening "+web1)
            break

        elif 'launch' in query:
            query = query.replace("Jarvis"," ")
            query = query.replace("launch"," ")
            web = 'http://www.' + query + '.com'
            webbrowser.open(web)
            Speak("launching"+query)
            break

        elif 'music' in query or 'song' in query:
            query = query.replace("jarvis","")
            query = query.replace("play","")
            query = query.replace("the song","")
            query = query.replace("song","")
            query = query.replace("the music","")
            query = query.replace("music","")
            Music()
            break
        
        elif 'wikipedia' in query:
            query = query.replace("jarvis","")
            query = query.replace("wikipedia","")
            wiki = wikipedia.summary(query,2)
            Speak(f"According To Wikipedia : {wiki}")
            break

        elif 'open whatsapp' in query:
            OpenApps()
            break

        elif 'whatsapp' in query:
            Whatsapp()
            break
           
        elif 'screenshot' in query: 
            query = query.replace("Jarvis","")
            query = query.replace("take a","")
            query = query.replace("take","")
            Speak("taking screenshot")
            keyboard.press_and_release('Win+prtscn')
            break

        elif 'open chrome' in query:
            OpenApps()
            break

        elif 'open facebook' in query:
            OpenApps()
            break

        elif 'open maps' in query:
            OpenApps()
            break

        elif 'close chrome' in query:
            CloseApps()
            break

        elif 'close youtube' in query:
            CloseApps()
            break

        elif 'pause' in query:
            query = query.replace("Jarvis"," ")
            keyboard.press('space bar')
            break

        elif 'restart' in query:
            query = query.replace("Jarvis"," ")
            keyboard.press('0')
            break    

        elif 'mute' in query:
            query = query.replace("Jarvis"," ")
            keyboard.press('m')  
            break

        elif 'skip' in query:
            query = query.replace("Jarvis"," ")
            keyboard.press('l')   
            break 

        elif 'back' in query:
            query = query.replace("Jarvis"," ")
            keyboard.press('j')
            break

        elif 'full screen' in query:
            query = query.replace("Jarvis","")
            keyboard.press('f')
            Speak("screen is now full") 
            break

        elif 'minimize the screen' in query or 'minimise the screen'in query:
            query = query.replace("Jarvis","")
            keyboard.press('f')
            Speak("screen is minimized")  
            break   

        elif 'film mod' in query or 'cenima mod' in query:
            query = query.replace("Jarvis"," ")
            keyboard.press('t')     
            Speak("shifting screen")  
            break  

        elif 'youtube tools' in query:
            YoutubeAuto()
            break

        elif 'close this tab' in query:
            query = query.replace("Jarvis"," ")
            Speak("closing")
            keyboard.press_and_release('ctrl + w')
            break

        elif 'new tab' in query:
            query = query.replace("Jarvis"," ")
            Speak("opening")
            keyboard.press_and_release('ctrl + t') 
            break

        elif 'new window' in query:
            query = query.replace("Jarvis"," ")
            Speak("opening")
            keyboard.press_and_release('ctrl + n')
            break

        elif 'chrome automation' in query:
            query = query.replace("Jarvis"," ")
            ChromeAuto()
            break

        elif 'joke' in query or 'jokes' in query:
            query = query.replace("Jarvis"," ")
            get = pyjokes.get_jokes()
            Speak(get)
            break
 
        elif 'repeat my words' in query or 'repeat after me' in query or 'repeat me' in query:
            query = query.replace("Jarvis"," ")
            Speak("Speak sir!")
            jj = takecommand()
            Speak(f" {jj}")
            break

        elif 'my location' in query:
            query = query.replace("Jarvis","")
            query = query.replace("what is","")
            Speak("here is your location sir")
            webbrowser.open('https://www.google.com/maps/place/Numaish+Camp,+Saharanpur,+Uttar+Pradesh+247001/@29.9738068,77.5592913,15z/data=!3m1!4b1!4m5!3m4!1s0x390ec0285f7b2af9:0xb5afb1735b15d17d!8m2!3d29.9753092!4d77.571972')
            break

        elif 'dictionary' in query:
            Dict()
            break

        elif 'select all' in query:
            keyboard.press_and_release('Ctrl + A')
            Speak("Selected")

        elif 'copy all' in query:
            keyboard.press_and_release('ctrl+c')  
            Speak("copied")  

        elif 'paste' in query or "paste all" in query or "print" in query:
            keyboard.press_and_release('ctrl+v')  
            Speak("paisted")     

        elif 'delete' in query:
            Delete()
            break

        elif 'save' in query:
            query = query.replace("Jarvis","")
            query = query.replace("the file","")
            query = query.replace("it","")
            query = query.replace("that file","")
            keyboard.press_and_release('ctrl+s') 
            Speak("saved succesfully")   
            break

        elif 'minimise all' in query or 'minimise all windows' in query:
            keyboard.press_and_release('Win+m')
            Speak("all windows minimized")
            break

        elif 'minimise window' in query:
            keyboard.press_and_release('Win+Down arrow')
            Speak("current window minimized")
            break

        elif 'maximise window' in query or 'maximize window' in query: 
            keyboard.press_and_release('Win+Up arrow')
            Speak("Window maximized")
            break

        elif 'split window' in query or 'split the window' in query:
            query = query.replace("Jarvis","")
            Splitwin()
            break

        elif 'second dekstop' in query or 'second destop' in query or'virtual dekstop' in query or 'virtual destop' in query or 'second desktop' in query or'virtual desktop' in query or 'virtual destop' in query:
            keyboard.press('Win+ctrl+d')     
            Speak("here is your virtual Dekstop sir.")
            break

        elif 'shift destop' in query or 'shift dekstop' in query:
            shiftdekstop()
            break

        elif 'shutdown pc' in query or "log out" in query or "log off"in query:
            PCdown()
            break
            
        elif 'open spotify' in query:
            webbrowser.open_new_tab("https://open.spotify.com/?_ga=2.221590619.29341355.1621750891-1847216084.1618288245")
            Speak("opening spotify")
            break

        elif 'on spotify'  in query:
            query = query.replace("jarvis","")
            query = query.replace("on spotify","")
            query = query.replace("spotify","")
            query = query.replace("search","")
            query = query.replace("play","")
            Speak("here we go for " +query)
            web = 'https://open.spotify.com//results?search_query=' + query
            webbrowser.open(web)
            break

        elif 'news' in query:
            webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
            Speak("Here are some headlines from the Times of India. Happy reading sir") 
            break   
            
        elif 'download the video' in query:
            root = Tk()
            root.geometry('600x300')
            root.resizable(0,0)
            root.title("Youtube Video Downloader")
            Speak("Enter Video Url Here !")
            Label(root,text = "Youtube Video Downloader",font = 'arial 20 bold').pack()
            link = StringVar()
            Label(root,text = "Paste Video URL Here",font = 'arial 15').place(x=180,y=80)
            Entry(root,width = 90,textvariable = link).place(x=42,y=120)

            def VideoDownloader():
                url = YouTube(str(link.get()))
                video = url.streams.first()
                video.download()
                Label(root,text = "Downloaded",font = 'arial 15').place(x= 200,y=210)

            Button(root,text = "Download",font = 'arial 15 bold',bg = 'pale violet red',padx = 2 , command = VideoDownloader).place(x=200,y=200)

            root.mainloop()
            Speak("Video Downloaded")
            break

        elif 'translator' in query:
            Tran()
            break

        elif 'remember that' in query:
            query = query.replace("remember that","")
            query = query.replace("jarvis","")
            query = query.replace("i","")
            Speak("You Tell Me to Remind You that you : " +query)
            remember = open('data.txt','w')
            remember.write(query)
            remember.close()
            break

        elif 'do you remember anything' in query or ('what do you remember') in query: 
            remember = open('data.txt', 'r')
            Speak("You tell me that you" +remember.read())   
            break

        elif 'temperature' in query:
            query = query.replace("what is" ,"")
            query = query.replace("what's" ,"")
            query = query.replace("what" ,"")
            query = query.replace("temperature in" ,"")
            query = query.replace("temperature" ,"")
            Temp()
            break

        





     
        elif 'search' in query or 'Search' in query:
            query = query.replace("jarvis", "")
            query = query.replace("search ","")
            query = query.replace("on google","")
            query = query.replace("google", "")
            Speak("searching for " +query)
            
            try:
                pywhatkit.search(query)
                result = googlescrap.summary(query,3)
                Speak(result)    

            except:  
               pywhatkit.search(query) 
               Speak("there is no open data available sir! but you can visit the site data here") 

               break 

        elif 'time' in query:
            time = datetime.datetime.now().strftime('%I:%M %p')
            Speak('Current time is ' + time)
            break

        elif 'how are you' in query:
            query = query.replace("Jarvis"," ")
            Speak("Iam fine sir!")
            Speak("how about you?")
            break

        elif 'who are you' in query:
            query = query.replace("Jarvis"," ")
            Speak("hello sir, i am Jarvis .")
            Speak("your personal AI assistant")
            Speak("You can give me a command ! n I will do that for you")
            break
          
        elif 'who made you' in query:
            query = query.replace("Jarvis"," ")
            Speak("Thanks to Mr. Arpit Sir")
            Speak("rather it is personal") 
            break

        elif 'how to' in query:
            Speak("Getting Data From The Internet !")
            op = query.replace("jarvis","")
            max_result = 1
            how_to_func = search_wikihow(op,max_result)
            assert len(how_to_func) == 1
            how_to_func[0].print()
            Speak(how_to_func[0].summary)
            break

        elif 'speed' in query or "check my internet" in query:
            SpeedTest()
            break

        elif 'what' in query or 'who' in query or 'how' in query or 'is' in query or 'can' in query or 'will' in query:
            query = query.replace("jarvis", "")

            try:
               result = googlescrap.summary(query,3)
               Speak(result)    

            except:  
               pywhatkit.search(query)
               Speak("there is no open data available sir! but you can visit the site data here")  
               break

        elif 'you need a break' in query or 'you need some rest' in query:
            query = query.replace("Jarvis"," ")
            Speak("OK Sir, you can call me any time !")
            break
        
        elif 'ok alex' in query or 'okay alex' in query:
            query = query.replace("Jarvis"," ")
            Speak("ok sir, Call me any time")
            break

        else:
            Speak("sorry sir, I'm unable to recognize your word, can u please speak again")


if __name__ == "__main__":
    while True:
        permission = takecommand()
        

        if 'jarvis' in permission:
            taskExe()

        if 'jarves' in permission:
            taskExe()    

        if 'Jarvis' in permission:
            taskExe()    

        elif 'sleep' in permission:
            sys.exit() 

        elif 'exit' in permission:
            sys.exit()        

        else:
            print ("if you are trying to wake me up please use other words")
            print("and if not ignore the msg")

          
