import speech_recognition as sr
import pyttsx3

from VA.features import dateTime,openApp,systemStats,websiteOpen,wiki,weather,news,note,wa

t2s = pyttsx3.init()
voices = t2s.getProperty('voices')
t2s.setProperty('voices', voices[0].id)

class VirtualAssistant:
    def __init__(self):
        pass

    def voiceInput(self):
        # take voice input from user and return it as a text
        try:
            r = sr.Recognizer()

            with sr.Microphone() as source:
                print("Listening..")
                r.energy_threshold = 4000
                audio = r.listen(source)
            try:
                command = r.recognize_google(audio, language='en-in').lower()
                print(f'You said: {command}')
            except:
                print('Sorry could not recognize what you said. Please try again')
                command = self.voiceInput()
            return command

        except Exception as e:
            print(e)
            return  False

    def voiceOutput(self, text):
        # convert text to speech and play the result
        try:
            t2s.say(text)
            t2s.runAndWait()
            t2s.setProperty('rate', 175)
            return True
        except:
            t = "Sorry I couldn't understand and handle this input"
            print(t)
            return False

    def tellTime(self):
        return dateTime.time()
    
    def tellDate(self):
        return dateTime.date()
    
    def launchApp(self, app):
        #Launch any application 
        return openApp.launch(app)
    
    def systemInfo(self):
        return systemStats.stats()

    def websiteOpener(self, domain):
        #open website according to domain
        return websiteOpen.open(domain)
    
    def search_wikipedia(self, topic):
    	return wiki.search_wiki(topic)
    	
    def news(self):
        return news.get_news()
    
    def wolframalpha(self,text):
        return wa.wolfalpha(text)
        
    def take_note(self,text):
        return note.note(text)
        
    def location(self):
    	city,state,country = loc.mylocation()
    	return city,state,country
    
    def weather(self, city):
    	try:
    		res = weather.fetch_weather(city)
    	except Exception as e:
    		print(e)
    		res = false
    	return res

