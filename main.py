import pyaudio
import pyttsx3
import speech_recognition as sr
import pywhatkit
import datetime
import wikipedia
import pyjokes
import subprocess
import webbrowser
import pyautogui
import time

listener = sr.Recognizer()
engine = pyttsx3.init()


def talk(text):
    engine.say(text)
    engine.runAndWait()


talk("Hi I am Jack how can I help you")


def take_command():
    try:
        with sr.Microphone() as source:
            print("Listening....")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
    except:
        print("there was an error please try again")
    return command
def take_and_type(text):
    time.sleep(2)
    pyautogui.typewrite(text)


def run():
    try:
        command = take_command()
        print(command)
        if "jack" in command:
            command = command.replace("bro", "")
            if "play" and "on youtube" in command:
                player1 = command.replace("play", "")
                player = player1.replace("on youtube", "")
                talk("playing" + player)
                print("playing" + player)
                pywhatkit.playonyt(player)
            elif "time" in command:
                time = datetime.datetime.now().strftime("%I: %M %p")
                talk("the time is: " + time)
                print(time)
            elif "tell me about" in command:
                wiki_query = command.replace("tell me about", "")
                info = wikipedia.summary(wiki_query, 3)
                print(info)
                talk(info)
            elif "joke" in command:
                joke = pyjokes.get_joke()
                print(joke)
                talk(joke)
            elif "open chrome" in command:
                talk("opening chrome")
                subprocess.call('C://Program Files//Google//Chrome//Application//chrome.exe')

            elif "what is" and "+" in command:
                try:
                    command = command.replace("what is", "")
                    command = command.replace("+", "")
                    num_list = command.split()
                    num1 = int(num_list[0])
                    num2 = int(num_list[1])
                    sum = num1 + num2
                    print(f"{num1} + {num2} is {sum}")
                    talk(f"{num1} + {num2} is {sum}")
                except ValueError:
                    talk("please speak valid numbers")
                    print("Please speak valid numbers")
            elif "what is" and "-" in command:
                try:
                    command = command.replace("what is", "")
                    command = command.replace("-", "")
                    num_list = command.split()
                    num1 = int(num_list[0])
                    num2 = int(num_list[1])
                    difference = num1 - num2
                    talk(f"{num1} minus {num2} is {difference}")
                    print(f"{num1} minus {num2} is {difference}")
                except ValueError:
                    talk("please speak valid numbers")
                    print("Please speak valid numbers")
            elif "what is" and "x" in command:
                try:
                    command = command.replace("what is", "")
                    command = command.replace("x", "")
                    num_list = command.split()
                    num1 = int(num_list[0])
                    num2 = int(num_list[1])
                    product = num1 * num2
                    talk(f"{num1} multiplied by {num2} is {product}")
                    print(f"{num1} multiplied by {num2} is {product}")
                except ValueError:
                    talk("please speak valid numbers")
                    print("Please speak valid numbers")
            elif "what is" and "x" in command:
                try:
                    command = command.replace("what is", "")
                    command = command.replace("x", "")
                    num_list = command.split()
                    num1 = int(num_list[0])
                    num2 = int(num_list[1])
                    product = num1 * num2
                    talk(f"{num1} multiplied by {num2} is {product}")
                    print(f"{num1} multiplied by {num2} is {product}")
                except ValueError:
                    talk("please speak valid numbers")
                    print("Please speak valid numbers")
            elif "what is" and "/" in command:
                try:
                    command = command.replace("what is", "")
                    command = command.replace("/", "")
                    num_list = command.split()
                    num1 = int(num_list[0])
                    num2 = int(num_list[1])
                    quotient = num1 / num2
                    talk(f"{num1} divided by {num2} is {quotient}")
                    print(f"{num1} divided by {num2} is {quotient}")
                except ValueError:
                    talk("please speak valid numbers")
                    print("Please speak valid numbers")
            elif "open unity" in command:
                talk("opening unity")
                subprocess.call("C://Program Files//Unity//Hub//Editor//2020.3.8f1//Editor//Unity.exe")
            elif "open vs code" in command:
                talk("opening VS code")
                print("opening vs code")
                subprocess.call("C://Users//yasht//AppData//Local//Programs//Microsoft VS Code//Code.exe")

            elif "open zoom" in command:
                talk("opening zoom")
                print("opening zoom")
                subprocess.call("C://Users//yasht//AppData//Roaming//Zoom//bin//Zoom.exe")

            elif "open visual studio" in command:
                talk("opening Visual Studio")
                print("opening visual studio")
                subprocess.call("C://Program Files (x86)//Microsoft Visual Studio//2019//Community//Common7//IDE//devenv.exe")
            elif "open classroom" in command:
                webbrowser.open_new("https://classroom.google.com/u/1/h")
                talk("opening google classroom")
            elif "search" and "chrome" in command:
                import time
                command = command.replace("search", "")
                command = command.replace("in chrome", "")
                talk(f"searching {command} in chrome")
                print(f"searching {command} in chrome")
                subprocess.call('C://Program Files//Google//Chrome//Application//chrome.exe')
                take_and_type(command)

                pyautogui.press('enter')
            elif "who is your mortal enemy" in command:
                talk("Alexa is my mortal enemy, we will never speak about her in front of me again!!")
                print("Alexa is my mortal enemy, we will never speak about her in front of me again!!")
            elif "open notepad" in command:
                subprocess.call('notepad.exe')
                talk("opening notepad")
            elif "who is trash" in command:
                print("Cortana, no questions asked")
                talk("Cortana, no questions asked")
            elif "open history quiz" in command:
                talk("opening your history quiz")
                webbrowser.open_new("https://quizizz.com/join/activity/created")
            elif "open chess.com" in command:
                talk("opening your second favourite chess website")
                webbrowser.open_new_tab("https://www.chess.com/home")
            elif 'open civics project website' in command:
                talk('opening the types of governments wikipedia page')
                webbrowser.open_new('https://en.wikipedia.org/wiki/List_of_forms_of_government')
            else:
                "Please say the command again"
        else:
            talk("I will only speak when you ask for me to speak")
            print("I will only speak when you ask for me to speak")
    except:
        print("sorry I couldn't understand you")
while True:
    run()
