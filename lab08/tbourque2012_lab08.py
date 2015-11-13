# COT 4930  Python Programming
# Name: Tyler Bourque
# ID  : tbourque2012
# Lab : 08


#-----------------------------------------

import re

def main( ):
    
    rfile = open("files/re6.tex", "r")
    wfile = open("output/re6.html", "w")
    
    for line in rfile:
        
        chapter = r"\\chapter{([^}]+)}"
        section = r"\\section{([^}]+)}"
        subsection = r"\\subsection{([^}]+)}"
        description_b = r"\\begin{([^}]+)}"
        item1 = r"\\item\[\\texttt\{(.+)\}\]" #Not sure yet
        description_e = r"\\end{([^}]+)}"
        itemize_b = r"\\begin{([^}]+)}"
        item2 = r"\\item(.+)"
        itemize_e = r"\\end{([^}]+)}"
        verb = r"\\verb\+(\S+)\+"
        
       
        line = re.sub( chapter, r"<H1>\1</H1>", line )
        line = re.sub( section, r"<H2>\1</H2>", line )
        line = re.sub( subsection, r"<H3>\1</H3>", line )
        line = re.sub( description_b, r"<DL>", line )
        line = re.sub( item1, r"<DD>\1</DD>", line )
        line = re.sub( description_e, r"</DL>", line )       
        line = re.sub( itemize_b, r"<UL>", line )
        line = re.sub( item2, r"<LI>\1</LI>", line )
        line = re.sub( itemize_e, r"</UL>", line )   
        line = re.sub( verb, r"<TT>\1</TT>", line )
            
        wfile.write( line )
        
    rfile.close( )
    wfile.close( )
           
main( )