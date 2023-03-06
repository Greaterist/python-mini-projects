import time
from random import uniform, choice
input = '''Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco'''





def timedPrint(text):
    for i in range(int(len(text))):
        time.sleep(0.1)
        yield text[0:i+1]


for x in timedPrint(input):
    print(x)

##########################################


def timedRandomPrint(text, min = 0.01, max = 1):
    for i in range(int(len(text))):
        time.sleep(uniform(min, max))
        yield text[0:i+1]


for x in timedRandomPrint(input, max=0.02):
    print(x)
        
##########################################
def timedRandomPrintWithMistakes(text, min = 0.01, max = 0.01, chance = 0.2, mistakeLimit = 2, errorLetters='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'):
    output = ""
    i = 0
    mistakes = 0
    isSpotted = False
    while i<= int(len(text)):
        time.sleep(uniform(min, max))
        if (chance>=uniform(0, 1)) and (int(mistakes)<int(mistakeLimit)) and not isSpotted:
            
            mistakes+=1
            output = output + choice(errorLetters)
            #output = text[0:i]+(choice(ascii_letters)*mistakes)
            yield output
        else:
            if mistakes>0:
                mistakes-=1
                isSpotted = True
                output = output[:-1]
            else:
                isSpotted = False
                i+=1
                output = text[0:i]
            yield output

        


for x in timedRandomPrintWithMistakes(input, max=0.1):
    print(x)














