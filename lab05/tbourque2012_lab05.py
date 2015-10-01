# COT 4930  Python Programming
# Name: Tyler Bourque
# ID  : tbourque2012
# Lab : 05


#-----------------------------------------

bib = {'\Y': "year", '\B': "book", '\A': "author", '\J': "journal", '\P': "publisher", '\R': "article",
       '\\bibitem': "dio" }

def main( ):
    
    ifile = open( "bib.txt", "r" )

    for line in ifile :
        line = line.strip( )
        if '\\bibitem' in line:
            print("<doi>")
        if not line.strip():
            print("<\doi>")
        commands(line)
        
    ifile.close( )
  
def commands(line):
    
    line = line.rstrip(".")
    line = line.rstrip(",")
    
    if '\\A' in line:
        line = line.replace('\\A',"")
        line = line.lstrip()
        key = '\A'
        if key in bib.keys():
            print("<", bib.get(key), ">", line, "</", bib.get(key), ">", sep = "")
    elif '\\B' in line:
        line = line.replace('\\B',"")
        line = line.lstrip()
        key = '\B'
        if key in bib.keys():
            print("<", bib.get(key), ">", line, "</", bib.get(key), ">", sep = "")
    elif '\\J' in line:
        line = line.replace('\\J',"")
        line = line.lstrip()
        key = '\J'
        if key in bib.keys():
            print("<", bib.get(key), ">", line, "</", bib.get(key), ">", sep = "")
    elif '\\Y' in line:
        line = line.replace('\\Y',"")
        line = line.lstrip()
        key = '\Y'
        if key in bib.keys():
            print("<", bib.get(key), ">", line, "</", bib.get(key), ">", sep = "")        
    elif '\\R' in line:
        line = line.replace('\\R',"")
        line = line.lstrip()
        key = '\R'
        if key in bib.keys():
            print("<", bib.get(key), ">", line, "</", bib.get(key), ">", sep = "")
    elif "invalid" in line:
        print("***unknown command:" , line)
 
main()
 
