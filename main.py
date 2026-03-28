# main.py

from core.listener import Listener
from core.speaker import Speaker

listener = Listener()
speaker = Speaker()

print("Lucy ETAP 2 uruchomiona")

# test startowy
speaker.speak("Lucy uruchomiona. Słucham.")

while True:
    text = listener.listen()
    print(f"Ty: {text}")

    # TEST: Lucy powtarza co usłyszy
    speaker.speak(f"Powiedziałeś {text}")