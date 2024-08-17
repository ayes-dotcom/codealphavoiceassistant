import speech_recognition as sr
import pyttsx3
import webbrowser
import time
import wikipedia

r = sr.Recognizer()
engine = pyttsx3.init()


def listen():
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Please say something:")
        audio = r.listen(source)
        try:
            command = r.recognize_google(audio)
            print("You said: " + command)
            return command
        except sr.UnknownValueError:
            print("Sorry, I couldn't understand what you said")
            return None
        except sr.RequestError as e:
            print("Error requesting results; {0}".format(e))
            return None


def speak(text):
    engine.say(text)
    engine.runAndWait()


def greeting():
    speak("hello i am your voice assistant ,how can i help you today")


def open_google():
    webbrowser.open("https://www.google.com.pk/")
    speak("Google is now open,be patient")


def open_facebook():
    webbrowser.open("https://m.facebook.com/")
    speak("facebook is now open,be patient")


def open_youtube():
    print("Opening YouTube...")
    webbrowser.open("https://www.youtube.com/")
    speak("youtube is now open,be patient")


def open_twitter():
    print("Opening twitter...")
    webbrowser.open_new_tab("https://twitter.com/")
    speak("twitter is now open,be patient")


def open_instagram():
    print("Opening insta...")
    webbrowser.open_new_tab("https://www.instagram.com/")
    speak("insta is now open,be patient")


def timing():
    current_time = time.localtime()
    current_time = time.strftime("%Y-%m-%d %H:%M:%S", current_time)
    print(current_time)
    speak(current_time)


def search_wikipedia(query):
    search_results = wikipedia.search(query)
    if search_results:
        page_title = search_results[0]
        page = wikipedia.page(page_title)
        result = page.summary
        print(result)
        speak(result)

    else:
        print("No results found")


def main():
    while True:
        command = listen()
        if command is not None:
            if command.lower() == "hello":
                greeting()
            elif command.lower() == "open google":
                open_google()
            elif command.lower() == "open facebook":
                open_facebook()
            elif command.lower() == "open youtube":
                open_youtube()
            elif command.lower() == "open insta":
                open_instagram()
            elif command.lower() == "open twitter":
                open_twitter()

            elif "search wikipedia for" in command.lower():
                query = command.lower().replace("search wikipedia for", "")
                search_wikipedia(query)
            elif command.lower() == "can you tell me a timing and date":
                timing()


if __name__ == "__main__":
    main()
