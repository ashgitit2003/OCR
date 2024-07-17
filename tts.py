import pyttsx3

# Initialize the Text-to-speech engine.
engine = pyttsx3.init()

# Open the file to be read.
with open("C:\\Users\\91845\\Desktop\\College mini project 3rd year\\Python_OCR Sem 5 project latest\\output.txt", "r") as f:
    # Read the contents of the file. 
    text = f.read()

# Speak the contents of the file.
engine.say(text)

# Wait for the engine to finish speaking.
engine.runAndWait()