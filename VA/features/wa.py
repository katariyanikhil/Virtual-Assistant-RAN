import wolframalpha

def wolfalpha(question):
    try:
        client = wolframalpha.Client('56P5E5-5XKWHETUQE')
        answer = client.query(question)
        answer = next(answer.results).text
        print(answer)
        return answer
    except:
        speak("Sorry sir I couldn't fetch your question's answer. Please try again ")
        return None
