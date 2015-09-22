# COT 4930  Python Programming
# Name: Tyler Bourque
# ID  : tbourque2012
# Lab : 02


#-----------------------------------------

#def fibonacci( n ):
#    if n <= 1:
#        return n
#    else:
#        return( fibonacci( n - 1 ) + fibonacci( n - 2 ) )

fibonacci = [ 0 , 1 , 1 , 2 , 3 , 5 , 8 , 13 , 21 , 34 , 55 , 89 , 144 , 233 , 377 , 610 , 987 , 1597 , 2584 , 4181 , 6765  ]
    
nTerms = eval(input( "Type in how many numbers in the Fibonacci sequence should be printed: " ) )

for i in range( 0 , nTerms ):
    if( i % 6 == 0 ):
        print( )    
    print( "%5d" % fibonacci[i] , end = "\t" )
