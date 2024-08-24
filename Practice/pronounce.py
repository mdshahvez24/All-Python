# from gtts import gTTS 

import pyttsx3
engine = pyttsx3.init()
engine.say(["Era","Shaad","Jhon","Rihan","Talha","Katrina","Misba"])
engine.runAndWait()






import pyttsx3
import time

repeat = pyttsx3.init()
while True:
  repeat.say("Hey Harry drink water")
  repeat.runAndWait()
  time.sleep(repeat[10])


#   command = "osascript -e \'say \"Hey Harry drink water\"\'; osascript -e \'display alert \"Hey Harry, Drink water\"\'"
#   os.system(command)
#   time.sleep(REPEAT_INTERVAL)