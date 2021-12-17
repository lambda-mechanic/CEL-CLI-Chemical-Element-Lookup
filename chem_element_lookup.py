# MIT Open License, 2021
# Creator: Liam Chiasson, Github: @liamchiasson

# CHEM ELEMENT LOOKUP (CLI For Bash)
import os

currentDir = os.path.dirname(os.path.abspath(__file__))
filePath = os.path.join(currentDir, "elements.txt")
input = "dw He" # user input variable
stringParts = ["", ""] #list will contain command and specified chemical element as list elements
line = ""

def errorMessage():
    print("Error: command not found.\nPlease enter the case-sensitive command as follows: command Element")
    print("Example: mass He")

def getInfo(specifiedElement):
    f = open(filePath, "r")

    while(f.closed != True):
        line = f.readline().strip("\n")
        if(line == specifiedElement):
            print(line) # print specified element when located
            for x in range(13): 
                print(f.readline().strip("\n"))
            f.close()

        elif(line == "@"):
            errorMessage()
            f.close()

def readAttribute(attrStr, f):
    charHolder = ""
    while(charHolder != "\n"): # check when line is finished
        charHolder = f.read(1)
        if(charHolder != "\n"): # prevent \n from being added to attrStr
            attrStr += charHolder
    print(attrStr)
    f.close()
    
def getAttribute(attr, element):
    attrStr = ""
    f = open(filePath, "r")

    while(f.closed != True):
        line = f.readline().strip("\n")
        if(line == element): # SKIP TO ELEMENT
            
            while(f.closed != True):
                x = f.read(1) # read char by char
                if(x == "\n"): # when there is a new line, reset attrStr
                    attrStr = ""
                elif(x == "@"):
                    f.close()
                    errorMessage()
                else: # otherwise, add x to attrStr
                    attrStr += x
                # Set of if-elif statements to read the specified attribute
                if(attrStr == "Element Name: " and attr == "name"):
                    readAttribute(attrStr, f)
                elif(attrStr == "Series: " and attr == "series"):
                    readAttribute(attrStr, f)
                elif(attrStr == "Group: " and attr == "group"):
                    readAttribute(attrStr, f)
                elif(attrStr == "Row: " and attr == "row"):
                    readAttribute(attrStr, f)
                elif(attrStr == "Atomic Mass(amu): " and attr == "mass"):
                    readAttribute(attrStr, f)
                elif(attrStr == "Energy Levels: " and attr == "levels"):
                    readAttribute(attrStr, f)
                elif(attrStr == "Electronegativity: " and attr == "neg"):
                    readAttribute(attrStr, f)
                elif(attrStr == "Melting Point(deg C): " and attr == "melt"):
                    readAttribute(attrStr, f)
                elif(attrStr == "Boiling Point(deg C): " and attr == "boil"):
                    readAttribute(attrStr, f)
                elif(attrStr == "Electron Affinity(kj/mol): " and attr == "affinity"):
                    readAttribute(attrStr, f)
                elif(attrStr == "First Ion Energy(kj/mol): " and attr == "fion"):
                    readAttribute(attrStr, f)
                elif(attrStr == "Atomic Radius(pm): " and attr == "rad"):
                    readAttribute(attrStr, f)
                elif(attrStr == "Atomic Number: " and attr == "num"):
                    readAttribute(attrStr, f)
        elif (line == "@"):
            f.close()
            errorMessage()

def parseString(string):
    counter = 0
    for x in string:
        if x == " ":
            stringParts[0] = string[:counter] # set zeroeth index as command
            stringParts[1] = string[counter+1:] # set first index as element
        counter += 1

    if(stringParts[0] == "" and stringParts[1] == ""): # in case of no command selected, leave command empty
        stringParts[1] = string 


def commandChecker(command):
    parseString(command) # parse command to separate attribute from element

    if(stringParts[0] == ""): # in case of empty command, print all properties of selected element
        getInfo(stringParts[1])
    else:
        getAttribute(stringParts[0], stringParts[1])

# get input via terminal here
commandChecker(input) # send command to be parsed and checked in order to selet output