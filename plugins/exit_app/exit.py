if "exit" or "quit" in command:
  akulai.speak("Are you sure?")
  akulai.listen()
  if command == "yes":
    akulai.speak("Okay, please come again!")
    exit()
  else:
    akulai.speak("Okay, what would you like to say?")
