# COT 4930  Python Programming
# Name: Tyler Bourque
# ID  : tbourque2012
# Lab : 03


#-----------------------------------------

def eratos( n ):
    
    primeNumbers = [ ]
    
    for i in range(2,n):
        primeNumbers.append(i)
      
    composite = 2
    m = 1
    loop = 0
    
    while loop < m:
        for k in primeNumbers[::1]:
            if k == 2:
                pass
            else:
                if k % composite == 0 and k != composite:
                    primeNumbers.remove(k)
                    m = len(primeNumbers)
                    continue
            
        composite += 1
        loop += 1
    
    return primeNumbers

def print_primes( primes ):
     
    for i in range(0, len(primes)):
        if i % 10 == 0:
            print( )
        print( "%5d" % primes[i], end = "\t" )

def main( ):
    
    n = eval(input( "Please type in a number between 2 and 300 to determine the prime numbers: " ) )
    
    if 2 <= n <= 300:
        primes= eratos( n )
        print_primes( primes ) 
        
    else:
         print( "Number is not between 2 and 300!")

main( )
