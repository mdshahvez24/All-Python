import pyttsx3
import time

repeat = pyttsx3.init()
while True:
  repeat.say("osascript -e \'say \"Hey Harry drink water\"\'; osascript -e \'display alert \"Hey Harry, Drink water\"\'")
  repeat.runAndWait()
  time.sleep(repeat[10])