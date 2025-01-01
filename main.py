import pyttsx3 # Pip install first

def text_to_speech(text):
    # Initialize the Text-to-Speech engine
    engine = pyttsx3.init()
    
    # Set properties before adding text
    engine.setProperty('rate', 150)  # Speed of speech
    engine.setProperty('volume', 1.0)  # Volume level (0.0 to 1.0)
    
    # Speak the text
    engine.say(text)
    engine.runAndWait()


def intake(character,workingString,wordList):
    if(character=="SPACE"):
        wordList.append(workingString)
        text_to_speech(workingString)
        workingString=""
    elif(character=="DELETE"):
        workingString = workingString[:-1]
    elif(character!="NOTHING"):
        workingString+=character
    return workingString,wordList

workingString = ""
wordList = []

workingString,wordList = intake("h",workingString,wordList)
print(workingString)
workingString,wordList = intake("b",workingString,wordList)
print(workingString)
workingString,wordList = intake("DELETE",workingString,wordList)
print(workingString)
workingString,wordList = intake("e",workingString,wordList)
workingString,wordList = intake("l",workingString,wordList)
print(workingString)
workingString,wordList = intake("NOTHING",workingString,wordList)
print(workingString)
workingString,wordList = intake("l",workingString,wordList)
workingString,wordList = intake("o",workingString,wordList)
workingString,wordList = intake("SPACE",workingString,wordList)
print(workingString)
print(wordList)
workingString,wordList = intake("w",workingString,wordList)
workingString,wordList = intake("o",workingString,wordList)
workingString,wordList = intake("r",workingString,wordList)
workingString,wordList = intake("l",workingString,wordList)
workingString,wordList = intake("d",workingString,wordList)
workingString,wordList = intake("SPACE",workingString,wordList)
print(workingString)
print(wordList)