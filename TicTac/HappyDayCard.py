# 1st project Happy Father's Day
"""from asciimatics.effects import Cycle, Stars
from asciimatics.renderers import FigletText
from asciimatics.scene import Scene
from asciimatics.screen import Screen
def demo(screen):
    effects = {
        Cycle(
            screen,
            FigletText("Happy", font='big'),
            int(screen.height / 2 - 9)),
        Cycle(
            screen,
            FigletText("Father's    Day!", font='big'),
            int(screen.height / 4 + 5)),
        Stars(screen, 400)import speech_recognition as sr
    }
    screen.play([Scene(effects, 700)])


Screen.wrapper(demo)
"""

# 2nd project voice-to-text
"""import speech_recognition as sr
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Speak Now: ")
    audio = r.listen(source)
print(r.recognize_google(audio))
"""

# 3rd project text-to-voice
"""import pyttsx3
engine = pyttsx3.init()
engine.say("Hello I'm Jade. Okay. I love pancakes.")
engine.runAndWait()
"""

# 4th project play music using python

