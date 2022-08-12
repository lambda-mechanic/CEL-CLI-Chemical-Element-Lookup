#!/usr/bin/python3
# MIT Open License, 2022
# Creator: Liam Chiasson, Github: @liamchiasson
# CHEM ELEMENT LOOKUP (CLI For Bash)

import os

currentDir = os.path.dirname(os.path.abspath(__file__))
filePath = os.path.join(currentDir, "elements.txt")
stringParts = ["", ""] #list will contain command and specified chemical element as list elements
line = "" # buffer to store each line that the program reads from elements.txt
programClosed = False
userCommand = ""

def errorMessage():
    print("\nError: command not found.\nPlease enter the case-sensitive command as follows: command Element\nOr: Element")
    print("Example 1: mass He")
    print("Example 2: He")

# FOR ALL PROPERTIES OF ONE ELEMENT
def getInfo(specifiedElement): 
    f = open(filePath, "r")
    while(f.closed != True):
        line = f.readline().strip("\n")
        if(line == specifiedElement):
            print(line) # print specified element when located
            for x in range(13): # print all 13 lines of info for specified element
                print(f.readline().strip("\n"))
            f.close()
        elif(line == "@"):
            errorMessage()
            f.close()

# FOR ONE PROPERTY OF ONE ELEMENT
def readAttribute(attrStr, f):
    charHolder = ""
    while(charHolder != "\n"): # check when line is finished
        charHolder = f.read(1)
        if(charHolder != "\n"): # prevent \n from being added to attrStr
            attrStr += charHolder
    print(attrStr)
    f.close()
# FOR ONE PROPERTY OF ONE ELEMENT
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
                elif(attrStr == "Energy Levels: " and attr == "energy"):
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
    spaceTrue = False
    for x in string:
        if x == " ":
            spaceTrue = True
            stringParts[0] = string[:counter] # set zeroeth index as command
            stringParts[1] = string[counter+1:] # set first index as element
        counter += 1
    if(string == ""): # in case of empty input, display error message
       errorMessage()
    elif(spaceTrue == False): # Otherwise, if the original input contained no space character, then set stringParts[1] to string
        stringParts[1] = string

def commandChecker(command):
    parseString(command) # parse command to separate attribute from element

    # ADD THIRD OPTION: what if I want to print a list of all the elements in a particular series? Need a more general command check that accounts for commands that dont include an element
    if(stringParts[0] == ""): # in case of empty command, print all properties of selected element
        getInfo(stringParts[1])
    else:
        getAttribute(stringParts[0], stringParts[1])

print("CEL-CLI: For all available properties, enter a chemical's symbol (ie 'He').\nOtherwise, specify the property and the element(ie 'group He')\nFor a list of commands, please type 'commands'")
while(programClosed == False):
    # get input via terminal here
    userCommand = input()
    if(userCommand == "commands"):
        print("""CEL-CLI COMMANDS:
        name Element: displays element name 
        series Element: displays series of element (i.e. transition metals)
        group Element: displays group of element
        row Element: displays row of element
        mass Element: displays mass of element in atomic mass units
        levels Element: displays the energy levels of the element's electrons
        neg Element: displays the electronegativity of the element
        melt Element: displays the melting point of the element in degrees celsius
        boil Element: displays the boiling point of the element in degrees celsius
        affinity Element: displays electron affinity of element in kj/mol
        fion Element: displays the first ionization energy of the element in kj/mol
        rad Element: displays the atomic radius of the element in picometers
        num Element: displays the atomic number of the element
        """)
    else:
        commandChecker(userCommand) # send command to be parsed and checked in order to select output
    if(input("Would you like to close the program? (y/n): ") == "y"):
        programClosed = True
    else:
        userCommand = ""
        stringParts = ["", ""]
        line = ""
        print("Enter another chemical element and optional command: ")
        #start again