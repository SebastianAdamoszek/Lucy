# core/speaker.py

import pyttsx3
import threading
import queue
import time

class Speaker:
    def __init__(self):
        self.engine = pyttsx3.init('sapi5')
        self.engine.setProperty('rate', 170)

        voices = self.engine.getProperty('voices')
        voice_set = False

        for v in voices:
            if "pl" in v.id.lower():
                self.engine.setProperty('voice', v.id)
                voice_set = True
                break

        if not voice_set:
            self.engine.setProperty('voice', voices[0].id)

        self.q = queue.Queue()

        # ważne: osobny wątek dla mowy
        self.thread = threading.Thread(target=self._run)
        self.thread.start()

    def _run(self):
        print("🔊 Speaker gotowy")
        while True:
            text = self.q.get()
            if text is None:
                break

            print(f"Lucy: {text}")
            self.engine.say(text)
            self.engine.runAndWait()
            time.sleep(0.05)

    def speak(self, text):
        self.q.put(text)