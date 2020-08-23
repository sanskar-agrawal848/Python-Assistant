import pyttsx3
import os

while True:
	print(" Please tell what application you want to launch : "  , end='')
	s = input()


	if (("run" in s) or  ("execute" in s) or ("open" in s))  and ("chrome" in s):
	  os.system("start chrome")
	  #pyttsx3.speak("your application is launched successfully")

	elif (("run" in s) or  ("execute" in s) or ("open" in s)) and  (("notepad" in s) or ("editor" in s) ) :
	  os.system("notepad")
	  #pyttsx3.speak("your application is launched successfully")

	elif (("run" in s) or  ("execute" in s) or ("open" in s)) and (("player" in s) or ("media" in s) or ("vlc" in s)):
	  os.system("start vlc")
	  #pyttsx3.speak("your application is launched successfully")
	  
	  
	elif (("run" in s) or  ("execute" in s) or ("open" in s)) and ("firefox" in s):
	  os.system("start firefox")
	  #pyttsx3.speak("your application is launched successfully")
	  
	elif (("run" in s) or  ("execute" in s) or ("open" in s)) and (("calc" in s) or ("calculator" in s)):
	  os.system("calc")
	  #vlcpyttsx3.speak("your application is launched successfully")

	elif  ("exit" in s)  or ("quit" in s):
	  break

	else:
	  print("don't support")

