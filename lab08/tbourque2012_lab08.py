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
        verb = r"\\verb{([^}])}" #Not sure yet
        
        if line.find( "\\chapter" ) != -1:
            
            new_line = re.sub( chapter, r"<H1>\1</H1>", line )
            wfile.write( new_line )
            
        elif line.find( "\\section" ) != -1:
            
            new_line = re.sub( section, r"<H2>\1</H2>", line )
            wfile.write( new_line )
            
        elif line.find( "\\subsection" ) != -1:
            
            new_line = re.sub( subsection, r"<H3>\1</H3>", line )
            wfile.write( new_line )
            
        elif line.find( "\\begin{description}" ) != -1:
            
            new_line = re.sub( description_b, r"<DL>", line )
            wfile.write( new_line )
            
        elif line.find( "\\item[" ) != -1:
            
            new_line = re.sub( item1, r"<DD>\1</DD>", line )
            wfile.write( new_line )
            print(new_line)
            
        elif line.find( "\\end{description}" ) != -1:
            
            new_line = re.sub( description_e, r"</DL>", line )
            wfile.write( new_line )
            
        elif line.find( "\\begin{itemize}" ) != -1:
            
            new_line = re.sub( itemize_b, r"<UL>", line )
            wfile.write( new_line )
            
        elif line.find( "\\item" ) != -1:
            
            new_line = re.sub( item2, r"<LI>\1</LI>", line )
            wfile.write( new_line )
            
        elif line.find( "\\end{itemize}" ) != -1:
            
            new_line = re.sub( itemize_e, r"</UL>", line )
            wfile.write( new_line )
            
        elif line.find( "\\verb" ) != -1:
            
            new_line = re.sub( verb, r"<TT>\1</TT>", line )
            wfile.write( new_line )
            print(new_line)
            
        else:
            
            wfile.write( line )
        
    rfile.close( )
    wfile.close( )
           
main( )
