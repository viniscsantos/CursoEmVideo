import pyttsx3

engine = pyttsx3.init()
engine.setProperty("voice", "brazil")
engine.setProperty("rate", "120")

while True:
    frase = input(">")
    if frase != "sair!":
        engine.say(frase)
        engine.runAndWait()
    else:
        break
