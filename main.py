from VA import VirtualAssistant
import datetime
import re
import sys
import os
import pyjokes
import requests

obj = VirtualAssistant()

def speak(text):
    obj.voiceOutput(text)


def startup():
	print("My name is RAN.")
	speak("My name is RAN.")

	hour = int(datetime.datetime.now().hour)
	if hour>=0 and hour<=12:
		print("Good morning sir")
		speak("Good morning sir")
	elif hour>12 and hour<18:
		print("Good afternoon sir")
		speak("Good afternoon sir")
	else:
		print("Good evening sir")
		speak("Good evening sir")

	print("Please tell me how may I help you?")    
	speak("Please tell me how may I help you?")


class Main():
    def __init__(self):
        super().__init__()

    def run(self):
        startup()

        while True:
            command = obj.voiceInput()

            if re.search('date', command):
                date = obj.tellDate()
                print(date)
                speak(f"Sir the date is {date}")

            elif re.search('time', command):
                time = obj.tellTime()
                print(time)
                speak(f"Sir the time is {time}")

            elif "joke" in command:
                joke = pyjokes.get_joke()
                print(joke)
                speak(joke)

            elif "system" in command:
                sysInfo = obj.systemInfo()
                print(sysInfo)
                speak(sysInfo)
            
            elif re.search('created', command):
                speak(f"I was created by Rohit, Nikhil and Akshat in their 5660 Final Project.")
                startup()
                
            elif "calculate" in command or "what is" in command or "who is" in command:
                ans = obj.wolframalpha(command)
                speak(ans)
            
            elif "make a note" in command or "write this down" in command or "remember this" in command:
                speak("What would you like me to write down?")
                text = obj.voiceInput()
                obj.take_note(text)
                print("I've made a note of that")
                speak("I've made a note of that")

            elif "close the note" in command or "close notepad" in command:
                speak("Okay sir, closing notepad")
                os.system("taskkill /f /im gedit")
                
            elif "where i am" in command or "current location" in command or "where am i" in command:
                try:
                    city, state, country = obj.my_location()
                    print(city, state, country)
                    speak(
                        f"You are currently in {city} city which is in {state} state and country {country}")
                except Exception as e:
                    speak(
                        "Sorry sir, I coundn't fetch your current location. Please try again")

            elif re.search('open', command) or re.search('launch', command):
                app = command.split(' ', 1)[1]
                speak('Opening: ' + app + 'for you sir!')
                try:
                    obj.launchApp(app)
                except:
                    result = obj.websiteOpener(app)
                    speak(f'Alright Opening {app}')
                    print(result)

            elif "news" in command or "headlines" in command:
                news_res = obj.news()
                speak('Source: The Times Of India')
                speak('Todays Headlines are..')
                for index, articles in enumerate(news_res):
                    print(articles['title'])
                    speak(articles['title'])
                    if index == len(news_res)-2:
                        break
                speak('These were the top headlines, Have a nice day Sir!!..')
            
            elif re.search('weather', command):
            	city = command.split(' ')[-1]
            	res = obj.weather(city)
            	print(res)
            	speak(res)
            
            elif re.search('wikipedia', command):
            	topic = command.split(' ')[-1]
            	if topic:
            		res = obj.search_wikipedia(topic)
            		print(res)
            		speak(res)
            	else:
            		speak("Sorry sir. I couldn't search for it") 
            
            elif "ip address" in command:
                ip = requests.get('https://api.ipify.org').text
                print(ip)
                speak(f"Your ip address is {ip}")
            
            elif "goodbye" in command or "offline" in command or "bye" in command or "see you" in command:
                speak("Alright sir, going offline.")
                sys.exit()
            
ran = Main()
ran.run()
