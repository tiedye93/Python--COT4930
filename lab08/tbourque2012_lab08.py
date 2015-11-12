# COT 4930  Python Programming
# Name: Tyler Bourque
# ID  : tbourque2012
# Lab : 08


#-----------------------------------------

import re

def main( ):
    
    rfile = open("files/re2.tex", "r")
    wfile = open("output/re2.html", "w")
    
    for line in rfile:
        
        chapter = r"\\chapter{([^}]+)}"
        section = r"\\section{([^}]+)}"
        subsection = r"\\subsection{([^}]+)}"
        description_b = r"\\begin{([^}]+)}"
        item1 = r"\\item{([^}]+)}" #Not sure yet
        description_e = r"\\end{([^}]+)}"
        itemize_b = r"\\begin{([^}]+)}"
        item2 = r"\\it{([^}]+)}"
        itemize_e = r"\\end{([^}]+)}"
        verb1 = r"\\verb\W(\W+)\W\W" #Not sure yet
        verb2 = r"\\verb\W\W(\w*)\W"
        verb3 = r"\\verb\W(\W*\w*\W)\W"
        
       
        line = re.sub( chapter, r"<H1>\1</H1>", line )
        line = re.sub( section, r"<H2>\1</H2>", line )
        line = re.sub( subsection, r"<H3>\1</H3>", line )
        line = re.sub( description_b, r"<DL>", line )
        line = re.sub( item1, r"<DD>\1</DD>", line )
        line = re.sub( description_e, r"</DL>", line )       
        line = re.sub( itemize_b, r"<UL>", line )
        line = re.sub( item2, r"<LI>\1</LI>", line )
        line = re.sub( itemize_e, r"</UL>", line )   
        line = re.sub( verb1, r"<TT>\1</TT>", line )
        line = re.sub( verb2, r"<TT>\1</TT>", line )
        line = re.sub( verb3, r"<TT>\1</TT>", line )
            
        wfile.write( line )
        
    rfile.close( )
    wfile.close( )
           
main( )