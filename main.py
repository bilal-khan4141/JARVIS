import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests

recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi  = "850c4f2743c94a21b6ef7a2e43d0dd2e"


def speak(text):
    engine.say(text)
    engine.runAndWait()


def  processCommand(c):
    if "open google" in  c.lower():
        webbrowser.open("https://google.com")
    elif "open instagram" in  c.lower():
        webbrowser.open("https://instagram.com")
    elif "open youtube" in  c.lower():
        webbrowser.open("https://youtube.com")
    elif "open facebook" in  c.lower():
        webbrowser.open("https://facebook.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)

    elif "news" in c.lower():
        try:
            r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")

            if r.status_code == 200:
                # Parse the JSON response
                data = r.json()

                # Extract the articles (✅ Corrected key: 'articles')
                articles = data.get('articles', [])

                if not articles:  # ✅ Handling empty list case
                    speak("Sorry, I couldn't find any news.")
                else:
                    speak("Here are the latest news headlines.")
                    for article in articles[:5]:  # ✅ Get only the top 5 headlines
                        speak(article['title'])  # ✅ Corrected key: 'title'
            else:
                speak("Sorry, I couldn't fetch the news.")

        except Exception as e:
            speak(f"An error occurred while fetching the news: {e}")


    else:
        # let openAI handle the request
        pass

    


if __name__ == "__main__":
    speak("jarvis on duty sir...")
    while True:

    # listen to the jarvis
    # obtain audio from the microphone
        r = sr.Recognizer()
        

        print("recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening!")
                audio = r.listen(source, timeout=3, phrase_time_limit=2)
            word = r.recognize_google(audio)
            if(word.lower() == "jarvis"):
                speak("yes")
            # listen for command
            with sr.Microphone() as source:
                print("jarvis Active..")
                audio = r.listen(source)
                command = r.recognize_google(audio)

                processCommand(command)

        except Exception as e:
            print("Error; {0}".format(e))
