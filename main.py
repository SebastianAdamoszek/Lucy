# main.py

from core.speaker import Speaker
from core.actions import open_chrome
from core.actions import open_firefox


speaker = Speaker()

print("Lucy TEST KOMEND")

while True:
    text = input("Wpisz komendę: ")
    text_lower = text.lower()

    if "chrome" in text_lower:
        response = open_chrome()
        print(response)
        speaker.speak(response)

    elif "firefox" in text_lower:
        response = open_firefox()
        print(response)
        speaker.speak(response)
    else:
        print("Nie znam komendy")