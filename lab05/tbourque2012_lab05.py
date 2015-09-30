# COT 4930  Python Programming
# Name: Tyler Bourque
# ID  : tbourque2012
# Lab : 05


#-----------------------------------------

bib = { }

def main( ):
    ifile = open( "bib.txt", "r" )

    for line in ifile :
        line = line.strip( )
        line = line.rstrip(".")
        line = line.rstrip(",")
            
        commands(line)
        
    ifile.close( )
  
def commands(line):
    if(line.rfind('}') == -1 ):
        command = line.split(' ', 1)
        bib[line] = command
    else:
        command = line.split('{', 1)
        bib[line] = command
        
    if '\\bibitem' in line:
        print("<doi>")
    elif '\\A' in line:
        line = line.replace('\\A',"")
        line = line.lstrip()
        print("<author>", line, "<\\author>", sep = "")
    elif '\\B' in line:
        line = line.replace('\\B',"")
        line = line.lstrip()
        print("<book>", line, "<\\book>", sep = "")
    elif '\\J' in line:
        line = line.replace('\\J',"")
        line = line.lstrip()
        print("<journal>", line, "<\\journal>", sep = "")
    elif '\\Y' in line:
        line = line.replace('\\Y',"")
        line = line.lstrip()
        print("<year>", line, "<\\year>", sep = "")         
    elif '\\R' in line:
        line = line.replace('\\R',"")
        line = line.lstrip()
        print("<article>", line, "<\\article>", sep = "")
    else:
        if '\\' in line:
            print("***unknown command:" , line )
        else:
            print("<\doi>")
main()

