# core/actions.py

import subprocess

def open_chrome():
    try:
        subprocess.Popen(
            "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
        )
        return "Otwieram Chrome"
    except Exception as e:
        return f"Błąd uruchamiania Chrome: {e}"


def open_firefox():
    try:
        subprocess.Popen(
            r"C:\Program Files\Mozilla Firefox\firefox.exe"
        )
        return "Otwieram Firefox"
    except Exception as e:
        return f"Błąd uruchamiania Firefox: {e}"