import wikipedia
import re

def search_wiki(topic):
    try:
        res = wikipedia.summary(topic, sentences=1)

        return res
    except Exception as e:
        print(e)
        return False
