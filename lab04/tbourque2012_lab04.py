# COT 4930  Python Programming
# Name: Tyler Bourque
# ID  : tbourque2012
# Lab : 04


#-----------------------------------------

city_Zip= { }

def make_dict( ):
    ifile = open( "fl_cities.txt", "r" )

    for line in ifile :
        line = line.rstrip( )
        ( zipCode, city ) = line.split( ":" )
        city_Zip[city] = zipCode
        
    ifile.close( )
    
def test_dict( ):
    ifile = open( "fl_maint.txt", "r" )

    for word in ifile :
        word = word.rstrip( )
        (command, argument ) = word.split( "-")
        if(command == 'p'):
            print( 'p' )
            keys = list(city_Zip.keys( ) )
            keys.sort( )
            for cities in keys: 
                print( "%-20s%-5s" % ( cities, city_Zip[cities] ) )
            print( )
        elif(command == 'f'):
            print( 'f' )
            keys = list(city_Zip.keys( ) )
            length = len(keys)
            for cities in keys:
                if argument in cities:
                    print( "%-20s%-5s" % ( cities, city_Zip[cities] ) )
                    length = length - 1
                    break
                elif(length == 1):
                    print( "%-20s%-5s" % (argument, "City Unknown" ) )
                length = length - 1
            print( )
        elif(command == 'c'):
            print( 'c' )
            keys = list(city_Zip.keys( ) )
            (zipCode, location) = argument.split(":")
            length = len(keys)
            for cities in keys:
                if location in cities:
                    city_Zip[cities] = zipCode
                    print( "%-20s%-5s" % ( cities, city_Zip[cities] ) )
                    length = length - 1
                    break
                elif(length == 1):
                    print( "%-20s%-5s" % (location, "City Unknown" ) )
                length = length - 1
            print( )
        else:
            print( command )
            print( "Unknown Command" )
            print( )
            
    ifile.close( )

make_dict( )
print( )
test_dict( )