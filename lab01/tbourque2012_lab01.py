# COT 4930 Python Programming
# Tyler Bourque
# tbourque2012
# Lab : 01

def convertMiles( miles ):
    kilo = miles * 1.609
    print( miles, "Miles is", kilo, "in Kilometers." )
    
userInput = eval( input( "type in a number to convert Miles to Kilometers: " ) )
convertMiles( userInput )
