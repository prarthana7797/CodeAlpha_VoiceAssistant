import speech_recognition as aa
import pyttsx3
import pywhatkit
import datetime
import wikipedia

listener = aa.Recognizer()

machine = pyttsx3.init()

def talk(text):
    machine.say(text)
    machine.runAndWait()

def input_instruction():
    instruction = None  # Initialize instruction variable
    try:
        with aa.Microphone() as origin:
            print("listening")
            speech = listener.listen(origin)
            instruction = listener.recognize_google(speech)  # for Google API
            instruction = instruction.lower()
            if "jarvis" in instruction:
                instruction = instruction.replace('jarvis', '')  # Remove "jarvis" from instruction
            print(instruction)
    except:
        pass
    return instruction

def play_Jarvis():
    instruction = input_instruction()
    print(instruction)

    if instruction:
        if "play" in instruction:
            song = instruction.replace('play ', '')  # Remove "play " from instruction to get song name
            talk("playing " + song)
            pywhatkit.playonyt(song)

        elif 'time' in instruction:
            time_now = datetime.datetime.now().strftime('%I:%M %p')
            talk('Current time is ' + time_now)

        elif 'date' in instruction:
            date_today = datetime.datetime.now().strftime('%d /%m /%Y')
            talk("Today's date is " + date_today)

        elif 'how are you' in instruction:
            talk('I am fine, how about you?')

        elif 'what is your name' in instruction:
            talk('I am Jarvis. What can I do for you?')

        elif 'who is' in instruction:
            person = instruction.replace('who is ', '')  # Remove "who is " from instruction to get person's name
            info = wikipedia.summary(person, 1)
            print(info)
            talk(info)

        else:
            talk('Please repeat')
    else:
        talk('Please repeat')  # Handle case when no valid instruction is received

play_Jarvis()
